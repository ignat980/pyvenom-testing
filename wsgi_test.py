import os
import sys

sdk_path = '/usr/local/google_appengine/'
if os.path.exists(os.path.join(sdk_path, 'platform/google_appengine')):
    sys.path.insert(0, os.path.join(sdk_path, 'platform/google_appengine'))
else:
    sys.path.insert(0, sdk_path)
import dev_appserver
dev_appserver.fix_sys_path()

try:
    import appengine_config
    (appengine_config)
except ImportError:
    print "Note: unable to import appengine_config."

from webtest import TestApp
# from app import app as application  # venom app
from sample_app import application
app = TestApp(application)

resp = app.get('/api/v2/helloworld')

print(resp)
print(resp.request)
print '{'
for k, v in resp.request.environ.items():
    print '    \'{}\': {}'.format(k, v)
print '}'
