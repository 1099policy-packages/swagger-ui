from core import ApplicationDocument
from masonite import handler


class SwaggerUI:
    def __init__(self, app, **kwargs):
        return handler(ApplicationDocument(app, **kwargs))
