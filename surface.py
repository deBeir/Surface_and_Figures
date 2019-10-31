# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:40:18 2019

@author: Sofia
"""
# =============================================================================
# IMPORTS
# =============================================================================
import random
# =============================================================================
# SURFACE
# =============================================================================
# =============================================================================
# This class creates a surface with a certain dimension
# The surface is able to store a finite number of rectangles and circles, as 
# long as the figures do not overlap nor surpass the edges of the surface.
# It contains a method that automatically places the given figures as long as
# there's still space left. Since it gives the figures random x and y coordi-
# nates, the figures are not placed one after the other.
# =============================================================================
class Surface:
    
    def __init__(self,width,height):
        self.width = int(width)
        self.height = int(height)
        self.area = self.width * self.height
        # list to take all figures that will be inserted into the surface
        self.placed_figures = []
    
    def occupied_area(self):
        # returns the total area occupied by the inserted figures         
        occupied_area = 0
        for figure in self.placed_figures:
            occupied_area += (figure.width * figure.height)        
        return occupied_area
            
    def valid_coordinates(self,figure,x,y):
        # makes sure the desired coordinates are within the surface area         
        if x >= 0 and y >= 0 and x + figure.width <= self.width and y + figure.height <= self.height:
            return True
    
    def overlap(self,figure):
        # checks wheter or not the figures overlap within one another         
        # if False, then the figures DO NOT overlap 
        
        # if the list is empty, so is the surface - first figure can be inserted anywhere
        if len(self.placed_figures) == 0:
            self.placed_figures.append(figure)
            return False      
        else:
            for figure2 in self.placed_figures:
                if figure.posx > figure2.posx + figure2.width or figure2.posx > figure.posx + figure.width or \
                   figure.posy < figure2.posy - figure2.height or figure2.posy < figure.posy - figure.height:                       
                       self.placed_figures.append(figure)
                       return False
        return True
                    
    def rectangle_placement(self,figure,x,y):
        # checks if a rectangle can be placed inside the surface given x and y coordinates
       
        # checks if x and y are valid coordinates, this is, are inside the surface
        if self.valid_coordinates(figure,x,y) == True:
            figure.setposition(x,y)               
            # checks if the figure overlaps with another one
            if self.overlap(figure) == False:
                print("{0} successfully placed at coordinates {1},{2}.".format(figure.name,figure.posx,figure.posy))
                return True
            elif self.overlap(figure) == True:               
                figure.setposition(-1,-1)
                print("{0} wasn't placed.".format(figure.name))
    
    def circle_placement(self,figure,x,y):
        # checks if a circle can be placed inside the surface given x and y coordinates 
        
        # checks if x and y are valid coordinates, this is, are inside the surface
        if self.valid_coordinates(figure,x,y) == True:
            figure.setposition(x,y)    
            # checks if the figure overlaps with another one
            if self.overlap(figure) == False:
                print("{0} successfully placed at coordinates {1},{2}.".format(figure.name,figure.posx,figure.posy))
                return True
            elif self.overlap(figure) == True:               
                figure.setposition(-1,-1)
                print("{0} wasn't placed.".format(figure.name))
        
                            
    def move(self,figure,x,y):
        # if possible, moves the figure to another position        
        self.placed_figures.remove(figure)
        figure.setposition(-1,-1)      
        
        if self.rectangle_placement(figure,x,y) == True or self.circle_placement(figure,x,y) == True:
            figure.setposition(x,y)
            print("{0} moved to position {1},{2}.".format(figure.name,figure.posx,figure.posy))        
        else:
            print("{0} was not moved.".format(figure.name))
    
    def rotation(self,figure):
        # if possible, rotates the figure (90º angle)
        temp = figure.width #temporary variable
        figure.width = figure.height
        figure.height = temp
        
        if self.rectangle_placement(figure,figure.posx,figure.posy) == True:
            print("{0} successfully rotated.".format(figure.name))
        else:
            print("{0} was not rotated.".format(figure.name))
            
    def clear(self):
        # removes all figures from the surface
        del self.placed_figures[:]
            
    def auto_placement(self,figure):         
        # automatically places a figure at a random position
        # (as long as figures do not overlap)
        # since the coordinates are randomly attributed, there's no need to place the first figure at position (0,0)
        x = random.randrange(self.width)
        y = random.randrange(self.height)
        self.rectangle_placement(figure,x,y)
         
        # if the figure is not placed because of the overlap with another figure, we use recursion to find a new position
        if figure.getposition() == (-1,-1):
            return self.auto_placement(figure)
        # checks if there's no more space, thus being impossible to store any more figures
        elif self.occupied_area() == self.area:
            print("Can't place any more figures.")
# =============================================================================
#                            
# =============================================================================
# =============================================================================
#     
# =============================================================================
# =============================================================================
#     
# =============================================================================
# =============================================================================
#     
# =============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    