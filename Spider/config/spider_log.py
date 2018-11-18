"""
logging配置
"""
import os
import logging.config

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d]' \
                  '[task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'
simple_format = '[%(levelname)s][%(asctime)s]' \
                '[%(filename)s:%(lineno)d]%(message)s'
logfile_dir = os.path.dirname(os.path.abspath(__file__))
logfile_name = '../log/spider.log'

if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)
logfile_path = os.path.join(logfile_dir, logfile_name)

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        # print to terminal/console
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # print to log file
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': logfile_path,
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


def spider_logger():
    logging.config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger(__name__)
    return logger
