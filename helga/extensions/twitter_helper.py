""" helga.extensions.twitter_helper

    abstract class for getting helga to deliver quotes from
    twitter users. see helga.extensions.noir for a concrete
    example of how this is used.

"""
import random
from twisted.internet import reactor
from helga.extensions.base import CommandExtension
from helga.log import setup_logger
from helga.util.twitter import get_settings, get_api

logger = setup_logger(__name__)

class TwitterHelper(CommandExtension):
    _cached_tweets = []
    default_count = 200

    def populate_cache(self):
        logger.info('downloading some tweets for: ' + self.twitter_user)
        api = get_api(get_settings())
        source1 = api.get_user(self.twitter_user)
        timeline = source1.timeline(exclude_replies=True,
                                    include_rts=False,
                                    trim_user=True,
                                    count=self.default_count)
        self._cached_tweets = [ status.text for status in timeline ]
        logger.info('finished downloading.')

    @property
    def next_message(self):
        if self._cached_tweets:
            logger.info('returning random tweet from cache (len={0})'.format(
                len(self._cached_tweets)))
            return random.choice(self._cached_tweets)
        else:
            logger.info('populating cache')
            reactor.callInThread(lambda: self.populate_cache())
            return self.default_message

    def handle_message(self, opts, message):
        message.response = self.next_message
