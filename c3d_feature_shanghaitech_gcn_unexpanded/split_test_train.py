import os
import numpy as np
import subprocess

def split():
    input_dir = os.getcwd() + '/c3d_feature_shanghaitech'
    normal_dir = os.path.join(input_dir,'train/features')
    abnormal_dir = os.path.join(input_dir,'test/features')
    
    gt_normal_dir = os.path.join(input_dir,'train/gt')
    gt_abnormal_dir = os.path.join(input_dir,'test/gt')

    save_train_path_normal = os.getcwd() + '/train/normal'
    save_train_path_abnormal = os.getcwd() + '/train/abnormal'


    save_test_path_combined = os.getcwd() + '/test'
    gt_save_test_path_combined = os.getcwd() + '/gt_test'

    path_list = []
    path_list.append(save_train_path_normal)
    path_list.append(save_train_path_abnormal)
    path_list.append(save_test_path_combined)
    path_list.append(gt_save_test_path_combined)

    for path in path_list:
        if not os.path.exists(path):
            os.makedirs(path)

    test_split = os.getcwd() + '/test_split.txt'
    train_split = os.getcwd() + '/train_split.txt'

    test_list = []
    train_list = []
    with open(train_split,'r') as f:
        train_list = f.readlines()
        train_list = [item.split('\n')[0] for item in train_list]
    with open(test_split,'r') as f:
        test_list = f.readlines()
        test_list = [item.split('\n')[0] for item in test_list]
    print('length of train_list : {} and the list: {}'.format(len(train_list),train_list))
    print('length of test_list : {} and the list: {}'.format(len(test_list),test_list))

    normal_list = sorted(os.listdir(normal_dir))
    abnormal_list = sorted(os.listdir(abnormal_dir))

    for item in train_list:
        if item+'.txt' in normal_list:
            result = subprocess.Popen(['cp',os.path.join(normal_dir,item+'.txt'),save_train_path_normal],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)
        elif item+'.txt' in abnormal_list:
            result = subprocess.Popen(['cp',os.path.join(abnormal_dir,item+'.txt'),save_train_path_abnormal],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)
    
    for item in test_list:
        if item+'.txt' in normal_list:
            result = subprocess.Popen(['cp',os.path.join(normal_dir,item+'.txt'),save_test_path_combined],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)

            result = subprocess.Popen(['cp',os.path.join(gt_normal_dir,item+'.npy'),gt_save_test_path_combined],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)

        elif item+'.txt' in abnormal_list:
            result = subprocess.Popen(['cp',os.path.join(abnormal_dir,item+'.txt'),save_test_path_combined],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)

            result = subprocess.Popen(['cp',os.path.join(gt_abnormal_dir,item+'.npy'),gt_save_test_path_combined],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)

if __name__ == "__main__":
    split()
