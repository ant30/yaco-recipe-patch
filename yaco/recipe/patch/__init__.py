# -*- coding: utf-8 -*-
"""Recipe patch"""

import logging
from subprocess import Popen, PIPE, STDOUT

import zc.buildout


logger = logging.getLogger('yaco.recipe.patch')


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

        self.binarypatch = options.get('binary-patch') or 'patch'

    def install(self):
        """Installer"""
        self.apply_patch()
        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.
        return tuple()

    def apply_patch(self):
        """
        patch -d basedirectory -N -i patch.patch
        patch --directory basedirectory --forward -input patch.patch
        """
        patchcommand = [self.binarypatch,
                            '-p0',
                            '--forward',
                            '--reject-file', '-', # Don't create reject file
                            '--directory', self.options['patchlocation'],
                            '--input', self.options['patch'],
                       ]
        logger.info(' '.join(patchcommand))
        applying = Popen(patchcommand, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        [logger.info(line) for line in applying.stdout.readlines()]
        if not (applying.returncode is None or applying.returncode == 0):
            raise zc.buildout.UserError('could not apply %s' % self.options['patch'])

    def reverse_patch(self):
        patchcommand =[self.binarypatch,
                            '-p0',
                            '--reverse',
                            '--reject-file', '-', # Don't create reject file
                            '--directory', self.options['patchlocation'],
                            '--input', self.options['patch'],
                       ]
        logger.info(' '.join(patchcommand))
        applying = Popen(patchcommand,
                         stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        [logger.info(line) for line in applying.stdout.readlines()]
        if applying.returncode != 0:
            raise zc.buildout.UserError('could not reverse patch %s' % self.options['patch'])

    def update(self):
        """Updater"""
        self.reverse_patch()
        self.apply_patch()
