from log import States,log
from tg import incoming_messages

def last_updated():
    try:
        with open('id.txt','r') as f:
            try:
                last_updated = int(f.read())
            except ValueError:
                last_updated = 0
        f.close()
    except FileNotFoundError:
            last_updated = 0
    log.debug('Last updated id: {0}'.format(last_updated))
    return last_updated


if __name__ == '__main__':
    try:
        log.debug("Starting bot service")
        States.last_updated_id = last_updated()
        while True:
            incoming_messages(States.last_updated_id)
    except KeyboardInterrupt:
        log.info('Recieved keyboard interrupt..exiting out of the bot service')
