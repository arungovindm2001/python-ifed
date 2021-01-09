def nearest_square(number):
    absoluteNumber = abs(number)
    sqrt = absoluteNumber**(1/2)
    roundoff = int(sqrt)
    square = roundoff**2
    return square
