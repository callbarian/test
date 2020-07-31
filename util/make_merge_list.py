import os

def make_list():
    video_root = os.getcwd() + '/videos'
    save_list_root = os.getcwd() + '/merge_videos'
    i = 0
    first_video_path = [''] 
    first_video = ['']
    
    second_video_path = ['']
    second_video = ['']
    
    #incase of merging 3 videos

    camera2_num = 3
    camera4_num = 9
    camera10_num = 5

    for video in sorted(os.listdir(video_root)):
        camera_number = int(video.split('_')[0]) 
        if camera_number is 2 or camera_number is 4 or camera_number is 10:
            if camera_number is 2:
                camera2_num-=1
                if(camera2_num<=2):
                    i=merge_3_videos(i,video_root,save_list_root,video,first_video,first_video_path,second_video,second_video_path)
                else:
                    i=merge_2_videos(i,video_root,save_list_root,video,first_video,first_video_path)
            elif camera_number is 4:
                camera4_num-=1
                if(camera4_num<=2):
                    i=merge_3_videos(i,video_root,save_list_root,video,first_video,first_video_path,second_video,second_video_path)
                else:
                    i=merge_2_videos(i,video_root,save_list_root,video,first_video,first_video_path)
            else:
                camera10_num-=1
                if(camera10_num<=2):
                    i=merge_3_videos(i,video_root,save_list_root,video,first_video,first_video_path,second_video,second_video_path)
                else:
                    i=merge_2_videos(i,video_root,save_list_root,video,first_video,first_video_path)

            
            continue
            #skipping camera number 2,4,10 since they have videos amount in odd numbers
        else:
            i=merge_2_videos(i,video_root,save_list_root,video,first_video,first_video_path)

def merge_2_videos(i,video_root,save_list_root,video,first_video,first_video_path):
    if i is 0:
        first_video_path[0] = os.path.join(video_root,video+'/'+video+'.mp4')
        first_video[0] = video
        #i+=1
        return i+1 
    else:
        second_video_path = os.path.join(video_root,video+'/'+video+'.mp4')
        save_path = first_video[0] + '-' + video + '.txt'
        with open(os.path.join(save_list_root,save_path),'w') as f:
            first_line = "file " + "\'" + first_video_path[0] + "\'" + "\n"
            second_line = "file " + "\'" +second_video_path + "\'"
            combined = first_line + second_line
            f.write(combined)
            f.close()
        return i-1
def merge_3_videos(i,video_root,save_list_root,video,first_video,first_video_path,second_video,second_video_path):
    if i is 0:
        first_video_path[0] = os.path.join(video_root,video+'/'+video+'.mp4')
        first_video[0] = video
        #i+=1
        return i+1 
    elif i is 1:
        second_video_path[0] = os.path.join(video_root,video+'/'+video+'.mp4')
        second_video[0] = video
        return i+1

    else:
        third_video_path = os.path.join(video_root,video+'/'+video+'.mp4')
        save_path = first_video[0] + '-' + second_video[0] + '-' +video+'.txt'
        with open(os.path.join(save_list_root,save_path),'w') as f:
            first_line = "file " + "\'" + first_video_path[0] + "\'" + "\n"
            second_line = "file " + "\'" +second_video_path[0] + "\'" + "\n"
            third_line = "file " + "\'" +third_video_path + "\'" 
            combined = first_line + second_line +third_line
            f.write(combined)
            f.close()
        return 0   


if __name__ == "__main__":
    make_list()


'''
if i is 0:
            first_video_path = os.path.join(video_root,video+'/'+video+'.mp4')
            first_video = video
            i+=1
            continue
        else:
            i-=1
            second_video_path = os.path.join(video_root,video+'/'+video+'.mp4')
            save_path = first_video + '-' + video
            with open(os.path.join(save_list_root,save_path),'w') as f:
                first_line = "file " + "\'" + first_video_path + "\'" + "\n"
                second_line = "file " + "\'" +second_video_path + "\'"
                combined = first_line + second_line
                f.write(combined)
                f.close()

'''
