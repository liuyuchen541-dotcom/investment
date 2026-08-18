from . import config, db


def list_holdings(db_path=None):
    return db.fetch_holdings(db_path or config.DATA_DIR)
