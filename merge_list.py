import os
import subprocess

def merge():
    merge_list_root = os.getcwd() + '/merge_videos'
    save_root = merge_list_root + '/merged_videos'
    if not os.path.exists(save_root):
        os.makedirs(save_root)
    for merge_list in sorted(os.listdir(merge_list_root)):
        list_path = os.path.join(merge_list_root,merge_list)
        save_path = save_root + '/' + merge_list.split('.')[0] + '.mp4'
        result = subprocess.Popen(['ffmpeg','-f','concat','-safe','0','-i',list_path,'-c','copy',save_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print(result.communicate())
        result.wait()
        

if __name__ =="__main__":
    merge()
