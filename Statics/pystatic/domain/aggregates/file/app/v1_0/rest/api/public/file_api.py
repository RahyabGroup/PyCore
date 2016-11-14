from flask import request
from pyfacil.web.rest.flask.response import *
from pyutil.file import file_info
from pystatic.domain.aggregates.file.app.v1_0.rest import apis
from pystatic.domain.aggregates.file.app.v1_0.rest.command.public.file_remove import FileRemove

from pystatic.domain.aggregates.file.app.v1_0.rest.command.public.file_replace import FileReplace
from pystatic.domain.aggregates.file.app.v1_0.rest.command.public.file_upload import FileUpload
from pystatic.domain.aggregates.file.app.v1_0.rest.query.public.file_download import FileDownload
from pystatic.domain.aggregates.file.app.v1_0.rest.resource import FileInfoCodes
from pystatic.main.assembler import auth


@apis.route('/files/<storage_name>/<file_name>', methods=['GET'])
def file_download(storage_name, file_name):
    dto = {"storage_name": storage_name, "file_name": file_name}
    file_download_reader = FileDownload(dto)
    result = file_download_reader.execute()
    response = make_send_file_response(result.file_content, result.file_name)
    response.headers['Content-Type'] = "file/{}".format(file_info.get_extension(result.file_name))
    return response


@apis.route('/files/<storage_name>', methods=['POST'])
@auth.login_required()
def file_upload(storage_name):
    file_key = next(iter(request.files))
    file = request.files[file_key]
    dto = {"storage_name": storage_name, "file": {"file_name": file.filename, "file_content": file.read()}}
    file_upload_command = FileUpload(dto)
    result = file_upload_command.execute()
    return created(result)


@apis.route('/files/<storage_name>/<old_file_name>', methods=['PUT'])
@auth.login_required()
def file_replace(storage_name, old_file_name):
    file_key = next(iter(request.files))
    file = request.files[file_key]
    dto = {"storage_name": storage_name, "old_file_name": old_file_name, "new_file": {"file_name": file.filename,
                                                                                      "file_content": file.read()}}
    file_replace_command = FileReplace(dto)
    file_replace_command.execute()
    return ok(FileInfoCodes.DONE)


@apis.route('/files/<storage_name>/<file_name>', methods=['DELETE'])
@auth.login_required()
def file_remove(storage_name, file_name):
    dto = {"storage_name": storage_name, "file_name": file_name}
    file_remove_command = FileRemove(dto)
    file_remove_command.execute()
    return ok(FileInfoCodes.DONE)
