import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/SubRedditFetcher')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

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