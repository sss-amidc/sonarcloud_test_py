import math

def rotate_point(x, y, angle_rad):
    """
    Rotate a point around the origin (0, 0) by a given angle in radians.
    
    Parameters:
    x (float): x-coordinate of the point.
    y (float): y-coordinate of the point.
    angle_rad (float): Rotation angle in radians.
    
    Returns:
    tuple: New coordinates (x', y') after rotation.
    """
    x_new = x * math.cos(angle_rad) + y * math.sin(angle_rad)
    y_new = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return x_new, y_new

def inverse_rotate_point(x, y, angle_rad):
    """
    Rotate a point around the origin (0, 0) by a given angle in radians.
    
    Parameters:
    x (float): x-coordinate of the point.
    y (float): y-coordinate of the point.
    angle_rad (float): Rotation angle in radians.
    
    Returns:
    tuple: New coordinates (x', y') after rotation.
    """
    x_new = x * math.cos(angle_rad) + y * math.sin(angle_rad)
    y_new = x * math.sin(angle_rad) - y * math.cos(angle_rad)
    return x_new, y_new