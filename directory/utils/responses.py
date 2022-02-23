from flask import Response


class DefaultResponse(Response):
    charset = 'utf-8'
    default_status = 200
    default_mimetype = 'application/json'

    def __init__(self, response=None, status=None, headers=None,
                 mimetype=None, content_type=None, direct_passthrough=False):
        pass

    @classmethod
    def force_type(cls, response, environ=None):
        pass

