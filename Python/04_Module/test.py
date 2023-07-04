
"""
 # Ex1)
import calc                         # import 모듈 이름
print(calc.plus(10, 5))
print(calc.minus(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5)) 
"""

"""
# Ex2)
from calc import plus, minus
print(plus(10, 5))
print(minus(10, 5))
"""

#Ex3)
import calc  as c
print(c.plus(10, 5))

# python 표준 모듈 목록
import sys 
print(sys.builtin_module_names)

import time     # time 모듈 함수
print(dir(time))
print()

print(dir(c))
print()

help(time.localtime)     # 함수의 상세한 도움말

# 외부 pip install Numpy
import numpy as np
mylist=[1, 2, 3, 4, 5]
myarr=np.array(mylist)
print(myarr, type(myarr))
print(myarr.size)
print(myarr.shape)
