import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

NO_SOURCE_ERR ='No sources.Set a Source using /source'
skip_list = []
sources_dict = {}


bot_key = os.getenv('NBT_ACCESS_TOKEN')
chat_id = os.getenv('BOT_ID')
reddit_client_id = os.getenv('REDDIT_ID');
reddit_client_secret = os.getenv('REDDIT_SECRET')
API = 'https://api.telegram.org/bot'
update_time = 6
false_response = {"ok":False}

print(bot_key)
print(reddit_client_id)
print(reddit_client_secret)
