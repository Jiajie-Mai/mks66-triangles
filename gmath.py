import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    factor = magnitude(vector)
    for x in range(vector):
        vector[x] /= factor
    return vector

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    x = polygons[i]
    y = polygons[i + 1]
    z = polygons[i + 2]
    output = []
    return output


def magnitude(vector):
    output = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    return output
