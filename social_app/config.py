class Development(object):
    DEBUG = True
    SECRET_KEY = '004f2af45d3a4e161a7dd2d17fdae47f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_my_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/my_database'


class Testing(object):
    DEBUG = True
    SECRET_KEY = '004f2af45d3a4e161a7dd2d17fdae47f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_my_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@test/my_database'


class Production(object):
    DEBUG = False
    SECRET_KEY = '004f2af45d3a4e161a7dd2d17fdae47f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod_my_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@prod/my_database'
