# Configuration classes for Flask App

class Config(object):
   DEBUG = False
   TESTING = False

   SESSION_COOKIE_SECURE = True

   # Debug and Testing is set to False

class ProductionConfig(Config):
   pass

class DevelopmentConfig(Config):
   DEBUG = True

   SESSION_COOKIE_SECURE = False

   # You can configure various DataBases for various stages, testing, deployment, testing, etc.

class TestingConfig(Config):
   TESTING = True

   SESSION_COOKIE_SECURE = False

