import sys
sys.path.insert(0, '/var/www/ipn.ir/web/IPN-Core')
sys.path.insert(0, '/var/www/ipn.ir/web/IPN-App/IPN')
import os
from flask.ext.cors import CORS

from atistancube.ipn.app import create_app

author = 'Hooman'

app = create_app(os.getenv('IPN_CONFIG') or 'ipndefault')
from atistancube.ipn.app.config import config
from atistancube.ipn.app.api_1_0 import prepare_db
prepare_db()
CORS(app)

#if __name__ == '__main__':
#    from atistancube.ipn.app.config import config
#    from atistancube.ipn.app.api_1_0 import prepare_db
#    prepare_db()
#    CORS(app)
#    app.run(host=config().HOST, port=config().PORT, threaded=True)
application = app
