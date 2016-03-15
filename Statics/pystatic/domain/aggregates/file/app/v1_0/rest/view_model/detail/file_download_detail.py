__author__ = 'H.Rouhani'


class FileDownloadDetail:
    file_name = None
    file_content = None

    @staticmethod
    def create_from_file(file):
        if file:
            file_detail = FileDownloadDetail()
            file_detail.file_name = file.persisted_file_name
            file_detail.file_content = file.content
            return file_detail
        return None
