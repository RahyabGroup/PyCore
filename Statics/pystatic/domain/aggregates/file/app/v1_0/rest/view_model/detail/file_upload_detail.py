__author__ = 'root'


class FileUploadDetail:
    file_name = None
    path = None

    @staticmethod
    def create_from_file(file):
        if file:
            file_upload_detail = FileUploadDetail()
            file_upload_detail.file_name = file.persisted_file_name
            file_upload_detail.path = file.path
            return file_upload_detail
        return None