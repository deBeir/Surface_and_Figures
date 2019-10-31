# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:58:16 2019

@author: Sofia
"""
# =============================================================================
# RECTANGLE
# =============================================================================
class Rectangle:
    
    def __init__(self,name,width,height,x=-1,y=-1):
        self.name = str(name)
        self.width = int(width)
        self.height = int(height)
        self.posx = x
        self.posy = y
        
    def area(self):
        self.area = self.width * self.height
        return self.area
        
    def getposition(self):
        return (self.posx,self.posy)
    
    def setposition(self,x,y):
        self.posx = x
        self.posy = y
# =============================================================================
#         
# =============================================================================
   