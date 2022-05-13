from masonite.request import Request
from masonite.response import Response
from masonite.routes import Route


class SwaggerDocs:
    def __init__(self, doc):
        self.doc = doc

    def __call__(self):
        return self.doc.doc_html


class SwaggerJSON:
    def __init__(self, doc):
        self.doc = doc

    def __call__(self, request: Request, response: Response):
        return response.json(self.doc.get_config(request.get_host()))


class SwaggerEditor:
    def __init__(self, doc):
        self.doc = doc

    def __call__(self):
        return self.doc.editor_html


class SwaggerResources:
    def __init__(self, doc):
        self.doc = doc

    def __call__(self, path: str, response: Response):
        return response.download(path, self.doc.static_dir + "/" + path)


def handler(doc):
    swagger_docs = SwaggerDocs(doc)
    swagger_json = SwaggerJSON(doc)
    swagger_editor = SwaggerEditor(doc)
    swagger_resources = SwaggerResources(doc)

    SWAGGER_ROUTES = [
        Route.get("/docs/", swagger_docs),
        Route.get(doc.swagger_json_uri_absolute, swagger_json),
        Route.get(doc.editor_uri_absolute(), swagger_editor),
        Route.get(f"{doc.static_uri_absolute}/@path", swagger_resources),
    ]

    doc.app.make("router").add(
        Route.group(
            SWAGGER_ROUTES,
        )
    )
