# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_host', [dirname(__file__)])
        except ImportError:
            import _host
            return _host
        if fp is not None:
            try:
                _mod = imp.load_module('_host', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _host = swig_import_helper()
    del swig_import_helper
else:
    import _host
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _host.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _host.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _host.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _host.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _host.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _host.SwigPyIterator_equal(self, x)

    def copy(self):
        return _host.SwigPyIterator_copy(self)

    def next(self):
        return _host.SwigPyIterator_next(self)

    def __next__(self):
        return _host.SwigPyIterator___next__(self)

    def previous(self):
        return _host.SwigPyIterator_previous(self)

    def advance(self, n):
        return _host.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _host.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _host.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _host.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _host.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _host.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _host.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _host.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class WarpingNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WarpingNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WarpingNode, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _host.new_WarpingNode(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_setmethods__["first"] = _host.WarpingNode_first_set
    __swig_getmethods__["first"] = _host.WarpingNode_first_get
    if _newclass:
        first = _swig_property(_host.WarpingNode_first_get, _host.WarpingNode_first_set)
    __swig_setmethods__["second"] = _host.WarpingNode_second_set
    __swig_getmethods__["second"] = _host.WarpingNode_second_get
    if _newclass:
        second = _swig_property(_host.WarpingNode_second_get, _host.WarpingNode_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _host.delete_WarpingNode
    __del__ = lambda self: None
WarpingNode_swigregister = _host.WarpingNode_swigregister
WarpingNode_swigregister(WarpingNode)

class WarpingPath(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WarpingPath, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WarpingPath, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _host.WarpingPath_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _host.WarpingPath___nonzero__(self)

    def __bool__(self):
        return _host.WarpingPath___bool__(self)

    def __len__(self):
        return _host.WarpingPath___len__(self)

    def __getslice__(self, i, j):
        return _host.WarpingPath___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _host.WarpingPath___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _host.WarpingPath___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _host.WarpingPath___delitem__(self, *args)

    def __getitem__(self, *args):
        return _host.WarpingPath___getitem__(self, *args)

    def __setitem__(self, *args):
        return _host.WarpingPath___setitem__(self, *args)

    def pop(self):
        return _host.WarpingPath_pop(self)

    def append(self, x):
        return _host.WarpingPath_append(self, x)

    def empty(self):
        return _host.WarpingPath_empty(self)

    def size(self):
        return _host.WarpingPath_size(self)

    def swap(self, v):
        return _host.WarpingPath_swap(self, v)

    def begin(self):
        return _host.WarpingPath_begin(self)

    def end(self):
        return _host.WarpingPath_end(self)

    def rbegin(self):
        return _host.WarpingPath_rbegin(self)

    def rend(self):
        return _host.WarpingPath_rend(self)

    def clear(self):
        return _host.WarpingPath_clear(self)

    def get_allocator(self):
        return _host.WarpingPath_get_allocator(self)

    def pop_back(self):
        return _host.WarpingPath_pop_back(self)

    def erase(self, *args):
        return _host.WarpingPath_erase(self, *args)

    def __init__(self, *args):
        this = _host.new_WarpingPath(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _host.WarpingPath_push_back(self, x)

    def front(self):
        return _host.WarpingPath_front(self)

    def back(self):
        return _host.WarpingPath_back(self)

    def assign(self, n, x):
        return _host.WarpingPath_assign(self, n, x)

    def resize(self, *args):
        return _host.WarpingPath_resize(self, *args)

    def insert(self, *args):
        return _host.WarpingPath_insert(self, *args)

    def reserve(self, n):
        return _host.WarpingPath_reserve(self, n)

    def capacity(self):
        return _host.WarpingPath_capacity(self)
    __swig_destroy__ = _host.delete_WarpingPath
    __del__ = lambda self: None
WarpingPath_swigregister = _host.WarpingPath_swigregister
WarpingPath_swigregister(WarpingPath)


def lockstepEuclidean1d(series0, series1):
    return _host.lockstepEuclidean1d(series0, series1)
lockstepEuclidean1d = _host.lockstepEuclidean1d

def lockstepEuclidean2d(series0, series1):
    return _host.lockstepEuclidean2d(series0, series1)
lockstepEuclidean2d = _host.lockstepEuclidean2d

def lockstepEuclidean3d(series0, series1):
    return _host.lockstepEuclidean3d(series0, series1)
lockstepEuclidean3d = _host.lockstepEuclidean3d

def lockstepEuclidean4d(series0, series1):
    return _host.lockstepEuclidean4d(series0, series1)
lockstepEuclidean4d = _host.lockstepEuclidean4d

def lockstepEuclideanNd(series0, series1, stride):
    return _host.lockstepEuclideanNd(series0, series1, stride)
lockstepEuclideanNd = _host.lockstepEuclideanNd

def lockstepEuclidean1f(series0, series1):
    return _host.lockstepEuclidean1f(series0, series1)
lockstepEuclidean1f = _host.lockstepEuclidean1f

def lockstepEuclidean2f(series0, series1):
    return _host.lockstepEuclidean2f(series0, series1)
lockstepEuclidean2f = _host.lockstepEuclidean2f

def lockstepEuclidean3f(series0, series1):
    return _host.lockstepEuclidean3f(series0, series1)
lockstepEuclidean3f = _host.lockstepEuclidean3f

def lockstepEuclidean4f(series0, series1):
    return _host.lockstepEuclidean4f(series0, series1)
lockstepEuclidean4f = _host.lockstepEuclidean4f

def lockstepEuclideanNf(series0, series1, stride):
    return _host.lockstepEuclideanNf(series0, series1, stride)
lockstepEuclideanNf = _host.lockstepEuclideanNf

def lockstepManhattan1d(series0, series1):
    return _host.lockstepManhattan1d(series0, series1)
lockstepManhattan1d = _host.lockstepManhattan1d

def lockstepManhattan2d(series0, series1):
    return _host.lockstepManhattan2d(series0, series1)
lockstepManhattan2d = _host.lockstepManhattan2d

def lockstepManhattan3d(series0, series1):
    return _host.lockstepManhattan3d(series0, series1)
lockstepManhattan3d = _host.lockstepManhattan3d

def lockstepManhattan4d(series0, series1):
    return _host.lockstepManhattan4d(series0, series1)
lockstepManhattan4d = _host.lockstepManhattan4d

def lockstepManhattanNd(series0, series1, stride):
    return _host.lockstepManhattanNd(series0, series1, stride)
lockstepManhattanNd = _host.lockstepManhattanNd

def lockstepManhattan1f(series0, series1):
    return _host.lockstepManhattan1f(series0, series1)
lockstepManhattan1f = _host.lockstepManhattan1f

def lockstepManhattan2f(series0, series1):
    return _host.lockstepManhattan2f(series0, series1)
lockstepManhattan2f = _host.lockstepManhattan2f

def lockstepManhattan3f(series0, series1):
    return _host.lockstepManhattan3f(series0, series1)
lockstepManhattan3f = _host.lockstepManhattan3f

def lockstepManhattan4f(series0, series1):
    return _host.lockstepManhattan4f(series0, series1)
lockstepManhattan4f = _host.lockstepManhattan4f

def lockstepManhattanNf(series0, series1, stride):
    return _host.lockstepManhattanNf(series0, series1, stride)
lockstepManhattanNf = _host.lockstepManhattanNf

def lockstepQuaternionf(series0, series1):
    return _host.lockstepQuaternionf(series0, series1)
lockstepQuaternionf = _host.lockstepQuaternionf

def lockstepQuaterniond(series0, series1):
    return _host.lockstepQuaterniond(series0, series1)
lockstepQuaterniond = _host.lockstepQuaterniond

def elasticEuclideanDTW1d(series0, series1):
    return _host.elasticEuclideanDTW1d(series0, series1)
elasticEuclideanDTW1d = _host.elasticEuclideanDTW1d

def elasticEuclideanCDTW1d(series0, series1, window):
    return _host.elasticEuclideanCDTW1d(series0, series1, window)
elasticEuclideanCDTW1d = _host.elasticEuclideanCDTW1d

def elasticEuclideanDTW1dBacktrace(series0, series1, wpath):
    return _host.elasticEuclideanDTW1dBacktrace(series0, series1, wpath)
elasticEuclideanDTW1dBacktrace = _host.elasticEuclideanDTW1dBacktrace

def elasticEuclideanCDTW1dBacktrace(series0, series1, window, wpath):
    return _host.elasticEuclideanCDTW1dBacktrace(series0, series1, window, wpath)
elasticEuclideanCDTW1dBacktrace = _host.elasticEuclideanCDTW1dBacktrace

def elasticEuclideanCDTW2dBacktrace(series0, series1, window, wpath):
    return _host.elasticEuclideanCDTW2dBacktrace(series0, series1, window, wpath)
elasticEuclideanCDTW2dBacktrace = _host.elasticEuclideanCDTW2dBacktrace

def elasticQuaternionCDTWd(series0, series1, window):
    return _host.elasticQuaternionCDTWd(series0, series1, window)
elasticQuaternionCDTWd = _host.elasticQuaternionCDTWd

def elasticWarpingEnvelopeNd(series0, env_lower, env_upper, window, stride):
    return _host.elasticWarpingEnvelopeNd(series0, env_lower, env_upper, window, stride)
elasticWarpingEnvelopeNd = _host.elasticWarpingEnvelopeNd

def elasticLBKim4d(series0, series1):
    return _host.elasticLBKim4d(series0, series1)
elasticLBKim4d = _host.elasticLBKim4d

def residuesMatrixEuclideanNd(series0, series1, matrix, stride):
    return _host.residuesMatrixEuclideanNd(series0, series1, matrix, stride)
residuesMatrixEuclideanNd = _host.residuesMatrixEuclideanNd
# This file is compatible with both classic and new-style classes.


