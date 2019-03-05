import os
import logging

logging.debug("config")

LOG_DIR = 'logs'
logging_config = {
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
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
    'loggers': {
        'foo': {
            'handlers': ["debug_file", "info_file", "warn_file", "error_file"]
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'debug_file', 'errors']
    },
}
