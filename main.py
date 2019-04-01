from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

# i = 0
# while i < 500:
#     add_sphere( edges, 250, 250, 250, 100 + i, 20 )
#     i += 150
#
# draw_polygons(edges, screen, color)
# display(screen)
# save_extension(screen, args[0])

parse_file( 'script', edges, polygons, transform, screen, color )
