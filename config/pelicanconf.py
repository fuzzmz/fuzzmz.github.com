#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Serban Constantin'
SITENAME = u'QWERTY - fast keystrokes'
SITEURL = 'http://fuzz.me.uk'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = u'en'


DEFAULT_PAGINATION = 5

# old stuff
FEED_ALL_ATOM = ('qwertyfuzz/main')
DEFAULT_CATEGORY = ('rand')
MARKUP = ('rst', 'md')
CATEGORY_FEED_ATOM = 'qwertyfuzz/%s'
TWITTER_USERNAME = 'fuzzmz'
DISQUS_SITENAME = "qwertyfuzz"
FEED_DOMAIN = 'http://feeds.feedburner.com'
GOOGLE_ANALYTICS = "UA-28459915-1"
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'