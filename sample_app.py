import cgi


def application(environ, start_response):
    # Note that an application is usually not a pure WSGI
    # application, might be some framework or environment.
    # But as an example...
    # setup_testing_defaults(environ)
    start_response('200 OK', [('Content-type', 'text/html')])
    greeting = 'Hello world'
    content = [
        '<html><head><title>%s</title></head>\n' % greeting,
        '<body><h1>%s!</h1>\n' % greeting,
        '<table border=1>\n',
    ]
    items = environ.items()
    items.sort()
    for key, value in items:
        content.append('<tr><td>{}</td><td>{}</td></tr>\n'
                       .format(key, cgi.escape(repr(value))))
    content.append('</table></body></html>')
    return content
