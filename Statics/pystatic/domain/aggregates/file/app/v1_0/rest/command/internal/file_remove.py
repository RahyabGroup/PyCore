from pystatic.domain.aggregates.file.model.file import File

__author__ = 'H.Rouhani'


class FileRemove:
    storage_name = None
    file_name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        file = File(self.storage_name)
        file.persisted_file_name = self.file_name
        file.remove_by_path()
