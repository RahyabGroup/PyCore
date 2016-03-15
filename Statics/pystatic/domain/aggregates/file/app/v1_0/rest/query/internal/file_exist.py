from pystatic.domain.aggregates.file.model.file import File

__author__ = 'H.Rouhani'


class FileExist:
    storage_name = None
    path = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        return File.path_exist(self.storage_name, self.path)
