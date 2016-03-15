from pyfacil.reposiotry.mongo.repository import Repository
from pyclaim.main.config import Config

__author__ = 'Hooman'


class ClaimTypeWriter(Repository):
    def __init__(self):
        cfg = Config()
        super(ClaimTypeWriter, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "claim_type")
