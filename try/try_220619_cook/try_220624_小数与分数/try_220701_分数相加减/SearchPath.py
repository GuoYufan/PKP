import os
here=__file__
#当设置为1 为回退到最底层目录
回退到上几级目录=5
for i in range(回退到上几级目录):
    here=os.path.dirname(here)
del 回退到上几级目录,i


import sys
sys.path.append(
	here+os.sep.join(
	(
	str(),"common",
	"Lively",
	)
))
del os,sys,here


if __name__=="__main__":
    print(dir())
