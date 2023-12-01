import subprocess

# Replace hardcoded file paths with user-defined inputs
input_file = r"C:\Users\ADMIN\Desktop\ff_input_videos\avengers.mp4"
output_file =r"C:\Users\ADMIN\Desktop\ff_out_files\avengers_audio.mp3"

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


audio_extraction(input_file, output_file)