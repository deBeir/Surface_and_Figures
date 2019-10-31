# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:01:29 2019

@author: Sofia
"""
# =============================================================================
# IMPORT
# =============================================================================
from rectangle import Rectangle
from circle import Circle
from surface import Surface
# =============================================================================
# TESTING
# =============================================================================
# =============================================================================
# Create: Surface
# =============================================================================
S = Surface(1000,500)
# =============================================================================
# Rectangles
# =============================================================================
def test_R():
    # creates rectangles
    R1 = Rectangle('R1',100,100)
    R2 = Rectangle('R2',100,200)
    
    # insertsthe rectangles
    print("\n#==== RECTANGLES PLACEMENT ====#")
    S.rectangle_placement(R1, 10, 10) 
    S.rectangle_placement(R2, 70, 100) 
    S.move(R1,181,0)
    S.rectangle_placement(R2,70,100)
    
    # rotates the rectangles
    S.rotation(R1)
# =============================================================================
# Circles    
# =============================================================================
def test_C():
    # creates circles
    C1=Circle("C1", 100) 
    C4=Circle("C4", 50) 
    
    # inserts the circles
    print("\n#==== CIRCLES PLACEMENT ====#")
    S.circle_placement(C1, 250, 250) 
    S.circle_placement(C4, 190, 200) 
# =============================================================================
#  Self Placement   
# =============================================================================
def autoplacement():
    # clears the surface to place new figures.
    S.clear()
    
    print("\n#==== AUTOPLACEMENT ====#")
    # creates the figuress      
    R1 = Rectangle('R1',100,100)
    R2 = Rectangle('R2',100,200)
    R3 = Rectangle('R3',50,100)
    R4 = Rectangle('R4',400,400)
    R5 = Rectangle('R5',200,200)
    C1=Circle("C1", 100) 
    C2=Circle("C2", 100) 
    C3=Circle("C3", 100)
    C4=Circle("C4", 50)

    # places the figures
    S.auto_placement(R1)
    S.auto_placement(R2)
    S.auto_placement(R3)
    S.auto_placement(R4)
    S.auto_placement(R5)
    S.auto_placement(C1)
    S.auto_placement(C2)
    S.auto_placement(C3)
    S.auto_placement(C4)

# =============================================================================
# Area    
# =============================================================================
def area():
    print("\n#==== AREA ===#")
    remain = S.area - S.occupied_area()
    print("Occupied area:{0}".format(S.occupied_area()))
    print("Remaining area:{0}".format(remain))    
# =============================================================================
#  Main  
# =============================================================================
if __name__ == "__main__":
    test_R()  
    test_C()
    autoplacement()
    area()