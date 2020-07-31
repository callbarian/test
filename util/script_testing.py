from __future__ import absolute_import, print_function
import os
import utils
import torch
from torchvision import transforms
from torch.utils.data import DataLoader
import numpy as np
import data
import scipy.io as sio
from options.testing_options import TestOptions
import utils
import time
from models import AutoEncoderCov3D, AutoEncoderCov3DMem

###
opt_parser = TestOptions()
opt = opt_parser.parse(is_print=True)
use_cuda = opt.UseCUDA
device = torch.device("cuda" if use_cuda else "cpu")

###
batch_size_in = opt.BatchSize #1
chnum_in_ = opt.ImgChnNum      # channel number of the input images
framenum_in_ = opt.FrameNum  # frame number of the input images in a video clip
mem_dim_in = opt.MemDim
sparse_shrink_thres = opt.ShrinkThres

img_crop_size = 0

######
model_setting = utils.get_model_setting(opt)

## data path
data_root = opt.DataRoot + opt.Dataset + '/'
data_frame_dir = data_root + 'testing/'
data_idx_dir = data_root + 'testing_idx/'

############ model path
model_root = opt.ModelRoot
model_path = os.path.join(model_root, model_setting + '.pt')

### test result path
te_res_root = opt.OutRoot
te_res_path = te_res_root + '/' + 'res_' + model_setting
utils.mkdir(te_res_path)

###### loading trained model
if (opt.ModelName == 'AE'):
    model = AutoEncoderCov3D(chnum_in_)
elif(opt.ModelName=='MemAE'):
    model = AutoEncoderCov3DMem(chnum_in_, mem_dim_in, shrink_thres=sparse_shrink_thres)
else:
    model = []
    print('Wrong Name.')

##
model_para = torch.load(model_path)
model.load_state_dict(model_para)
model.to(device)
model.eval()

##
frame_trans = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
unorm_trans = utils.UnNormalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))

# ##
video_list = utils.get_subdir_list(data_idx_dir)
video_num = len(video_list)

##
with torch.no_grad():
    for ite_vid in range(video_num):
        video_name = video_list[ite_vid]
        video_idx_path = os.path.join(data_idx_dir, video_name)  # idx path of the current sub dir
        video_frame_path = os.path.join(data_frame_dir, video_name)  # frame path of the current sub dir
        # info for current video
        idx_name_list = [name for name in os.listdir(video_idx_path) \
                         if os.path.isfile(os.path.join(video_idx_path, name))]
        idx_name_list.sort()
        # load data (frame clips) for single video
        video_dataset = data.VideoDatasetOneDir(video_idx_path, video_frame_path, transform=frame_trans)
        video_data_loader = DataLoader(video_dataset,
                                       batch_size=batch_size_in,
                                       shuffle=False,
                                       )
        # testing results on a single video sequence
        print('[vidx %d/%d] [vname %s]' % (ite_vid+1, video_num, video_name))
        recon_error_list = [None] * len(video_data_loader)
        recon_std_list = [None] * len(video_data_loader)
        #
        for batch_idx, (item, frames) in enumerate(video_data_loader):
            idx_name = idx_name_list[item[0]]
            idx_data = np.load(os.path.join(video_idx_path, idx_name))
            print(os.path.join(video_idx_path, idx_name))
            print(idx_data)
            #v_name = idx_data['v_name'][0]  # video name
            #frame_idx = idx_data['idx'][0, :]  # frame index list for a video clip
            ######
            frames = frames.to(device)
            ##
            if (opt.ModelName == 'AE'):
                recon_frames = model(frames)
                ###### calculate reconstruction error (MSE)
                recon_np = utils.vframes2imgs(unorm_trans(recon_frames.data), step=1, batch_idx=0)
                input_np = utils.vframes2imgs(unorm_trans(frames.data), step=1, batch_idx=0)
                r = utils.crop_image(recon_np, img_crop_size) - utils.crop_image(input_np, img_crop_size)
                # recon_error = np.mean(sum(r**2)**0.5)
                recon_error = np.mean(r ** 2)  # **0.5
            elif (opt.ModelName == 'MemAE'):
                recon_res = model(frames)
                recon_frames = recon_res['output']
                recon_np = utils.vframes2imgs(unorm_trans(recon_frames.data), step=1, batch_idx=0)
                input_np = utils.vframes2imgs(unorm_trans(frames.data), step=1, batch_idx=0)
                r = utils.crop_image(recon_np, img_crop_size) - utils.crop_image(input_np, img_crop_size)
                sp_error_map = sum(r ** 2)**0.5
                recon_error = np.mean(sp_error_map.flatten())
                ##
            else:
                recon_error = -1
                print('Wrong ModelName.')
            recon_error_list[batch_idx] = recon_error
        np.save(os.path.join(te_res_path, video_name + '.npy'), recon_error_list)

## evaluation
utils.eval_video(data_root, te_res_path, is_show=False)
