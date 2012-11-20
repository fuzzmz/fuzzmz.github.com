#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = ''

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
#RELATIVE_URLS = False

DISQUS_SITENAME = "qwertyfuzz"
GOOGLE_ANALYTICS = "UA-28459915-1"

MD_EXTENSIONS = ['codehilite', 'extra']
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
STATIC_PATHS = ['images', 'js']
