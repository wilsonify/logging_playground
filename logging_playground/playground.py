import os
import logging
from logging.config import dictConfig
import config

logging.debug('A debug message')
logging.info('Some information')
logging.warning('A shot across the bows')


def main():
    logging.info("main")
    logging.debug("__name__=={}".format(__name__))


if __name__ == '__main__':
    os.makedirs(config.LOG_DIR, exist_ok=True)
    dictConfig(config.logging_config)
    logger = logging.getLogger()
    main()
