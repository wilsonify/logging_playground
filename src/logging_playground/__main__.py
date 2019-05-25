import os
from playground import main
import logging
from logging.config import dictConfig
import config
import utils

if __name__ == '__main__':
    os.makedirs(config.LOG_DIR, exist_ok=True)
    dictConfig(config.logging_config)
    logging.debug("running {}".format(__file__))
    utils.log_paths()
    main()
