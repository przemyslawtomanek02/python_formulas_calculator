import math
Pi = math.floor(math.pi * 100)/100

# square area - in
def square_area(l):
    cacl_square_area = l * l
    return cacl_square_area
# rectangle area - in
def rectangle_area(w, h):
    cacl_rectangle_area = w * h
    return cacl_rectangle_area
# triangle area - in
def triangle_area(b, h):
    calc_triangle_area = (b * h)/2
    return calc_triangle_area
# rhombus area - in
def rhombus_area(D, d):
    calc_rhombus_area = (D * d)/2
    return calc_rhombus_area
# trapezoid area - in
def trapezoid_area(B, b, h):
    calc_trapezoid_area = ((B + b)/2) * h
    return calc_trapezoid_area
# regular polygon area - in
def regular_polygon_area(P, a):
    calc_regular_polygon_area = (P/2) * a
    return calc_regular_polygon_area
# circle area - in
def circle_area(r):
    calc_circle_area = Pi * (r * r)
    return calc_circle_area
def cone_area(r, s):
    calc_cone_area = (Pi * r) * s
    return calc_cone_area
def sphere_area(r):
    calc_sphere_area = (4 * Pi) * (r * r)
    return calc_sphere_area