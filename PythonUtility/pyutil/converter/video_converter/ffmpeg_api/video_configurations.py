__author__ = 'R.Azh'


class VideoConfigurations:
    # MP4_HIGH_RESOLUTION = []
    MP4_NORMAL_RESOLUTION = ['-codec:v', 'libx264', '-profile:v', 'high', '-codec:a', 'libfdk_aac']
    # MP4_LOW_RESOLUTION = []
    # MP4_1280X720 = []
    # MP4_720X547 = []
    # MP4_320X240 = []

    # FLV_HIGH_RESOLUTION = []
    FLV_NORMAL_RESOLUTION = ['-c:v', 'libx264', '-ar', '22050', '-crf', '28']
    # FLV_LOW_RESOLUTION = []
    # FLV_426x240 = []

    # WEBM_HIGH_RESOLUTION = []
    WEBM_NORMAL_RESOLUTION = ['-b', '1500k', '-vcodec', 'libvpx', '-acodec', 'libvorbis', '-ab', '160000', '-f', 'webm', '-g', '30']
    # WEBM_LOW_RESOLUTION = []
    # WEBM_1920x1080 = []
    # WEBM_854x480 = []
    # WEBM_640x360 = []
    # WEBM_320X240 = []

    # OGG_HIGH_RESOLUTION = []
    OGG_NORMAL_RESOLUTION = ['-acodec', 'libvorbis']
    # OGG_LOW_RESOLUTION = []

