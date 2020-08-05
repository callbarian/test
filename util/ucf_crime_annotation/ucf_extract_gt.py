import os
import subprocess
import numpy as np

def extract():
    gt_txt_path = os.getcwd() +'/Temporal_Anomaly_Annotation_for_Testing_Videos.txt'
    video_dir = os.getcwd() + '/test_videos'
    result_path = os.getcwd() + '/gt'
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    video_list = sorted(os.listdir(video_dir))
    
    stream = open(gt_txt_path,'r')
    lines = stream.readlines()
    count = 0
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

            
    print('total videos processed: ',count)
if __name__ =="__main__": 
    extract()