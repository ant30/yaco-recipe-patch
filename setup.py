# -*- coding: utf-8 -*-
"""
This module contains the tool of yaco.recipe.patch
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.3'

long_description = (
    read('README.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('yaco', 'recipe', 'patch', 'README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
   'Download\n'
    '********\n')

name='yaco.recipe.patch'
entry_point = '%s:Recipe' % name

tests_require=['zope.testing', 'zc.buildout']

setup(name=name,
      version=version,
      description="Yet, another buildout recipe for patching",
      long_description=long_description,
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        ],
      keywords='buildout patch',
      author=('Antonio Pérez-Aranda Alcaide'),
      author_email='ant30tx at gmail.com',
      url='http://github.com/ant30/yaco-recipe-patch',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['yaco', 'yaco.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'yaco.recipe.patch.tests.test_docs.test_suite',
      entry_points = {"zc.buildout": ["default = %s" % entry_point],
                    "zc.buildout.uninstall": ["default = %s:uninstall_recipe" % name],
                    },
      )
