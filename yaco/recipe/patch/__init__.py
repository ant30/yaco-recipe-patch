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
        returncode = self.run_patch_command()
        if not (returncode is None or returncode == 0):
            raise zc.buildout.UserError('could not apply %s' % self.options['patch'])

    def reverse_patch(self):
        returncode = self.run_patch_command(revert=True)
        if not (returncode is None or returncode == 0):
            raise zc.buildout.UserError('could not revert patch %s' % self.options['patch'])

    def run_patch_command(self, revert=False):
        if revert:
            cmd = '--reverse'
        else:
            cmd = '--forward'
        patchcommand =[self.binarypatch,
                            '-p0',
                            cmd,
                            '--reject-file', '-', # Don't create reject file
                            '--directory', self.options['patchlocation'],
                            '--input', self.options['patch'],
                       ]
        logger.info(' '.join(patchcommand))
        patcher = Popen(patchcommand,
                         stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        [logger.info(line.replace('\n','')) for line in patcher.stdout.readlines()]
        return patcher.returncode

    def update(self):
        """Updater"""
        pass
        # self.reverse_patch()
        # self.apply_patch()


def uninstall_recipe(name, options):
    """ Try to reverse patch on uninstall """
    recipe = Recipe(None, name, options)
    recipe.reverse_patch()
