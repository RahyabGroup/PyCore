__author__ = 'root'

STATUS_KEY = {400: "errors", 401: "errors", 403: "errors", 404: "errors", 405: "errors", 500: "errors", 200: "data", 201: "data"}


class ResponseReader:

    @staticmethod
    def get_body(response):
        content_json = response.json()
        return content_json[STATUS_KEY[response.status_code]]

    @staticmethod
    def get_meta(response):
        content_json = response.json()
        if 'meta' in content_json:
            return content_json["meta"]


