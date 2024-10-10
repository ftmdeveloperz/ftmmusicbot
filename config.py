import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ᴄʏʙᴇʀ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://raw.githubusercontent.com/ftmdeveloperz/ftmmusicbot/a5636bf8a45c9d4142c35e4a77a0db7d2a2024f7/file-CRA9zevdFFyBFEeu421odwb3.webp")
THUMB_IMG = getenv("THUMB_IMG", "https://raw.githubusercontent.com/ftmdeveloperz/ftmmusicbot/90beecaee1d28e2dfa31ad3dcba6a54b95597cc5/%D2%93%E1%B4%9B%E1%B4%8D%20%E1%B4%8D%E1%B4%9Cs%C9%AA%E1%B4%84%20%E1%B4%A1%E1%B4%8F%CA%80%CA%9F%E1%B4%85.png")
AUD_IMG = getenv("AUD_IMG", "https://raw.githubusercontent.com/ftmdeveloperz/ftmmusicbot/90beecaee1d28e2dfa31ad3dcba6a54b95597cc5/%D2%93%E1%B4%9B%E1%B4%8D%20%E1%B4%8D%E1%B4%9Cs%C9%AA%E1%B4%84%20%E1%B4%A1%E1%B4%8F%CA%80%CA%9F%E1%B4%85.png")
QUE_IMG = getenv("QUE_IMG", "https://raw.githubusercontent.com/ftmdeveloperz/ftmmusicbot/90beecaee1d28e2dfa31ad3dcba6a54b95597cc5/%D2%93%E1%B4%9B%E1%B4%8D%20%E1%B4%8D%E1%B4%9Cs%C9%AA%E1%B4%84%20%E1%B4%A1%E1%B4%8F%CA%80%CA%9F%E1%B4%85.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", ")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝙵𝚃𝙼 𝙼𝚄𝚂𝙸𝙲 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CyberSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CyberMusicProject")
OWNER_NAME = getenv("OWNER_NAME", "Badboyanim") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
