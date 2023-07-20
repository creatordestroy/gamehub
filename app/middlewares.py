class JSONContentTypeMiddleware:
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        
        environ['CONTENT_TYPE'] = 'application/json'
        return self.app(environ, start_response)