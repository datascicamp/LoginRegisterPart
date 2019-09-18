import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('WEB_SERVER_SECRET_KEY') or 'abcdef020301abc8c86f'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')

    # my postgres in K8s
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    # ------------------------------ #
    # # K8s config
    POSTGRES_HOST = os.environ.get('POSTGRES_SERVICE_HOST')
    POSTGRES_PORT = os.environ.get('POSTGRES_SERVICE_PORT')
    POSTGRES_DBNAME = os.environ.get('POSTGRES_DBNAME')
    POSTGRES_USERNAME = os.environ.get('POSTGRES_USERNAME')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_PROTOCOL = os.environ.get('POSTGRES_PROTOCOL')
    POSTGRES_SSLMODE = os.environ.get('POSTGRES_SSLMODE')
    #
    # # assembled Database URI
    # SQLALCHEMY_DATABASE_URI = POSTGRES_PROTOCOL + '://' + POSTGRES_USERNAME + ':' + POSTGRES_PASSWORD + '@' +\
    #                           POSTGRES_HOST + ':' + POSTGRES_PORT + '/' + POSTGRES_DBNAME + '?sslmode=' + POSTGRES_SSLMODE
    # ------------------------------ #

    # protocol + `://` + dbUsername + `:` + dbPassword + `@` + dbIp + `:` + dbPort + `/` + dbName + `?sslmode=` +sslMode
    # config example:
    # SQLALCHEMY_DATABASE_URI = 'postgres://dbuser:docker@174.137.53.253:5432/testdb?sslmode=disable'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

