#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rory Hartong-Redden'
SITENAME = "Rory's Corner"

SITEURL = ''
# OUTPUT_PATH = 'output/blog'

# PAGE_URL = '../{slug}.html'
# PAGE_SAVE_AS = '../{slug}.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Home', '/'),
             ('Blog', '/archives'),
             ('About', '/pages/about'),
             ('Projects', '/pages/projects'),
             ('Contact', '/pages/contact')]

PATH = 'content'
ARTICLE_PATHS = ['blog',]
PAGE_PATHS = ['pages',]
STATIC_PATHS = ['images',]
# PAGE_ORDER_BY = 'attribute'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'


# Blogroll
LINKS = (('Keras', 'http://blog.keras.io/'),
         ('No Free Hunch (Kaggle)', 'http://blog.kaggle.com/'),
         ('EFAVDB', 'http://efavdb.com/'),
         ('Google', 'http://googleresearch.blogspot.com/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/roryhr'),
          ('LinkedIn', 'https://www.linkedin.com/in/rory-hartong-redden-18334356'),
	      ('Twitter', 'https://twitter.com/rory_h_r'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Don't bother generating an Author page - we've only got one author
AUTHOR_SAVE_AS = False


# Turn off Feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
