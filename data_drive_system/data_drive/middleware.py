import logging

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logging.info(f"Request {request.method}: {request.path}")
        response = self.get_response(request)
        return response
