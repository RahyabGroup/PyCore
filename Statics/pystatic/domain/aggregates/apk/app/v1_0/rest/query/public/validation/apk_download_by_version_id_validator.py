from pyvalidate.validation import Validation

from pystatic.domain.aggregates.apk.model.validation.apk_version_id_not_exist import ApkVersionIdNotExist

__author__ = 'root'


class ApkDownloadByVersionIdValidator(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.storage_name, 2, 20)
        super().integer.positive(self.instance.version_id, include_zero=False)
        super().custom.register(self.instance.version_id, ApkVersionIdNotExist(self.instance.storage_name))
        super().validate()

