import subprocess
__author__ = 'root'

FFMPEG_PATH = 'ffmpeg'


def encode(file, video_configs, output_file):
    command = [FFMPEG_PATH, '-i', file]
    command.append(video_configs)
    command += ['-threads', '8', output_file]    # add threads and output
    subprocess.call(command)    # encode the video!




