import subprocess
from pyutil.converter.video_converter.ffmpeg_api.ffmpeg_convert_api import encode
from pyutil.converter.video_converter.ffmpeg_api.video_configurations import VideoConfigurations

__author__ = 'R.Azh'


def convert_to_mp4(source_file_path, source_file_name, convert_config='MP4_NORMAL_RESOLUTION', output_path=None,
                   output_file_name=None,
                   remove_source_file=False):
    print('thread started -----------------------------------------------------------------------')
    output_path = source_file_path if not output_path else output_path
    if not output_file_name:
        output_file_name = ''.join(source_file_name.split('.')[:-1])
    converted_file_name = '{}.{}'.format(output_file_name, 'mp4')
    encode('{}/{}'.format(source_file_path, source_file_name), getattr(VideoConfigurations, convert_config),
           '{}/{}'.format(output_path, converted_file_name))
    if remove_source_file:
        _remove_file(source_file_path, source_file_name)
    print('thread ended ---------------------------------------------------------------------------')
    return converted_file_name


def convert_to_flv(file_path, file_name, convert_config='FLV_NORMAL_RESOLUTION', output_path=None):
    output_path = file_path if not output_path else output_path
    converted_file_name = '{}.{}'.format(''.join(file_name.split('.')[:-1]), 'flv')
    encode('{}/{}'.format(file_path, file_name), getattr(VideoConfigurations, convert_config),
           '{}/{}'.format(output_path, converted_file_name))
    return converted_file_name


def convert_to_webm(file_path, file_name, convert_config='WEBM_NORMAL_RESOLUTION', output_path=None):
    output_path = file_path if not output_path else output_path
    converted_file_name = '{}.{}'.format(''.join(file_name.split('.')[:-1]), 'webm')
    encode('{}/{}'.format(file_path, file_name), getattr(VideoConfigurations, convert_config),
           '{}/{}'.format(output_path, converted_file_name))
    return converted_file_name


def convert_to_ogg(file_path, file_name, convert_config='OGG_NORMAL_RESOLUTION', output_path=None):
    output_path = file_path if not output_path else output_path
    converted_file_name = '{}.{}'.format(''.join(file_name.split('.')[:-1]), 'ogg')
    encode('{}/{}'.format(file_path, file_name), getattr(VideoConfigurations, convert_config),
           '{}/{}'.format(output_path, converted_file_name))
    return converted_file_name


def _remove_file(file_path, file_name):
    command = ['rm', '{}/{}'.format(file_path, file_name)]
    subprocess.call(command)
