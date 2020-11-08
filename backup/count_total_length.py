import os
import subprocess
import numpy as np

def count_gt(dir_path,fps,normal,count_all):
    files = sorted(os.listdir(dir_path))
    total_length_arr = []
    
    count = 0
    for file in files:
        if file.split('.')[1]!='mp4':
            continue
        count+=1
        file_path = os.path.join(dir_path,file)
        result = subprocess.Popen(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', '-sexagesimal', file_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result.wait()
        out = result.communicate()
        print('file :{} duration: {}'.format(file,out))
        
        time = out[0].decode().split(':')
        minutes = int(time[1])
        seconds = int(time[2].split('.')[0])
        total_length = minutes*60 + seconds
        total_length_arr.append(total_length)
        #make numpy gt
    total_length_dataset = np.sum(total_length_arr,axis=0)
    print('\n',count,total_length_dataset,'\n')
    count_all.append(count)
    return total_length_dataset
    
if __name__ == "__main__":
    fps = 30
    # for full dataset uncomment
    '''
    path = os.getcwd() + '/resized_dataset/faint/outsidedoor_11'
    folders = sorted(os.listdir(path))
    total_length_dataset = 0
    for folder in folders:
        if folder == ".DS_Store":
            continue
        total_length_dataset += count_gt(os.path.join(path,folder),fps,True)
    
    seconds = int(total_length_dataset%60)
    minutes = int(total_length_dataset/60)
    hours = int(minutes/60)
    minutes = int(minutes%60)
    print('hours: {}, minutes: {}, seconds: {} '.format(hours,minutes,seconds))
    #for test and training minisets, uncomment
    '''
    # True for normal gt
    normal_path_train = os.getcwd() +'/clips_dataset/faint/train/insidedoor_01_normal'
    normal_path_test = os.getcwd() +'/clips_dataset/faint/test/insidedoor_01_normal'
    total_length_normal = 0
    count_normal = []
    total_length_normal += count_gt(normal_path_train,fps,True,count_normal)
    total_length_normal += count_gt(normal_path_test,fps,True,count_normal)

    seconds = int(total_length_normal%60)
    minutes = int(total_length_normal/60)
    hours = int(minutes/60)
    print('\n Normal hours: {}, minutes: {}, seconds: {}, occurance: {} \n'.format(hours,minutes,seconds,np.sum(count_normal,axis=0)))

    # False for abnormal gt
    abnormal_path_train = os.getcwd() +'/clips_dataset/faint/train/insidedoor_01_abnormal'
    abnormal_path_test = os.getcwd() +'/clips_dataset/faint/test/insidedoor_01_abnormal'
    total_length_abnormal = 0
    count_abnormal = []
    total_length_abnormal += count_gt(abnormal_path_train,fps,False,count_abnormal)
    total_length_abnormal += count_gt(abnormal_path_test,fps,False,count_abnormal)

    seconds = int(total_length_abnormal%60)
    minutes = int(total_length_abnormal/60)
    hours = int(minutes/60)
    print('\n Abnormal hours: {}, minutes: {}, seconds: {}, occurance: {} \n'.format(hours,minutes,seconds,np.sum(count_abnormal,axis=0)))
    
