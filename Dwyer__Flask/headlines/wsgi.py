# WSGI file for apache2 server

activate_this = '/var/www/headlines/virtualenv_headlines/bin/activate_this.py'

with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/headlines/')
from headlines import app as application
