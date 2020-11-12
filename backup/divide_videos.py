import os
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime,timedelta

# divide videos into multiple clips
# length is set to 1 minute(60 seconds)
#ffmpeg -i 101-1_cam01_swoon01_place03_day_spring_resize.mp4 -c copy -c:v libx264 -crf 22 -map 0 -segment_time 60 -reset_timestamps 1 -segment_format_options movflags=+faststart -g 30 -sc_threshold 0 -f segment output%02d.mp4
# for precision

#ffmpeg -i 101-1_cam02_swoon01_place03_day_spring_resize.mp4 -c copy -segment_time 60 -reset_timestamps 1 -f segment output%02d.mp4
# for fast extraction

def divide(dir_path):
    files = sorted(os.listdir(dir_path))
    for file in files:
        if file.split('.')[1]=='mp4':
            tree = ET.parse(os.path.join(dir_path,file.split('_resize')[0]+'.xml'))
            root = tree.getroot()
            header = root.find('header')
            video_duration = header.find('duration').text
            start_time = root.find('event').find('starttime').text
            event_duration = root.find('event').find('duration').text
            video_duration = datetime.strptime(video_duration,'%H:%M:%S.%f').time()
            start_time = datetime.strptime(start_time,'%H:%M:%S.%f').time()
            event_duration = datetime.strptime(event_duration,'%H:%M:%S.%f').time()
            print('video_duration: {} ,start_time: {},event_duration: {}'.format(video_duration,start_time,event_duration))
            finish_time = timedelta(hours=start_time.hour,minutes=start_time.minute,seconds=start_time.second) + timedelta(seconds=event_duration.second,minutes=event_duration.minute)
            print('start+event duration : {}'.format(finish_time))
            
            # 10초 땡깁니다
            start_time_plus10s = timedelta(hours=start_time.hour,minutes=start_time.minute,seconds=start_time.second) - timedelta(seconds=10)
           
            # 01번 정상 비디오
            output_file = file.split('resize')[0]+'01.mp4'
            command = 'ffmpeg -i ' + os.path.join(dir_path,file) + ' -ss 00:00:00' + ' -to ' + str(start_time_plus10s) +' -c:v libx264 ' + os.path.join(dir_path,output_file)
            result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)

            # 02번 Anomaly 비디오(10초 앞으로 땡김,길이가 결과적으로 10초 늘어남)
            output_file = file.split('resize')[0]+'02.mp4'
            command = 'ffmpeg -i ' + os.path.join(dir_path,file) + ' -ss ' + str(start_time_plus10s) + ' -to ' + str(finish_time) +' -c:v libx264 ' + os.path.join(dir_path,output_file)
            result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)
            
            # 03번 정상 비디오
            output_file = file.split('resize')[0]+'03.mp4'
            command = 'ffmpeg -i ' + os.path.join(dir_path,file) + ' -ss ' + str(finish_time) +' -to ' + str(video_duration) +' -c:v libx264 ' + os.path.join(dir_path,output_file)
            result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
            result.wait()
            output = result.communicate()
            print(output)
            print('\n\n',os.path.join(dir_path,output_file),'\n\n')

            # 원본 비디오 삭제
            command = 'rm ' + os.path.join(dir_path,file) 
            result = subprocess.Popen([command],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print("divided {} to {}".format(file,output_file))
        else:
            continue
        
if __name__ == "__main__":
    # input 폴더 경로 지정(파일 resized 된 후 진행)
    folder_dir = os.getcwd() + '/resized_dataset/faint/outsidedoor_10'
    dirs = sorted(os.listdir(folder_dir))

    # output 폴더 경로 지정
    output_dir_path = os.getcwd() + '/clips_dataset/faint/outsidedoor_10'
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    
    # input 폴더를 output폴더로 복사후 자르기 진행
    for file_dir in dirs:
        input_dir_path = os.path.join(folder_dir,file_dir)
        command = 'cp -r ' + input_dir_path + ' ' + output_dir_path
        result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
        result.wait()
        output = result.communicate()
        print(output)

        divide(os.path.join(output_dir_path,file_dir))

