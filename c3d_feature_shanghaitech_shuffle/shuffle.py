import os
import numpy as np
import subprocess

def shuffle_videos():
    input_dir = os.getcwd() + '/c3d_feature_shanghaitech'
    normal_dir = os.path.join(input_dir,'train/features')
    abnormal_dir = os.path.join(input_dir,'test/features')
    
    gt_normal_dir = os.path.join(input_dir,'train/gt')
    gt_abnormal_dir = os.path.join(input_dir,'test/gt')

    save_train_path_normal = os.getcwd() + '/train/normal'
    save_train_path_abnormal = os.getcwd() + '/train/abnormal'


    save_test_path_combined = os.getcwd() + '/test'
    gt_save_test_path_combined = os.getcwd() + '/gt_test'
    normal_list = sorted(os.listdir(normal_dir))
    abnormal_list = sorted(os.listdir(abnormal_dir))

    normal_list_num = len(normal_list)
    abnormal_list_num = len(abnormal_list)

    normal_list = np.random.permutation(normal_list)
    abnormal_list = np.random.permutation(abnormal_list)

    save_train_normal = normal_list[0:int(normal_list_num*3/4)]
    save_train_abnormal = abnormal_list[0:int(abnormal_list_num*3/4)]

    save_test_normal = normal_list[int(normal_list_num*3/4):]
    save_test_abnormal = abnormal_list[int(abnormal_list_num*3/4):]

    for video in save_train_normal:
        result = subprocess.Popen(['cp',os.path.join(normal_dir,video),save_train_path_normal],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.wait()
        output = result.communicate()
        print(output)
    for video in save_train_abnormal:
        result = subprocess.Popen(['cp',os.path.join(abnormal_dir,video),save_train_path_abnormal],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.wait()
        output = result.communicate()
        print(output)
    
    for video in save_test_normal:
        result = subprocess.Popen(['cp',os.path.join(normal_dir,video),save_test_path_combined],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.wait()
        output = result.communicate()
        print(output)

        result = subprocess.Popen(['cp',os.path.join(gt_normal_dir,video.split('.')[0]+'.npy'),gt_save_test_path_combined],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.wait()
        output = result.communicate()
        print(output)
    for video in save_test_abnormal:
        result = subprocess.Popen(['cp',os.path.join(abnormal_dir,video),save_test_path_combined],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.wait()
        output = result.communicate()
        print(output)

        result = subprocess.Popen(['cp',os.path.join(gt_abnormal_dir,video.split('.')[0]+'.npy'),gt_save_test_path_combined],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.wait()
        output = result.communicate()
        print(output)

    
if __name__ == "__main__":
    shuffle_videos()