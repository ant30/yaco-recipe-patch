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

.. Note to recipe author!
   ----------------------
   zc.buildout provides a nice testing environment which makes it
   relatively easy to write doctests that both demonstrate the use of
   the recipe and test it.
   You can find examples of recipe doctests from the PyPI, e.g.
   
     http://pypi.python.org/pypi/zc.recipe.egg

   The PyPI page for zc.buildout contains documentation about the test
   environment.

     http://pypi.python.org/pypi/zc.buildout#testing-support

   Below is a skeleton doctest that you can start with when building
   your own tests.

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


