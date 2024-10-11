import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
PICS = os.environ.get("PICS", "").split()
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")
RemoveBG_API = os.environ.get("RemoveBG_API", "")
IBB_API = os.environ.get("IBB_API", "")
FORCE_SUB = os.environ.get("FORCE_SUB", "")
PORT = os.environ.get('PORT', '8080')          
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""
