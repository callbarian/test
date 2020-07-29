import os
import subprocess

def merge():
    current_path = os.getcwd()
    video_path = os.path.join(current_path,'videos')
    videos = sorted(os.listdir(frame_path))

    result_path = current_path + '/frame'
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    for video in videos:
        input_video_path = os.path.join(video_path,video)
        #input_video_path = input_video_path + '/%03d.jpg'
        #print(input_video_path)
        output_directory_path = os.path.join(result_path,video.split('.')[0])
        #input_video_path = '\"' + input_video_path + '\"'
        #print(input_video_path)
        file_name = video.split('.')[0] +'%03d.jpg'
        if not os.path.exists(output_video_path):
            os.makedirs(output_video_path)
        #print(os.path.join(output_video_path,file_name))
        result = subprocess.Popen(['ffmpeg','-i',input_video_path,'-r','1/1', os.path.join(output_directory_path,file_name)],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.wait()
        output = result.communicate()
        print(output)

if __name__ == "__main__":
    merge()
