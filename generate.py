from wsgiref.handlers import BaseCGIHandler
from wsgiref.util import setup_testing_defaults
import sys
import os
from sample_app import application


def main():
    environ = dict(os.environ.items())
    setup_testing_defaults(environ)
    for arg in sys.argv[1:]:
        i = arg.find('=')
        if i != -1:
            environ[arg[0:i].upper()] = arg[i + 1:]
    handler = BaseCGIHandler(sys.stdin, sys.stdout, sys.stderr, environ, multithread=True, multiprocess=False)
    handler.run(application)


def make_environ(path='/', port='8000', method='GET', remote_host='', remote_addr='127.0.0.1',
                 headers={}):
    defualt_headers = {
        'content-type': 'text/plain',
        'content-length': '',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch',
        'accept-language': 'en-US,en;q=0.8,ru;q=0.6',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 PyVenom/1.0 (Macintosh; OS X/10.10.5) PyVenomTestKit'
    }
    for h in headers:
        defualt_headers[h] = headers[h]
    env = dict(os.environ.items())
    setup_testing_defaults(env)
    server_version = "WSGIServer/0.1"
    import socket
    env['SERVER_NAME'] = socket.getfqdn()
    env['SERVER_PORT'] = port
    env['SERVER_PROTOCOL'] = 'HTTP/1.1'
    env['GATEWAY_INTERFACE'] = 'CGI/1.1'
    env['SERVER_SOFTWARE'] = server_version + ' Python/' + '.'.join(map(str, sys.version_info[:3]))
    env['CONTENT_LENGTH'] = ''
    env['SCRIPT_NAME'] = ''
    env['REQUEST_METHOD'] = method.upper()
    if '?' in path:
        path, query = path.split('?', 1)
    else:
        path, query = path, ''
    import urllib
    env['PATH_INFO'] = urllib.unquote(path)
    env['QUERY_STRING'] = query
    env['REMOTE_HOST'] = remote_host
    env['REMOTE_ADDR'] = remote_addr
    env['CONTENT_TYPE'] = defualt_headers['content-type']
    env['CONTENT_LENGTH'] = defualt_headers['content-length']

    for k, v in defualt_headers.items():
        k = k.replace('-', '_').upper()
        v = v.strip()
        if k in env:
            continue  # skip content length, type,etc.
        if 'HTTP_' + k in env:
            env['HTTP_' + k] += ',' + v  # comma-separate multiple headers
        else:
            env['HTTP_' + k] = v
    env['HTTP_HOST'] = env['SERVER_NAME'] + env['SERVER_PORT']
    return env

if __name__ == '__main__':
    # main()
    print(make_environ())
    make_environ(path='/', port='8000', method='GET', remote_host='', remote_addr='127.0.0.1', headers={})
