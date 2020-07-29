import os
import subprocess
import numpy as np

# copying the last frame of the video and adding to itself to make it at least 512 frames long
def expand():
    current_path = os.getcwd()
    video_path = os.path.join(current_path,'videos')
    videos = sorted(os.listdir(video_path))

    result_path = current_path + '/videos_expanded'
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    numpy_video_path = os.path.join(current_path,'test_frame_mask')
    gt_files = sorted(os.listdir(numpy_video_path))

    for video,gt_file in videos,gt_files:

        gt_file_path = os.path.join(numpy_video_path,gt_file)
        gt_loaded = np.load(gt_file_path)
        if gt_loaded.shape[0] < 512:
            input_video_path = os.path.join(video_path,video)
            output_video_path = os.path.join(result_path,video)
            file_name = video.split('.')[0] +'.jpg'
            #print(os.path.join(output_video_path,file_name))
            result = subprocess.Popen(['ffmpeg','-sseof','-3','-i',input_video_path,'-update','1', '-q:v','1',os.path.join(result_path,file_name)],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)

            command = 'ffmpeg -i ' + file_path + ' -loop 1 -framerate 25 -t 15 -i ' + output_video_path + ' -filter_complex \"[0]scale=320x240,setsar=1[im];[1]scale=320x240,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0\" ' + concat_path
            result = subprocess.Popen([command],shell=True,stdout=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)

            if gt_loaded[-1]==0:
                zeros = np.zeros(25*15)
                gt_loaded.extend(zeros)
            else:
                ones = np.ones(25)
                zeros =  np.zeros(25*14)
                gt_loaded.extend(ones)
                gt_loaded.extend(zeros)
            np.save(gt_file_path,gt_loaded)
        

if __name__ == "__main__":
    expand()

