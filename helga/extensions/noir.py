""" helga.extensions.noir """

from helga.extensions.twitter_helper import TwitterHelper

class NoirExtension(TwitterHelper):
    """ command that delivers quotations from @chandlerisms """
    NAME = 'noir'
    usage = '[BOTNICK] noir'
    twitter_user = 'chandlerisms'
    _cached_tweets = []
    default_message = ("It was raining in the city by the bay. A hard rain."
                       " Hard enough to wash the slime out of the streets "
                       "and back into the holes they crawled out of...")
