# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:06:32 2024

@author: HP
"""
#s = 0.5*n*R**2*math.sin(math.2*pi/2)
#p = 2*n*R*math.sin(mathpi/n)
# =============================================================================
# r = input('R ni kiriting\n>>>')
# n = input('n ni kiriting\n>>>')
# =============================================================================
import math
def perimetr(n,R):
    return 2*n*R*math.sin(math.pi/n)
def yuza(n,R):
    return  0.5*n*(R**2)*math.sin((2*math.pi)/n)
R = int(input('R ni kiriting\n>>>'))
n = int(input('n ni kiriting\n>>>'))

print(perimetr(n, R))
print(yuza(n, R))


#R radiusli doiraga ichki chizilgan muntazam n-burchakning perimetri va yuzasi hisoblansin.
#DONE>>>>>>>>........<<<<<<

