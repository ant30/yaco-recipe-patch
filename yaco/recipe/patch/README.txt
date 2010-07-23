.. contents::


Supported options
=================

The recipe supports the following options:

patch
    Path to patch

patchlocation
    Location to apply patch

binary-patch
    Location of patch binary. Use patch in $PATH by default if any is specified.


Example usage
=============

We'll start by creating a buildout that uses the recipe::

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... parts = testpatch
    ...
    ... [testpatch]
    ... recipe = yaco.recipe.patch
    ... patch = %(patch)s
    ... patchlocation = %(patchlocation)s
    ... """ % { 'patch' : 'patch/example-test.patch', 'example/' : 'value2'})

Running the buildout gives us::

    >>> print 'start', system(buildout) 
    Installing testpatch.


