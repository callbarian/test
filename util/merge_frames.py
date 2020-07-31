import os
import subprocess

def merge():
    current_path = os.getcwd()
    frame_path = os.path.join(current_path,'frames')
    videos = sorted(os.listdir(frame_path))

    result_path = current_path + '/videos'
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    for video in videos:
        input_video_path = os.path.join(frame_path,video)
        input_video_path = input_video_path + '/%03d.jpg'
        #print(input_video_path)
        output_video_path = os.path.join(result_path,video)
        #input_video_path = '\"' + input_video_path + '\"'
        #print(input_video_path)
        file_name = video +'.mp4'
        if not os.path.exists(output_video_path):
            os.makedirs(output_video_path)
        #print(os.path.join(output_video_path,file_name))
        result = subprocess.Popen(['ffmpeg','-y','-start_number','0','-i', input_video_path,'-c:v','libx264','-r','24.97','-pix_fmt', 'yuv420p', os.path.join(output_video_path,file_name)],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.wait()
        output = result.communicate()
        print(output)

if __name__ == "__main__":
    merge()
