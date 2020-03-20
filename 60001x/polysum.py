import math

def polysum(sides, length):
  '''
  sides: an int denoting the number of sides the shape has
  length: an int or float denoting the length of the sides

  returns: a float, summing the area and perimeter squared, rounded to 4 decimal places
  '''
  if sides == 0 or length == 0:
    return 0
  else: 
    area = (0.25 * sides * length**2) / math.tan(math.pi / sides)
    perimeter = sides * length
  
  return round(area + perimeter**2,4)

from math import * # importing math library for using tan and pi constant for calculation


def polysum2 (n,s):
    """
    This function takes in two arguments and returns the sum of area and peremeter of the regular polegon
    The returned value is rounded to 4 decemial places.
    n is an integer denoting number of sides of polygon
    s can be an integer or float for denoting length of side of polygon	
    """
    area = (0.25*n*(s*s))/tan(pi/n) 
    perimeter = (n*s)**2
    ans = area+perimeter
    return round(ans,4)

    '''
Area de um poligono regular =
(0.25 * n * s**2)/(tan(Pi/n))
n = numero de lados
s = comprimento da aresta do poligono

Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
'''
import math

def polysum3(n, s):
  area = (0.25 * n * s**2)/(math.tan(math.pi/n))
  perimeter = n * s
  return float('%.4f' % (area + perimeter**2))


print(polysum(100,5), polysum2(100,5), polysum3(100,5))