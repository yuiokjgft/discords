import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1278650999:AAEO4dwX3jfDLuAY7IAcbsqk6yadcvASe8k"
    DATABASE_URL = "postgres://dpouxldvifrhhy:dcc4c46b2b6d7f007543635ce9397fac09e2a743fca197ffefe758b5ee65112f@ec2-18-210-180-94.compute-1.amazonaws.com:5432/dflhhs41isfjpq"
    APP_ID = "1948374"
    API_HASH = "113be69e13bf6f71583fb0783b1ab841"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**rusak**"
      ]

      START_MSG = "**p [{}](tg://user?id={})**\n__rusak"
