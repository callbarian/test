import os
import subprocess

def split(dir_path,path_normal,path_abnormal):    
        
    files = sorted(os.listdir(dir_path))
    if not os.path.exists(path_normal):
        os.makedirs(path_normal)
    if not os.path.exists(path_abnormal):
        os.makedirs(path_abnormal)

    for file in files:
        if file == '.DS_Store':
            continue
        
        if int(file.split('.')[0].split('_')[6])==1 or int(file.split('.')[0].split('_')[6])==3:
        
            command = 'cp ' + os.path.join(dir_path,file) + ' ' + path_normal
            result = subprocess.Popen([command],stderr=subprocess.PIPE,shell=True)
            result.wait()
            out = result.communicate()
            print(out)

        elif int(file.split('.')[0].split('_')[6])==2:
            command = 'cp ' + os.path.join(dir_path,file) + ' ' + path_abnormal
            result = subprocess.Popen([command],stderr=subprocess.PIPE,shell=True)
            result.wait()
            out = result.communicate()
            print(out)
            
if __name__ =="__main__":
    dir_path = 'faint/train/feature'
    path = os.getcwd() +'/clips_dataset/'+ dir_path
    path_normal = os.path.join(path,'normal')
    path_abnormal = os.path.join(path,'abnormal')

    assert path,'directory does not exist, check the directory'
    
    split(path,path_normal,path_abnormal)