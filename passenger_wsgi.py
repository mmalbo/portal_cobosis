import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

INTERP = "/virtualenv/portal_cobosis/3.11/bin/python3.11"

environ = os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_cobosis.settings')

from portal_cobosis.wsgi import app
application = app

#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/plain')])
#    message = 'It works!\n'
#    version = 'Python %s\n' % sys.version.split()[0]
#    response = '\n'.join([message, version])
#    return [response.encode()]
