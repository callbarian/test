import os
import subprocess
import numpy as np
import xml.etree.ElementTree as ET
from datetime import datetime,timedelta
def extract(dir_path):
    
    gt_save_path = os.path.join(dir_path,'gt')
    if not os.path.exists(gt_save_path):
        os.makedirs(gt_save_path)

    folders = sorted(os.listdir(dir_path))

    files = sorted(os.listdir(os.path.join(dir_path,folders[1])))
    
    #stream = open(gt_txt_path,'r')
    #lines = stream.readlines()
    for file in files:
        if file.split('.')[1]=='xml':
            tree = ET.parse(os.path.join(dir_path,folders[1],file))
            '''
            root = tree.getroot()
            header = root.find('header')
            total_frames = header.find('frames').text
            print('total frames',total_frames)
            action = root.find('object').find('action')
            frame = action.findall('frame')
            start = frame[0].find('start').text
            end = frame[0].find('end').text
            print("start,end: ",start,end)
            '''
            tree = ET.parse(os.path.join(dir_path,folders[1],file))
            root = tree.getroot()
            header = root.find('header')
            video_duration = header.find('duration').text
            start_time = root.find('event').find('starttime').text
            event_duration = root.find('event').find('duration').text
            video_duration = datetime.strptime(video_duration,'%H:%M:%S.%f').time()
            start_time = datetime.strptime(start_time,'%H:%M:%S.%f').time()
            event_duration = datetime.strptime(event_duration,'%H:%M:%S.%f').time()
            #print('video_duration: {} ,start_time: {},event_duration: {}'.format(video_duration,start_time,event_duration))
            finish_time = timedelta(hours=start_time.hour,minutes=start_time.minute,seconds=start_time.second) + timedelta(seconds=event_duration.second,minutes=event_duration.minute)
            print('finish_time : {}'.format(finish_time))
            
            start_time_plus10s = timedelta(hours=start_time.hour,minutes=start_time.minute,seconds=start_time.second) - timedelta(seconds=10)

            total_frame = header.find('frames').text
            t_time= float(video_duration.minute*60) + float(video_duration.second)
            s_time = float(start_time.minute*60+start_time.second-10)
            f_time = float(start_time.minute*60+start_time.second)+float(event_duration.minute*60+event_duration.second)
            
            gt_list =[]
            gt_list.extend(np.zeros(int(s_time*30-1)))
            gt_list.extend(np.ones(int((f_time-s_time)*30)))
            gt_list.extend(np.zeros(int((t_time-f_time)*30)))
            np.save(os.path.join(gt_save_path,file.split('.')[0]+'.npy'),gt_list)
            #print('total_frame vs t_frame {} vs {} '.format(total_frame,t_time*30))
            print('first: {} second: {} last: {}'.format(int(s_time*30-1),int((f_time-s_time)*30),int((t_time-f_time)*30)))
            add = int(s_time*30-1)+int((f_time-s_time)*30)+int((t_time-f_time)*30)
            print('length: {} added: {}'.format(len(gt_list),add))
    ''' 
    for video,line in zip(video_list,lines):
        video_path = os.path.join(video_dir,video)
        command = 'ffprobe -select_streams v -show_streams '+video_path+' 2>/dev/null | grep nb_frames | sed -e \'s/nb_frames=//\''
        result = subprocess.Popen([command],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result.wait()
        out = result.communicate()
        frame_num = int(out[0].decode().split('\n')[0])
        #print(frame_num)
        info = line.split('  ')
     
        if(video==info[0]):
            print(info[0])
            count +=1
            gt_file = []
            if info[2]=='-1' and info[4]=='-1':
                print(info[0],' : no anomaly found for first scene ')
                gt_file.extend(np.zeros(frame_num))
            elif info[2]!='-1':
                gt_file.extend(np.zeros(int(info[2])-1))
                gt_file.extend(np.ones(int(info[3])-int(info[2])+1))
                
                if info[4]=='-1':
                    print(info[0],' : no anomaly found for second scene ')
                    print('frame numbers: {}, current_gt_length: {}'.format(frame_num,len(gt_file)))
                    gt_file.extend(np.zeros(frame_num-len(gt_file)))
                else:
                    gt_file.extend(np.ones(int(info[5])-int(info[4])+1))
                    gt_file.extend(np.zeros(frame_num-len(gt_file)))
                    
            print(info[0],'frame_numbers: {} gt_length: {}'.format(frame_num,len(gt_file)))
            save_path = os.path.join(result_path,info[0].split('.')[0]+'.npy')
            np.save(save_path,gt_file)
    '''
            
    #print('total videos processed: ',count)
if __name__ =="__main__": 

    output_dir_path = os.getcwd() + '/clips_dataset/faint/test'
    assert os.path.exists(output_dir_path),'path does not exist, check the path'
    
    extract(output_dir_path)