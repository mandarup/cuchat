

class BaseConfig(object):
  DEBUG = False  # make sure DEBUG is off unless enabled explicitly otherwise
  LOG_DIR = '.'  # create log files in current working directory
  SESSION_COOKIE_SECURE = True # used by session, Flask-Session


class Default(BaseConfig):
    pass

class Development(BaseConfig):
    DEBUG = True

class Production(BaseConfig):
    pass
