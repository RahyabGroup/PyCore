from pystatic.domain.aggregates.file.model.file import File

__author__ = 'H.Rouhani'


class FileRemove:
    storage_name = None
    path = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        file = File(self.storage_name)
        file.path = self.path
        file.remove_by_path()
