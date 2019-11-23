import ctypes, ctypes.util

def load_library(*alternates):
    for base_name in alternates:
        lib_name = ctypes.util.find_library(base_name)

        try:
            if lib_name:
                return ctypes.CDLL(lib_name)
            else:
                return ctypes.CDLL(base_name)
        except OSError:
            pass

    raise OSError('Unable to load any of: {}'.format(alternates))

_libc = load_library('c', 'msvcrt')

class tm(ctypes.Structure):
    _fields_ = [
        ('tm_sec', ctypes.c_int),
        ('tm_min', ctypes.c_int),
        ('tm_hour', ctypes.c_int),
        ('tm_mday', ctypes.c_int),
        ('tm_mon', ctypes.c_int),
        ('tm_year', ctypes.c_int),
        ('tm_wday', ctypes.c_int),
        ('tm_yday', ctypes.c_int),
        ('tm_isdst', ctypes.c_int),
    ]

printf = _libc.printf

scanf = _libc.scanf

localtime = _libc.localtime
localtime.argtypes = [ctypes.POINTER(ctypes.c_int)]
localtime.restype = ctypes.POINTER(tm)

asctime = _libc.asctime
asctime.argtypes = [ctypes.POINTER(tm)]
asctime.restype = ctypes.c_char_p

from ctypes import c_int, create_string_buffer, byref, Structure

def input_pair():
    key = c_int()
    value = create_string_buffer(16)
    printf(b"[Input a pair as int:string] ")
    scanf(b"%i:%s", byref(key), byref(value))
    return key, value.value

def print_a_time():
    timer = c_int(12345678)
    printf(asctime(localtime(byref(timer))))

"""
# It will try to find the full name of the version installed on the system
>>> import ctypes.util
>>> ctypes.util.find_library('c')
 

# Foreign Function Interface

>>> import ctypes
>>> libc = ctypes.CDLL('libc.so.6')
>>> libc.printf('Hello\n')
"""

