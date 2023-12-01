import subprocess

input_video = r"C:\Users\ADMIN\Desktop\ff_input_videos\avengers.mp4"
watermark_image = r"C:\Users\ADMIN\Desktop\ff_input_videos\water_image.png"
output_video = r"C:\Users\ADMIN\Desktop\ff_out_files\watermark_video.mp4"
opacity_level = 0.5

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

add_watermark(input_video, watermark_image, output_video, opacity_level)