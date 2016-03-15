from flask import request
from pyfacil.web.rest.flask.response import *
from pystatic.domain.aggregates.apk.app.v1_0.rest import apis

from pystatic.domain.aggregates.apk.app.v1_0.rest.command.public.apk_upload import ApkUpload
from pystatic.domain.aggregates.apk.app.v1_0.rest.query.public.apk_download import ApkDownload
from pystatic.domain.aggregates.apk.app.v1_0.rest.query.public.apk_download_by_version_id import ApkDownloadByVersionId
from pystatic.domain.aggregates.apk.app.v1_0.rest.query.public.apk_list import ApkList
from pystatic.main.assembler import auth


@apis.route('/apks/<storage_name>/<file_name>', methods=['GET'])
def apk_download(storage_name, file_name):
    dto = {"storage_name": storage_name, "file_name": file_name}
    apk_download_reader = ApkDownload(dto)
    result = apk_download_reader.execute()
    response = make_send_file_response(result.apk_content, result.apk_name)
    response.headers['Content-Type'] = "application/vnd.android.package-archive"
    return response


@apis.route('/apks/<storage_name>/download_by_version_id', methods=['GET'])
def apk_download_by_version_id(storage_name):
    dto = request.get_json()
    dto["storage_name"] = storage_name
    apk_download_by_version_id_reader = ApkDownloadByVersionId(dto)
    result = apk_download_by_version_id_reader.execute()
    response = make_send_file_response(result.apk_content, result.apk_name)
    response.headers['Content-Type'] = "application/vnd.android.package-archive"
    return response


@apis.route('/apks/<storage_name>', methods=['GET'])
def apk_list(storage_name):
    query_string = request.args
    dto = {"storage_name": storage_name, "query_string": query_string}
    apk_list_reader = ApkList(dto)
    result = apk_list_reader.execute()
    return ok(result)


@apis.route('/apks/<storage_name>', methods=['POST'])
@auth.authorize()
def apk_upload(storage_name):
    dto = {"package_name": request.args["package_name"], "version": request.args["version"], "version_id": int(request.args["version_id"])}
    file_key = next(iter(request.files))
    file = request.files[file_key]
    dto["storage_name"] = storage_name
    dto["file"] = {"file_name": file.filename, "file_content": file.read()}
    apk_upload_command = ApkUpload(dto)
    result = apk_upload_command.execute()
    return created(result)
