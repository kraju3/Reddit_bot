from os import environ

NO_SOURCE_ERR ='No sources.Set a Source using /source'
skip_list = []
sources_dict = {}


bot_key = environ.get('NBT_ACCESS_TOKEN')
reddit_client_id = environ.get('REDDIT_ID');
reddit_client_secret = environ.get('REDDIT_SECRET')
API = 'https://api.telegram.org/bot'
update_time = 6
false_response = {"ok":False}