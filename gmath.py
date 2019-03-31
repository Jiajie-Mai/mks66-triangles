import math
from display import *

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    factor = magnitude(vector)
    for x in range(vector):
        vector[x] /= factor

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def cross_product(a, b):
    return [a[1] * b[2] - b[1] * a[2], a[2] * b[0] - b[2] * a[0], a[0] * b[1] - b[0] * a[1]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    point1 = polygons[i]
    point2 = polygons[i + 1]
    point3 = polygons[i + 2]
    vectorA = [point2[0] - point1[0], point2[1] - point1[1], point2[2] - point1[2]]
    vectorB = [point3[0] - point1[0], point3[1] - point1[1], point3[2] - point1[2]]
    return cross_product(output)


def magnitude(vector):
    output = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    return output
