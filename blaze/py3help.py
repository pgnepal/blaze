import sys
import itertools

PY3 = sys.version_info[:2] >= (3,0)

if PY3:
    def dict_iteritems(d):
        return d.items().__iter__()
    xrange = range
    _inttypes = (int,)
    _strtypes = (str,)
    unicode = str
    imap = map
    basestring = str
    import urllib.parse as urlparse
else:
    import __builtin__
    def dict_iteritems(d):
        return d.iteritems()
    xrange = __builtin__.xrange
    unicode = __builtin__.unicode
    basestring = __builtin__.basestring

    _strtypes = (str, unicode)

    _inttypes = (int, long)
    imap = itertools.imap
    import urlparse