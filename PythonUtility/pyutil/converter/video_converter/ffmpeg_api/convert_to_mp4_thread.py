import threading
import subprocess
from pyutil.converter.video_converter.ffmpeg_api.video_converter import convert_to_mp4

__author__ = 'root'


class ConvertToMp4Thread(threading.Thread):
    source_file_path = None
    source_file_name = None
    output_file_path = None
    output_file_name = None
    remove_source_file = None

    def __init__(self, source_file_path, source_file_name, output_file_path=None, output_file_name=None,
        remove_source_file=False):
        threading.Thread.__init__(self)
        self.source_file_path = source_file_path
        self.source_file_name = source_file_name
        self.output_file_path = output_file_path
        self.output_file_name = output_file_name
        self.remove_source_file = remove_source_file

    def run(self):
        convert_to_mp4(self.source_file_path, self.source_file_name, self.output_file_path, self.output_file_name)
        if self.remove_source_file:
            command = ['rm', '{}/{}'.format(self.source_file_path, self.source_file_name)]
            subprocess.call(command)