import os
here=__file__
回退到上几级目录=2
for i in range(回退到上几级目录):
    here=os.path.dirname(here)
del os,回退到上几级目录,i

import sys
for folder in ("AmusementPark","Shade"):
    sys.path.append(
        here+\
        "/Stay/"+folder)
del sys,here,folder

#../Shade
from Obliged_setBuiltInType import *

#../AmusementPark
from PKP_color import *
from PKP_readSpecifyScope import *
from PKP_lengthsplit import *
from PKP_totype import *
from PKP_istypesame import *
from PKP_istypethisone import *
from PKP_insertm import *
from PKP_unpack import *
from PKP_substract import *
from PKP_draw import *

#按创建时间顺序排列
#2021.5.10 18:14
#readSpecifyScope()

#2021.6.29 10:25~
#<class '颜色世界'>

#2021.6.30 2:01
#str.lengthsplit()

#2021.6.30 10:29~
#（Not Mine）
#《Obliged_setBulitInType.py》

#2021.6.29 16:50~17:13
#list.istypesame()

#2021.7.1 8:31
#list.istypethisone()

#2021.7.1 16:43
#list.insertm()

#2021.10.6 1:40~2:14
#list.totype()

#2021.10.5 23:42~
#list.unpack()

#2021.10.6 3:49~4:08
#list.substract()

#2021.10.6 4:47~4:57
#list.draw()
