import os 
import subprocess

cur_path = os.getcwd()
files = sorted(os.listdir(cur_path))
for file in files:
    file_path = cur_path+'/'+file.split('.')[0]+'_'+'%03d.mp4'
    print(file_path)
    command = 'ffmpeg -i ' + os.path.join(cur_path,file) + ' -c copy -segment_time 5 -reset_timestamps 1 -f segment ' + file_path
    result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
    result.wait()
    message = result.communicate()
    print(message)