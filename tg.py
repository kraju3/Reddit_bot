import re
from time import sleep
import requests

from log import States,log
from consts import *
from reddit import latest_news

def updates(id):
    log.debug('Checking for requests , last updated  is {0}'.format(id))
    sleep(update_time)
    body = requests.get(API+f'{bot_key}'+'/getUpdates',params={'offset':id+1})

    response = false_response

    if body.status_code != 200:
        sleep(update_time*20)
        updates(id)

    try:
       response = body.json()
    except ValueError:
        sleep(update_time*20)
        updates(id)

    log.info("Response Recieved: {}".format(response))

    return response


def send(id,text):
    log.info('Posting text {} to bot {}'.format(text,id))
    info = {'chat_id':id,'text':text}
    requests.post(API+bot_key+'/sendMessage',data=info)


def incoming_messages(id):
    body = updates(id)
    chat_text = []

    if body['ok']:
        for value in body['result']:
            try:
                chat_sender_id = value['message' or 'edited_message']['chat']['id']
            except KeyError:
                pass
            try:
                chat_content = value['message']['text']
                chat_text = chat_content.split()
            except KeyError:
                chat_content = ''
                chat_text.append(chat_content)
                log.debug('No chat was detected...moving on')
            try:
                id_ = value['message']['from']['id']
            except KeyError:
                pass

            log.info('Chat text recieved {}'.format(chat_content))

            r = re.search('(source+)(.*)',chat_content)

            if (r is not None and r.group(1)=='source'):
                if r.group(2):
                    sources_dict[id_]= r.group(2)
                    log.debug('Sources set for {0} to {1}'.format(sources_dict[id_], r.group(2)))
                    send(id_,'Sources set as {0}!'.format(r.group(2)))
                else:
                    send(id_,'Need a comma separated list of subreddits! No subreddits given no news returned')
            if chat_content == '/stop':
                log.debug('Added {0} to skip list'.format(chat_sender_id))
                skip_list.append(chat_sender_id)
                send(chat_sender_id, "Ok, we won't send you any more messages.")

            if chat_content in ('/start', '/help'):
                helptext = '''
                                Hi! This is a News Bot which fetches news from subreddits. Use "/source" to select a subreddit source.
                                Example "/source programming,games" fetches news from r/programming, r/games.
                                Use "/fetch for the bot to go ahead and fetch the news. At the moment, bot will fetch total of 5 posts from all sub reddits
                                I will have this configurable soon.
                            '''
                send(chat_sender_id, helptext)

            if chat_text[0] == '/fetch' and (id_ not in skip_list):
                send(id_, 'Hang on, fetching your news..')
                try:
                    sub_reddits = sources_dict[id_]
                except KeyError:
                    send(id_,NO_SOURCE_ERR)
                else:
                    summarized_news = latest_news(sources_dict[id_])
                    send(id_, summarized_news)
            id = value['update_id']
            with open('id.txt', 'w') as f:
                f.write(str(id))
                States.last_updated_id = id
                log.debug(
                    'Updated last_updated to {0}'.format(id))
            f.close()
