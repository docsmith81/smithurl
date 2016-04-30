import string
import random

def shorten_url():
    random_chars = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(6))
    short_url = "http://smithbot.com/{}".format(random_chars)
    return short_url