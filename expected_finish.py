from test_wsgi import *

test_wsgi.do_request('/login').body({
    'email': 'test@example.com',
    'password': 'p@assword'
}).query().headers({}) == {'success': True}
