import os
import logging

logging.debug("config")

LOG_DIR = 'logs'

simple_format = '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'

detailed_format = "%(asctime)s  \
%(created)f \
%(filename)s    \
%(funcName)s    \
%(levelname)s   \
%(levelno)s \
%(lineno)d  \
%(module)s  \
%(msecs)d   \
%(name)s    \
%(pathname)s    \
%(process)d \
%(processName)s \
%(relativeCreated)d \
%(threadName)s  \
%(thread)s  \
%(message)s\
"

logging_config = {
    'version': 1,
    'formatters': {
        'simple': {
            'class': 'logging.Formatter',
            'format': simple_format
        },
        'detailed': {
            'class': 'logging.Formatter',
            'format': detailed_format
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
        },
        'debug_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'mode': 'w',
            'formatter': 'detailed',
            'level': 'DEBUG'
        },
        'info_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'info.log'),
            'mode': 'w',
            'formatter': 'detailed',
            'level': 'INFO'
        },
        'warn_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'warning.log'),
            'mode': 'w',
            'formatter': 'detailed',
            'level': 'WARNING'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'errors.log'),
            'mode': 'w',
            'level': 'ERROR',
            'formatter': 'detailed',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', "debug_file", "info_file", "warn_file", "error_file"]
    },
}
