# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:19:40 2021

@author: govin
"""

import matplotlib.pyplot as plt
import nump as np


x = np.linspace(0,50,100)
y = 18-2*x #2x+y=18
y1 = (42 - 2*x)/3 #2x+3y=42

# Create the plot
plt.plot(x,y,label='2x+y=18')
plt.plot(x,y1,label='2x+3y=42')
plt.grid(alpha=.4,linestyle='--')
plt.ylim(0, 30)
plt.xlim(0,30)
plt.legend()
plt.show()

def end_points(cx,cy,B):
    p=[]
    p1=[]
    p1.append(0)
    p1.append(B/cy)
    p2=[]
    p2.append(B/cx)
    p2.append(0)
    p.append(p1)
    p.append(p2)
    print(p)
    return p[0],p[1]

A,B = end_points(2,1,18)
C,D = end_points(2,3,42)

def int_point(a1,b1,c1,a2,b2,c2):
    D = a1*b2 - a2*b1
    Dx = c1*b2 - c2*b1
    Dy = a1*c2 - a2*c1
    
    if D==0:
        return -1,-1
    else:
        x=Dx/D
        y=Dy/D
        return x,y
p,q = int_point(2,1,18,2,3,42)
print(p,q)

