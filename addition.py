
def addition(a, b):
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("boths Inputs must be positive integers")
    
    return a + b


