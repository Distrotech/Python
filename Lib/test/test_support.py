"""Supporting definitions for the Python regression test."""

import sys


class Error(Exception):
    """Base class for regression test exceptions."""

class TestFailed(Error):
    """Test failed."""

class TestSkipped(Error):
    """Test skipped.

    This can be raised to indicate that a test was deliberatly
    skipped, but not because a feature wasn't available.  For
    example, if some resource can't be used, such as the network
    appears to be unavailable, this should be raised instead of
    TestFailed.
    """

verbose = 1                             # Flag set to 0 by regrtest.py
use_large_resources = 1 # Flag set to 0 by regrtest.py

def unload(name):
    try:
        del sys.modules[name]
    except KeyError:
        pass

def forget(modname):
    unload(modname)
    import os
    for dirname in sys.path:
        try:
            os.unlink(os.path.join(dirname, modname + '.pyc'))
        except os.error:
            pass

FUZZ = 1e-6

def fcmp(x, y): # fuzzy comparison function
    if type(x) == type(0.0) or type(y) == type(0.0):
        try:
            x, y = coerce(x, y)
            fuzz = (abs(x) + abs(y)) * FUZZ
            if abs(x-y) <= fuzz:
                return 0
        except:
            pass
    elif type(x) == type(y) and type(x) in (type(()), type([])):
        for i in range(min(len(x), len(y))):
            outcome = fcmp(x[i], y[i])
            if outcome != 0:
                return outcome
        return cmp(len(x), len(y))
    return cmp(x, y)

import os
if os.name !='riscos':
    TESTFN = '@test' # Filename used for testing
else:
    TESTFN = 'test' # Filename used for testing
del os

from os import unlink

def findfile(file, here=__file__):
    import os
    if os.path.isabs(file):
        return file
    path = sys.path
    path = [os.path.dirname(here)] + path
    for dn in path:
        fn = os.path.join(dn, file)
        if os.path.exists(fn): return fn
    return file

def verify(condition, reason='test failed'):
    """Verify that condition is true. If not, raise TestFailed.

       The optional argument reason can be given to provide
       a better error text.
    """

    if not condition:
        raise TestFailed(reason)

def check_syntax(statement):
    try:
        compile(statement, '<string>', 'exec')
    except SyntaxError:
        pass
    else:
        print 'Missing SyntaxError: "%s"' % statement



#=======================================================================
# Preliminary PyUNIT integration.

import unittest


class BasicTestRunner(unittest.VerboseTextTestRunner):
    def __init__(self, stream=sys.stderr):
        unittest.VerboseTextTestRunner.__init__(self, stream, descriptions=0)

    def run(self, test):
        result = unittest._VerboseTextTestResult(self.stream, descriptions=0)
        test(result)
        return result


def run_unittest(testclass):
    """Run tests from a unittest.TestCase-derived class."""
    if verbose:
        f = sys.stdout
    else:
        import StringIO
        f = StringIO.StringIO()

    suite = unittest.makeSuite(testclass)
    result = BasicTestRunner(stream=f).run(suite)
    if result.errors or result.failures:
        raise TestFailed("errors occurred in %s.%s"
                         % (testclass.__module__, testclass.__name__))
