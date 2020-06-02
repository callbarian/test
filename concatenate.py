import subprocess
import os


#result = subprocess.Popen(['ffmpeg', '-i', '/Users/iseongmin/Downloads/test/test_Video/Thief_face_caught_resize.mp4', '-loop', '1', '-framerate', '25', '-t', '30', '-i', '/Users/iseongmin/Downloads/test/test_Video/001_resize.jpg', '-filter_complex', "[0]scale=320x240,setsar=1[im];[1]scale=320x240,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0", 'output_concat2.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

#(out,err) = result.communicate()

result = subprocess.Popen(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', '-sexagesimal', '/Users/iseongmin/Downloads/test/test_Video/output.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out = result.communicate()
result.wait()
time = out[0].decode().split(':')

minute = int(time[1])
seconds = int(time[2].split('.')[0])
print(time)
print(minute)
print(seconds)
print('\"mynameis\"')

#tempstring = '''ffmpeg -i /Users/iseongmin/Downloads/test/test_Video/Thief_face_caught_resize.mp4 -loop 1 -framerate 25 -t 30 -i /Users/iseongmin/Downloads/test/test_Video/001_resize.jpg -filter_complex "[0]scale=320x240,setsar=1[im];[1]scale=320x240,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0" /Users/iseongmin/Downloads/test/test_Video/output_concat3.mp4'''

tempstring = 'ffmpeg -i ' + '/Users/iseongmin/Downloads/test/test_Video/Thief_face_caught_resize.mp4' + ' -loop 1 -framerate 25 -t 30 -i ' + '/Users/iseongmin/Downloads/test/test_Video/001_resize.jpg' + ' -filter_complex \"[0]scale=320x240,setsar=1[im];[1]scale=320x240,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0\" ' + '/Users/iseongmin/Downloads/test/test_Video/output_concat3.mp4'

print(tempstring)
result = subprocess.Popen([tempstring],shell=True,stdout=subprocess.PIPE)
#result = subprocess.Popen(['ffmpeg', '-i', '/Users/iseongmin/Downloads/test/test_Video/Thief_face_caught_resize.mp4', '-loop', '1', '-framerate', '25', '-t', '30', '-i', '/Users/iseongmin/Downloads/test/test_Video/001_resize.jpg', '-filter_complex', '\"[0]scale=320x240,setsar=1[im];[1]scale=320x240,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0\"' '/Users/iseongmin/Downloads/test/test_Video/output_concat3.mp4'],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#result = os.popen('ffmpeg -i /Users/iseongmin/Downloads/test/test_Video/Thief_face_caught_resize.mp4 -loop 1 -framerate 25 -t 30 -i /Users/iseongmin/Downloads/test/test_Video/001_resize.jpg -filter_complex "[0]scale=320x240,setsar=1[im];[1]scale=320x240,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0" /Users/iseongmin/Downloads/test/test_Video/output_concat3.mp4')
(out,err) = result.communicate()
print(out)
result.wait()