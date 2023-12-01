import subprocess

#trimming a video
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
    


# extarcting audio from a video
def audio_extraction(in_file, out_file):
    ff_command = [
        'ffmpeg', '-i', in_file,
        '-vn',  # Use '-vn' to extract audio only
         out_file
    ]

    try:
        subprocess.run(ff_command, check=True)
        print("Audio extraction completed")
    except Exception as e:
        print(e)

# extracting specific frame form a video
def extract_specific_frame(in_video, out_file, frame_num):
    ff_command = [
        'ffmpeg', '-i', in_video,
        '-vf', f'select=eq(n\,{frame_num})',
        '-vframes', '1', out_file
    ]
    try:
        subprocess.run(ff_command)
        print("Frame extraction completed")
    except Exception as e:
        print(e)

#adding watermark to a video

def add_watermark(in_video, watermark_image, out_video, opacity_level):
    ff_command = [
        'ffmpeg',
        '-i', in_video,
        '-i', watermark_image,
        
        '-filter_complex', f'[1:v]format=rgba,colorchannelmixer=aa={opacity_level}[watermark];[0:v][watermark]overlay=0:0',
        out_video
    ]
    try:
        subprocess.run(ff_command)
        print("Process complete. Watermark added to the video.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def extract_all_frames(in_video,frames):
    ff_command= [
        'ffmpeg',
        '-i',in_video,
        frames
    ]

    try:
        subprocess.run(ff_command,check=True)
        print ("extraction of all frames is completed")
    except Exception as e:
        print (e)