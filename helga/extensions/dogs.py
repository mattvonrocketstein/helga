""" helga.extensions.dogs """

from helga.extensions.base import ContextualExtension
from helga.extensions.twitter_helper import TwitterHelper

class DogsExtension(TwitterHelper):
    """ command that delivers quotations from @dogsdoingthings """
    NAME = 'dogs'
    usage = '[BOTNICK] dogs'
    twitter_user = 'dogsdoingthings'
    _cached_tweets = []
    default_message = ('Dogs bursting into a classroom with a bag full '
                       'of failed adult relationships and declaring, '
                       '"I HAVE BROUGHT ENOUGH FOR THE ENTIRE CLASS."')

class PuppiesExtension(ContextualExtension):
    """ invoke the DogsExtension any time anyone says 'puppies' keyword """
    NAME = 'puppies'
    context = r'puppies'
    allow_many = False
    response_fmt = '%(response)s'

    def transform_match(self, match):
        command_exts = self.bot.extensions.extensions['commands']
        dogs = [x for x in command_exts if x.__class__==DogsExtension]
        dogs = dogs[0] if dogs else None
        return dogs.next_message if dogs else ''
