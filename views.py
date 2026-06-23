from flask import Blueprint, render_template, request
import formulas_functions
words_error_message = "Akceptowane są tylko liczby"
side_0_error_message = "Bok nie może być mniejszy od 0"


views = Blueprint(__name__, "views")

@views.route("/")
def home():
  return render_template("home.html")

@views.route("/square", methods=['GET', 'POST'])
def square_area():
    if request.method == 'POST':
        bok = request.form.get('side-square')
        try:
            na_liczbe = float(bok)
            if na_liczbe < 0:
                # Błąd 1: Ujemna liczba
                return render_template("square.html", error_0="Bok nie może być mniejszy od 0") 
            
            # Sukces: Liczymy i oddajemy wynik
            wynik = formulas_functions.square_area(na_liczbe)
            return render_template("square.html", square_area=wynik)
            
        except ValueError: 
            # Błąd 2: Ktoś wpisał tekst
            return render_template("square.html", error_0=words_error_message) 
            
    # Standardowe wejście na stronę (metoda GET)
    # Zwracamy CZYSTY szablon, bez żadnych dodatkowych zmiennych!
    return render_template("square.html")

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
            if w < 0 or h < 0:
              return render_template("rectangle.html", error_0=side_0_error_message )
            backend_rectangle_are = formulas_functions.rectangle_area(w, h)
            return render_template("rectangle.html", rectangle_area=backend_rectangle_are)
        except ValueError:
            #Błąd ktoś wpisał teskt
            return render_template("rectangle.html", error_0=words_error_message)
    return render_template("rectangle.html")

