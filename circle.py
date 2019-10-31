# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:58:05 2019

@author: Sofia
"""
# =============================================================================
# IMPORTS
# =============================================================================
from math import pi
# =============================================================================
# CIRCLE
# =============================================================================
class Circle:
    
    def __init__(self,name,diameter,x=-1,y=-1):
        self.name = str(name)
        self.diameter = int(diameter)
        self.radius = self.diameter / 2
        self.width = self.diameter
        self.height = self.diameter
        self.posx = x
        self.posy = y
        
    def area(self):
        self.area = pi * self.radius ** 2
        return self.area
    
    def getposition(self):
        return(self.posx,self.posy)
    
    def setposition(self,x,y):
        self.posx = x
        self.posy = y
# =============================================================================
#         
# =============================================================================
