import sys

sys.path.insert(0, '/var/www/ipn.ir/web/IPN-Core')
sys.path.insert(0, '/var/www/ipn.ir/web/IPN-App/IPN')

import os
from flask_cors import CORS
os.environ["STATICS_CONFIG"] = "pystaticsprodcfg"

from pystatic.app import create_app

author = 'Hooman'
app = create_app(os.getenv('STATICS_CONFIG') or 'pystaticsprodcfg')
from pystatic.app.config import config
CORS(app)
application = app
