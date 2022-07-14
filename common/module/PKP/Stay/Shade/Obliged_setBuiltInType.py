import operator
import functools
import ctypes
class PyObject(ctypes.Structure):
    class PyType(ctypes.Structure):
        pass
    ssize = ctypes.c_int64 if\
ctypes.sizeof(ctypes.c_void_p) == 8 else\
ctypes.c_int32
    _fields_ = [
     ('ob_refcnt', ssize), 
     ('ob_type', ctypes.POINTER(PyType)), 
     ]
def sign(klass, func_name):
    def _(function):
        class SlotsProxy(PyObject):
            _fields_ = [('dict', ctypes.POINTER(PyObject))]
        name, target = klass.__name__, klass.__dict__
        proxy_dict = SlotsProxy.from_address(id(target))
        namespace = {}
        ctypes.pythonapi.PyDict_SetItem( \
ctypes.py_object(namespace),
ctypes.py_object(name), proxy_dict.dict, )
        namespace[name][func_name] = function
    return _ 


#updated:2021.6.30 10:29~
#网上找的修改内置类型的代码
