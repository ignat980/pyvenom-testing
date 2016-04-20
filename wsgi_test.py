from wsgiref.simple_server import make_server
from sample_app import application

httpd = make_server('', 8000, application)
print "Serving on port 8000..."
httpd.handle_request()
