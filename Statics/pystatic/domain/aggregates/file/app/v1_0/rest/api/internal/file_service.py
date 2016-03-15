from pyfacil.web.rest.flask.response import *
from pystatic.domain.aggregates.file.app.v1_0.rest import apis
from pystatic.domain.aggregates.file.app.v1_0.rest.command.internal.file_remove import FileRemove
from pystatic.domain.aggregates.file.app.v1_0.rest.query.internal.file_exist import FileExist
from pystatic.domain.aggregates.file.app.v1_0.rest.resource import FileInfoCodes

__author__ = 'H.Rouhani'


@apis.route('/internal/files/<storage_name>/<path>', methods=['GET'])
def file_path_exist(storage_name, path):
    dto = {"storage_name": storage_name, "path": path}
    file_exist_reader = FileExist(dto)
    result = file_exist_reader.execute()
    return ok(result)


@apis.route('/internal/files/<storage_name>/<path>', methods=['DELETE'])
def file_remove(storage_name, path):
    dto = {"storage_name": storage_name, "path": path}
    file_remove_command = FileRemove(dto)
    file_remove_command.execute()
    return ok(FileInfoCodes.DONE)
