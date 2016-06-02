#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rory Hartong-Redden'
SITENAME = "Rory's Corner"
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']  # Path to static image files
DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = 'America/Tijuana'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Keras', 'http://blog.keras.io/'),
         ('Kaggle', 'http://blog.kaggle.com/'),
         ('EFAVDB', 'http://efavdb.com/'),
         ('Google', 'http://googleresearch.blogspot.com/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/roryhr'),
          ('LinkedIn', 'https://www.linkedin.com/in/rory-hartong-redden-18334356'),
	  ('Twitter', 'https://twitter.com/rory_h_r'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

