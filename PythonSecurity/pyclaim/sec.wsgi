import sys

sys.path.insert(0, '/var/www/ipn.ir/web/IPN-Core')
sys.path.insert(0, '/var/www/ipn.ir/web/IPN-App/IPN')

import os

os.environ["SECURITY_CONFIG"] = "pysecurityprodcfg"

from pyclaim.app import create_app
from flask.ext.cors import CORS

__author__ = 'Hooman'

app = create_app(os.getenv('SECURITY_CONFIG') or 'pysecuritydevcfg')


from pyclaim.app.config import config
from pyclaim.app.api_1_0 import prepare_db
prepare_db()
CORS(app)
application = app
