import os
here=__file__
#当设置为1 为回退到最底层目录
回退到上几级目录=2
for i in range(回退到上几级目录):
    here=os.path.dirname(here)
del os,回退到上几级目录,i

import sys
sys.path.append(here+"/Shade")
del sys,here
from Obliged_setBuiltInType import *