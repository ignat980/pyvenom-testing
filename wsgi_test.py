from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

HELLO_WORLD = b"Hello world!\n"


def simplest_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [HELLO_WORLD]


class AppClass:
    """Produce the same output, but using a class

    (Note: 'AppClass' is the "application" here, so calling it
    returns an instance of 'AppClass', which is then the iterable
    return value of the "application callable" as required by
    the spec.

    If we wanted to use *instances* of 'AppClass' as application
    objects instead, we would have to implement a '__call__'
    method, which would be invoked to execute the application,
    and we would need to create an instance for use by the
    server or gateway.
    """

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield HELLO_WORLD


def simple_app(environ, start_response):
    """A relatively simple WSGI application. It's going to print out the
    environment dictionary after being updated by setup_testing_defaults"""
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)

    ret = ["{}: {}\n".format(key, value)
           for key, value in environ.iteritems()]
    return ret


httpd = make_server('', 8000, simple_app)
print "Serving on port 8000..."
httpd.handle_request()
