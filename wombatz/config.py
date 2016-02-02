class Base:
    SECRET_KEY = "not-secret"


class Local(Base):
    SERVER_NAME = "localhost"


class PyAnywhere(Base):
    SERVER_NAME = "wombatz.pythonanywhere.com"
