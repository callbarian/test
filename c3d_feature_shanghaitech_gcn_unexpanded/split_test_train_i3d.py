import os
import numpy as np
import subprocess

def split():
    test_path = os.getcwd() +'/test'
    train_normal_path = os.getcwd() + '/train/normal'
    train_abnormal_path = os.getcwd() + '/train/abnormal'

    i3d_path = os.getcwd() +'/i3d_combine'
    save_test_path = os.getcwd() + '/i3d/test'
    save_train_path = os.getcwd() +'/i3d/train'
    if not os.path.exists(save_test_path):
        os.makedirs(save_test_path)
    if not os.path.exists(save_train_path):
        os.makedirs(save_train_path)
        os.makedirs(save_train_path+'/normal')
        os.makedirs(save_train_path+'/abnormal')
    
    test_list = sorted(os.listdir(test_path))
    train_normal_list = sorted(os.listdir(train_normal_path))
    train_abnormal_list = sorted(os.listdir(train_abnormal_path))

    i3d_list = sorted(os.listdir(i3d_path))

    for video in i3d_list:
        if video in test_list:
            result = subprocess.Popen(['cp',os.path.join(i3d_path,video),save_test_path],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)
        elif video in train_normal_list:
            result = subprocess.Popen(['cp',os.path.join(i3d_path,video),os.path.join(save_train_path,'normal')],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)
        elif video in train_abnormal_list:
            result = subprocess.Popen(['cp',os.path.join(i3d_path,video),os.path.join(save_train_path,'abnormal')],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)
        
if __name__ == "__main__":
    split()