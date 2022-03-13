import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      API_ID = int(os.environ.get("API_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      OWNER_ID = int(os.environ.get("OWNER_ID"))
      MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
