import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    x = math.sqrt(sq)
    if sq % x ==0:
        x +=1
        next_square = x*x
        return next_square
    else:
        return -1