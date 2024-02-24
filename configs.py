import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "25269253"))
  API_HASH = os.environ.get("API_HASH", "a4f351103f9cb0eb6cfed99770f648ad")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6704331949:AAGpmMmvuXYsBijwSyGaNsrVa2F_1iu5J3M")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "filex_store_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002065381146"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5960791094"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://lillu:<password>@cluster0.j1pxf2k.mongodb.net/")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "0")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent File Store Bot!
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add/save Uploaded File in Channel and Share a Shareable Link. 

⍟──────[ File Store Bot]──────⍟

🔸 My Name: [File Store Bot](https://t.me/{BOT_USERNAME})

🔸 Language: [Python 3](https://www.python.org)

🔸 Library: [Pyrogram](https://docs.pyrogram.org)

"""
  ABOUT_DEV_TEXT = f"""
Developer: @kxzen_x

"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **File Store Bot**

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link(s).

⚠️ Benefits: If you have a Telegram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File(s) & I will Send Permanent Link(s) to You & Channel will be Safe from **Copygight Infringement Issues**. Checkout **About Bot** Section For More Details.
"""
