import os
import sys

SERVER = {
    'HOST': '192.168.55.101',
    'PORT': 6667,
}

LOG_LEVEL = 'DEBUG'

DEFAULT_NICK = 'helga'
CHANNELS = ('#bots',)

AUTO_RECONNECT = True
RATE_LIMIT = None

OPERATORS = ('sduncan',)

MONGODB = {
    'HOST': 'localhost',
    'PORT': 27017,
    'DB': 'helga',
}


# Modules and their settings
EXTENSIONS = (
    'helga.extensions.operator',
    'helga.extensions.reviewboard',
    'helga.extensions.jira',
    'helga.extensions.facts',
    'helga.extensions.haiku',
    'helga.extensions.tanka',
    'helga.extensions.loljava',
    'helga.extensions.oneliner',
    'helga.extensions.stfu',
    'helga.extensions.dubstep',
    'helga.extensions.icanhazascii',
)

JIRA_URL = 'https://jira.cmgdigital.com/browse/%(ticket)s'
REVIEWBOARD_URL = 'http://reviews.ddtc.cmgdigital.com/r/%(review)s'

ALLOW_NICK_CHANGE = False


if 'HELGA_SETTINGS' in os.environ:
    try:
        overrides = __import__(os.environ['HELGA_SETTINGS'])
    except ImportError:
        pass
    else:
        this = sys.modules[__name__]
        for attr in filter(lambda x: not x.startswith('_'), dir(overrides)):
            setattr(this, attr, getattr(overrides, attr))
