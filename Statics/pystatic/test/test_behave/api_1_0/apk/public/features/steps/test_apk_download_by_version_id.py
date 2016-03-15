import requests
from behave import *

from pystatic.test.test_behave.resources.url_addresses import Url


@when("we download the apk file by version id - apk_download")
def step_impl(context):
    apk_dict = {"version_id": context.version_id}
    result = requests.get(Url.DOMAIN_ADDRESS + Url.APK_DOWNLOAD_BY_VERSION_ID_ROUTE.format(context.storage_name), json=apk_dict)
    print(result)
    context.result = result
