import numpy as np
from sin_func import sin2d
#  This is a unit test 

# Test edge cases fib(0) and fib(1)
def test_internal_case():
    #Test edge 0
    obs = sin2d(np.pi / 2.0, 3.0 * np.pi/2.0)
    exp = (2.0 / np.pi) * (-2.0/(3.0 * np.pi))
    assert obs == exp
    
# Create a function to test fib(1)
def test_edge_x():
     #Test edge 1
     obs = sin2d(0.0, 3.0 *np.pi/2.0)
     exp = (-2.0 / (3.0 * np.pi))
     assert obs == exp
     
def test_edge_y():
     obs = sin2d(np.pi / 2.0, 0.0)
     exp = (2.0 / np.pi) # it is normally your reference not computed manually
     assert obs == exp # You can use assert_allclose from numpy   
     
#What if you have a negative value 
def test_corner():
    obs = sin2d(0,0) 
    exp = 1.0
    assert obs == exp


# Function to test "standard" behaviour
