import math 
import sys
import os
import numpy as np

# Add the application directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../application')))
from utils import rotate_point, inverse_rotate_point

def test_rotate_point_45_degrees():
    x, y = 1, 1
    angle = math.radians(45)
    result = rotate_point(x, y, angle)
    expected = (0, 1.414)

    assert np.all(np.isclose(result, expected, atol=1e-3))

def test_inverse_rotate_point_90_degrees():
    x, y = 0, 1
    angle = math.radians(90)
    result = inverse_rotate_point(x, y, angle)
    expected = (1, 0)

    assert np.all(np.isclose(result, expected, atol=1e-3))