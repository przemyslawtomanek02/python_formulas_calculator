from flask import Blueprint, render_template, request
import formulas_functions
import validators

#-----  Wiadomość do walidacji - start -----#
validate_message = 'Wartości muszą być większe od 0'
#-----  Wiadomość do walidacji - koniec -----#

#-----  Views - start -----#
views = Blueprint(__name__, "views")
#-----  Views - koniec -----#

#----- Strona główna - start -----#
@views.route("/")
def home():
  return render_template("home.html")
#----- Strona główna - koniec -----#

#----- Kwadrat - start -----#
@views.route("/square", methods=['GET', 'POST'])
def square_area():
    # Punk wejscia danych POST
    if request.method == 'POST':
        a_string = request.form.get('side-square')
        # Próba wykonania działania na liczbach
        try:
            a = float(a_string)
            # Walidacja danych
            validate_error = validators.validate_single_date(a)
            if validate_error:
                return render_template("square.html", error_0=validate_message) 
            # Renderowanie wyniku
            return render_template("square.html", square_area=formulas_functions.square_area(a))
        # Walidacja is int
        except ValueError: 
            return render_template("square.html", error_0=words_error_message) 
    # Wyświetlanie strony
    return render_template("square.html")
#----- Kwadrat - koniec -----#

#----- Prostokąt - start -----#
@views.route("/rectangle", methods=['GET', 'POST'])
def rectangle_area():
    # Punk wejscia danych POST
    if request.method == "POST":
        w_string = request.form.get('w')
        h_string = request.form.get('h')
        # Próba wykonania działania na liczbach
        try:
            w = float(w_string)
            h = float(h_string)
            # Walidacja danych
            validate_error = validators.validate_two_date(w, h)
            if validate_error:
              return render_template("rectangle.html", error_0=validate_message)
            # Renderowanie wyniku
            return render_template("rectangle.html", rectangle_area=formulas_functions.rectangle_area(w, h))
        # Walidacja is int
        except ValueError:
            return render_template("rectangle.html", error_0=validate_message)
    # Wyświetlanie strony
    return render_template("rectangle.html")
#----- Prostokąt - koniec -----#

#----- Trójkąt - start -----#
@views.route("/triangle", methods=['GET', 'POST'])
def triangle_area():
    # Punk wejscia danych POST
    if request.method == 'POST':
        b_string = request.form.get('b')
        h_string = request.form.get('h')
        # Próba wykonania działania na liczbach
        try:
            b = float(b_string)
            h = float(h_string)
            # Walidacja danych
            validate_error = validators.validate_two_date(b, h)
            if validate_error:
                return render_template('triangle.html', error_0=validate_message)
            # Renderowanie wyniku
            return render_template('triangle.html', triangle_area=formulas_functions.triangle_area(b, h))
        # Walidacja is int
        except ValueError:
            return render_template('triangle.html', error_0=words_error_message)
    # Wyświetlanie strony
    return render_template("triangle.html")
#----- Trójkąt - koniec -----#