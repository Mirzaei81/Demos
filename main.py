from telethon.sync import TelegramClient
from telethon import functions, types
import os 
api_id =os.getenv("tel_api_id")
api_hash =os.getenv("tel_api_hash")
name =os.getenv("tel_user")
with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.account.CheckUsernameRequest(
        username='some string here'
    ))
    print(result)