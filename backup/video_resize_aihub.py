import os
import subprocess

def resize(dir_path,out_path):
    files = sorted(os.listdir(dir_path))
    for file in files:
        if file.split('.')[1]=='mp4':
            output_file = file.split('.')[0]+'_resize.mp4'
            command = 'ffmpeg -i ' + os.path.join(dir_path,file) + ' -filter:v scale="720:trunc(ow/a/2)*2" -c:a copy ' + os.path.join(out_path,output_file)
            result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)

            command = 'mv ' + os.path.join(dir_path,output_file) + ' ' + out_path
            result = subprocess.Popen([command],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print("moved {} to {}".format(output_file,out_path))
        else:
            command = 'cp ' + os.path.join(dir_path,file) + ' ' + out_path
            result = subprocess.Popen([command],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print("moved {} to {}".format(file,out_path))
if __name__ == "__main__":
    #input 폴더 지정
    path = os.getcwd() + '/faint/outsidedoor_02'
    # output 폴더 지정
    out_path = os.getcwd() +'/resized_dataset/faint/outsidedoor_02'
    folders = sorted(os.listdir(path))
    
    for i,folder in enumerate(folders):
        if folder =='.DS_Store':
            continue
        input_dir_path = os.path.join(path,folder)
        output_dir_path = os.path.join(out_path,folder)
        if not os.path.exists(output_dir_path):
            os.makedirs(output_dir_path)
        resize(input_dir_path,output_dir_path)