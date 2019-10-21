import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRECT_KEY = os.environ.get('SECRECT_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMINT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX
