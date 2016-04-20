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

if __name__ == '__main__':
    main()
