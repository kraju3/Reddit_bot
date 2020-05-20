import logging


class States(object):
    last_updated_id = ''

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(asctime)s - %(funcName)s - %(message)s',filename='log.txt')

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(funcName)s - %(message)s',filename ='debug.txt')
log = logging.getLogger('nbt')