#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Jolene Smith'
SITENAME = 'SAA 2018 Government Digital Data'
SITEDESCRIPTION = 'The home on the web for the 2018 SAA Electronic Symposium'
SITEURL = 'http://127.0.0.1:8000/'

# plugins
PLUGIN_PATHS = ['/home/jolene/pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = '../pelican-fh5co-marble'
I18N_GETTEXT_LOCALEDIR = '../pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/en']
ARTICLE_PATHS = ['blog/en']

# # i18n
# I18N_SUBSITES = {
#   'de': {
#     'PAGE_PATHS': ['pages/de'],
#     'ARTICLE_PATHS': ['blog/de'],
#     'LOCALE': 'de_DE'
#   }
# }

# logo path, needs to be stored in PATH Setting
LOGO = '/SAA2018digigovt/images/saalogo.png'

# special content
HERO = [
  {
    'image': '/SAA2018digigovt/images/hero/lidar.jpg',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'Futures and Challenges in Government Digital Archaeology',
      # 'de': 'Spezieller Inhalt'
    },
    'text': {
      'en': 'An Electronic Symposium sponsored by SAA Digital Data Interest Group',
      # 'de': 'Jeglicher spezieller Inhalt den Sie hier bewerben möchten'
    },
    'links': [
      {
        'icon': 'icon-code',
        'url': 'https://docs.google.com/forms/d/e/1FAIpQLSfmrRBWsDE6hP2Vee-P-DVMKjeG5p0Yrj2uF_pqPJpL5QAmHg/viewform?usp=sf_link',
        'text': 'Contribute'
      }
    ]
  }, {
    'image': '/SAA2018digigovt/images/hero/saa_ddig.jpg',
    # keep it a string if you dont need multiple languages
    'title': 'Take the survey!',
    # keep it a string if you dont need multiple languages
    'text': 'Do you do things with archaeology data or technology in government?',
    'links': [
          {
            'icon': 'icon-code',
            'url': 'https://docs.google.com/forms/d/e/1FAIpQLSd8oZQGOuwKOIJhtgVOlfecaELW2m6SEy_oiLANQbpNSybXpA/viewform?usp=sf_link',
            'text': 'Survey'
          }
    ]
  }
  , {
    'image': '/SAA2018digigovt/images/hero/8459349522_213829baff_k.jpg',
    'title': 'Watch this space for presentations and discussion.',
    'text': '#SAA2018 #SAAdigigovt',
    'links': []
  }, {
    'image': '/SAA2018digigovt/images/hero/20332788199_8778a908dd_h_mod.jpg',
    'title': 'See abstracts, papers, and other posts.',
    'text': "We'll be adding presenations and links until the conference",
    'links': [
              {
                'icon': 'icon-code',
                'url': 'archives.html',
                'text': 'Read More'
              }
    ]
  }
]

# Social widget
# SOCIAL = (
#   ('Github', 'https://www.github.com/claudio-walser'),
#   ('Facebook', 'https://www.facebook.com'),
#   ('Twitter', 'https://www.twitter.com'),
#   ('Google+', 'https://plus.google.com')
# )

ABOUT = {
  # 'image': '/images/about/about.jpeg',
  'mail': 'jolene.smith@dhr.virginia.gov',
  # keep it a string if you dont need multiple languages
  'text': 'contact the organizer',
  # 'link': 'contact.html',
  # the address is also taken for google maps
  # 'address': 'Zürich, Schweiz',
  # 'phone': '+555-shoe'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Abstracts, Presentations, & Contributions', 'archives.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  # 'contact' # needed for the contact form
]

# # setup disqus
# DISQUS_SHORTNAME = 'saadigigovt'
# DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# # setup google maps
# GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'
