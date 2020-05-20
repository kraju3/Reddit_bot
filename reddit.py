import praw
from log import log
from consts import reddit_client_id,reddit_client_secret


def summary(url):
    log.info('No implementation ')
    return url


def latest_news(subs):
    log.debug('Fetching latest news from Subreddits')
    errmessage = ('Reddit client Id or secret is not set')
    if reddit_client_id is None or reddit_client_secret is None:
        return errmessage

    r = praw.Reddit(user_agent='SubReddit NewsFetcher Bot',client_id=reddit_client_id,client_secret=reddit_client_secret)
    subs = cleansubs(subs)

    log.debug("Fetching latest news from subs {0}".format(subs))
    content = r.subreddit(subs).hot(limit=5)

    contents_=''

    try:
        for post in content:
            contents_+= summary(post.title+' - '+post.url) + '\n'
    except praw.errors.Forbidden:
            log.debug('subreddit {0} is private'.format(subs))
            contents_ = "Sorry couldn't fetch; subreddit is private"
    except praw.errors.InvalidSubreddit:
            log.debug('Subreddit {} is invalid or doesn''t exist.'.format(subs))
            contents_ = "Sorry couldn't fetch; subreddit doesn't seem to exist"
    except praw.errors.NotFound :
            log.debug('Subreddit {} is invalid or doesn''t exist.'.format(subs))
            contents_= "Sorry couldn't fetch; something went wrong, please do send a report to @kraju1997"

    return contents_
def cleansubs(subs):
    log.debug("Cleaning up subs {0}".format(subs))
    return subs.strip().replace(" ","").replace(',','+')