import os
import subprocess
import numpy as np

def make_gt(dir_path,gt_dir_path,fps,normal = True):
    files = sorted(os.listdir(dir_path))
    for file in files:
        file_path = os.path.join(dir_path,file)
        save_path = os.path.join(gt_dir_path,file)
        result = subprocess.Popen(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', '-sexagesimal', file_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result.wait()
        out = result.communicate()
        print('file :{} duration: {}'.format(file,out))
        
        time = out[0].decode().split(':')
        minutes = int(time[1])
        seconds = int(time[2].split('.')[0])
        total_length = minutes*60 + seconds
        
        #make numpy gt
        if normal == True:
            save_path = save_path.split('.')[0] + '.npy'
            gt_numpy = np.zeros(int(total_length*fps))
            np.save(save_path,gt_numpy)
        else:
            save_path = save_path.split('.')[0] + '.npy'
            gt_numpy = np.ones(int(total_length*fps))
            np.save(save_path,gt_numpy)
def concat_gt(normal_path,abnormal_path,output_path):
    normal_files = sorted(os.listdir(normal_path))
    abnormal_files = sorted(os.listdir(abnormal_path))
    for normal,abnormal,i in zip(normal_files,abnormal_files,range(len(normal_files))):
        normal_np = []
        abnormal_np = []
        if normal.split('.')[1] == 'npy':
            normal_np = np.load(os.path.join(normal_path,normal))
        else:
            continue
        if abnormal.split('.')[1] == 'npy':
            abnormal_np = np.load(os.path.join(abnormal_path,abnormal))
        else:
            continue
        concat_np = np.hstack([normal_np,abnormal_np])
        np.save(os.path.join(os.getcwd()+'/mix'+str(i)+'.npy'),concat_np)

if __name__ == "__main__":
    fps = 30
    save_path = os.getcwd() +'/outsidedoor_11_gt'
    # True for normal gt
    normal_path = os.getcwd() +'/outsidedoor_11_normal'
    make_gt(normal_path,save_path,fps,True)

    # False for abnormal gt
    abnormal_path = os.getcwd() +'/outsidedoor_11_abnormal'
    make_gt(abnormal_path,save_path,fps,False)


    #concat_gt(normal_path,abnormal_path,os.getcwd())


