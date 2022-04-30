# -*- coding: utf-8 -*-
"""
An evented server framework designed for building scalable
and introspectable services. Built at PayPal, based on gevent.

Copyright 2015, Mahmoud Hashemi, Kurt Rose, Mark Williams, and Chris Lane.
BSD-licensed, see LICENSE for more details.

"""

import sys
from setuptools import setup, find_packages


__author__ = 'Mahmoud Hashemi, Kurt Rose, Mark Williams, and Chris Lane'
__version__ = '0.0.2dev'
__contact__ = 'mahmoud@paypal.com'
__url__ = 'https://github.com/paypal/support'
__license__ = 'BSD'

desc = ('An evented server framework designed for building scalable'
        ' and introspectable services. Built at PayPal, based on gevent.')

if sys.version_info[:2] != (2, 7):
    raise NotImplementedError("Sorry, SuPPort only supports Python 2.7")


if __name__ == '__main__':
    setup(name='support',
          version=__version__,
          description=desc,
          long_description=__doc__,
          author=__author__,
          author_email=__contact__,
          url=__url__,
          packages=find_packages(),
          include_package_data=True,
          zip_safe=False,
          install_requires=['boltons==16.5.0',
                            'clastic==0.4.3',
                            'faststat==0.3.1',
                            'gevent==1.1.2',
                            'greenlet==0.4.10',
                            'hyperloglog==0.0.9',
                            'lithoxyl==0.3.0',
                            'psutil==5.6.6',
                            'pyjks==0.5.0',
                            'pyOpenSSL==0.14',
                            'pytest==2.6.4',
                            'sampro==0.1',
                            'ufork==0.0.1'],
          license=__license__,
          platforms='any',
          classifiers=['Development Status :: 4 - Beta',
                       'Intended Audience :: Developers',
                       'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
                       'Topic :: Internet :: WWW/HTTP :: WSGI',
                       'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                       'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
                       'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
                       'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
                       'Topic :: Software Development :: Libraries :: Application Frameworks',
                       'Programming Language :: Python :: 2.7',
                       'Programming Language :: Python :: Implementation :: CPython',
                       'License :: OSI Approved :: BSD License'])
