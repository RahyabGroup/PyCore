from pyutil.converter.video_converter.ffmpeg_api.ffmpeg_convert import encode

__author__ = 'root'


def convert_to_mp4(file_path, file_name, output_path=None):
    # mp4_configs = ['-c:v', 'libx264', '-preset', 'fast', '-profile:v', 'high']
    output_path = file_path if not output_path else output_path
    mp4_configs = ['-qscale', '4', '-vcodec', 'libx264', '-f', 'mp4']
    converted_file_name = '{}.{}'.format(''.join(file_name.split('.')[:-1]), 'mp4')
    encode('{}/{}'.format(file_path, file_name), mp4_configs,
           '{}/{}'.format(output_path, converted_file_name))
    return converted_file_name


def convert_to_flv(file_path, file_name, output_path=None):
    output_path = file_path if not output_path else output_path
    flv_configs = ['-c:v', 'libx264', '-ar', '22050', '-crf', '28']
    converted_file_name = '{}.{}'.format(''.join(file_name.split('.')[:-1]), 'flv')
    encode('{}/{}'.format(file_path, file_name), flv_configs,
                                 '{}/{}'.format(output_path, converted_file_name))
    return converted_file_name


def convert_to_webm(file_path, file_name, output_path=None):
    output_path = file_path if not output_path else output_path
    webm_configs = ['-b', '1500k', '-vcodec', 'libvpx', '-acodec', 'libvorbis', '-ab', '160000', '-f', 'webm', '-g', '30']
    converted_file_name = '{}.{}'.format(''.join(file_name.split('.')[:-1]), 'webm')
    encode('{}/{}'.format(file_path, file_name), webm_configs,
                                 '{}/{}'.format(output_path, converted_file_name))
    return converted_file_name


def convert_to_ogg(file_path, file_name, output_path=None):
    output_path = file_path if not output_path else output_path
    ogg_configs = ['-acodec', 'libvorbis']
    converted_file_name = '{}.{}'.format(''.join(file_name.split('.')[:-1]), 'ogg')
    encode('{}/{}'.format(file_path, file_name), ogg_configs,
                                 '{}/{}'.format(output_path, converted_file_name))
    return converted_file_name
