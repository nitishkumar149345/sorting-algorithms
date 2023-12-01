import subprocess

input_file = r"C:\Users\ADMIN\Desktop\ff_input_videos\avengers.mp4"
output_file =r"C:\Users\ADMIN\Desktop\ff_out_files\frames_%d.png"
frame_number = int (input())


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

extract_specific_frame(input_file, output_file, frame_number)

