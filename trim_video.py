import subprocess

input_file = r"C:\Users\ADMIN\Desktop\ff_input_videos\avengers.mp4"
output_file = r"C:\Users\ADMIN\Desktop\ff_out_files\trimmed_video.mp4"
start_time = '00:00:00'
end_time = '00:01:00'

# Constructing the FFmpeg command
def trim_video(in_video,stime,etime,out_file):
    ffmpeg_command = [
    'ffmpeg', '-i', in_video, '-ss', stime, '-to', etime,
    '-c', 'copy', out_file
    ]
    try: 
        subprocess.run (ffmpeg_command)
        print ("triming video completed")
    except Exception as e:
        print (e)
    
trim_video(input_file,start_time,end_time,output_file)

# Execute FFmpeg command using subprocess