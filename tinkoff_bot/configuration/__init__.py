import os

try:
    from .local_config import LocalConfig
except ModuleNotFoundError as e:
    from .sample_local_config import LocalConfig


class Config(object):
    def __init__(self):
        config = LocalConfig()

        self.TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', config.TELEGRAM_TOKEN)

        self.POSTGRES_DB = os.environ.get('POSTGRES_DB', config.POSTGRES_DB)
        self.POSTGRES_USER = os.environ.get('POSTGRES_USER', config.POSTGRES_USER)
        self.POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', config.POSTGRES_PASSWORD)
        self.POSTGRES_HOST = os.environ.get('POSTGRES_HOST', config.POSTGRES_HOST)
        self.POSTGRES_PORT = os.environ.get('POSTGRES_PORT', config.POSTGRES_PORT)
