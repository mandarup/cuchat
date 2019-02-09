

class BaseConfig(object):
  DEBUG = False  # make sure DEBUG is off unless enabled explicitly otherwise
  LOG_DIR = '.'  # create log files in current working directory
  SESSION_COOKIE_SECURE = True # used by session, Flask-Session
  WTF_CSRF_ENABLED = True


class DefaultConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    WTF_CSRF_ENABLED = False

class TestingConfig(BaseConfig):
    pass

class StagingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass
