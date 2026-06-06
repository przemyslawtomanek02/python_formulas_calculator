import formulas_functions
print("         ")
print('------------------Use only "cm"------------------')
print('1: Square Area, 2: Rectangle Area,  ')
print('3: Triangle Area, 4: Rhombus area  ')
print('5: Trapezoid Area, 6: Regular polygon  ')
print('7: Circle Area, 8: Regular polygon  ')

while True:
    option = int(input('[0 - to exit] What do you need calc:'))
    if option == 0:
        quit()
    elif option == 1:
        l = int(input('l : length of side:'))
        formulas_functions.square_area(l)
    elif option == 2:
        w = int(input('w : width:'))
        h = int(input('h : height:'))
        formulas_functions.rectangle_area(w, h)
    elif option == 3:
        b = int(input('b : base:'))
        h = int(input('h : height:'))
        formulas_functions.triangle_area(b, h)
    elif option == 4:
        D = int(input('D : large diagonal:'))
        d = int(input('d : small diagonal:'))
        formulas_functions.rhombus_area(D, d)
    elif option == 5:
        B = int(input('B : large side:'))
        b = int(input('b : small side:'))
        h = int(input('h : height:'))
        formulas_functions.trapezoid_area(B, b, h)
    elif option == 6:
        P = int(input('P : perimeter:'))
        a = int(input('a : apothem:'))
        formulas_functions.regular_polygon_area(P, a)
    elif option == 7:
        r = int(input('r : apothem:'))
        formulas_functions.circle_area(r)
    elif option == 8:
        r = int(input('r : apothem:'))
        s = int(input('s : slant height:'))
        formulas_functions.cone_area(r, s)
    elif option == 9:
        r = float(input('r : radius:'))
        formulas_functions.sphere_area(r)