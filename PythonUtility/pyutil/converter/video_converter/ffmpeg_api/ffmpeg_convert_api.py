import subprocess
__author__ = 'R.Azh'

# FFMPEG_PATH = 'ffmpeg'
FFMPEG_PATH = '/bin/ffmpeg'


def encode(file, video_configs, output_file):
    command = [FFMPEG_PATH, '-i', file]
    command += video_configs
    command += ['-threads', '8', output_file]    # add threads and output
    subprocess.call(command)    # encode the video!




