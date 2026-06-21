from flask import Blueprint, render_template, request
import formulas_functions
error = "ERROR MESSAGE"


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
            return render_template("square.html", error_0="Akceptowane są tylko liczby") 
            
    # Standardowe wejście na stronę (metoda GET)
    # Zwracamy CZYSTY szablon, bez żadnych dodatkowych zmiennych!
    return render_template("square.html")

@views.route("/rectangle", methods=['GET', 'POST'])
def rectangle_area():
  wynik = None
  if request.method == "POST":
    w_string = request.form.get('w')
    h_string = request.form.get('h')
    if w_string == "" and h_string == "":
      error = "this is message"
      return render_template("rectangle.html", rectangle_area=error )
    w = float(w_string)
    h = float(h_string)
    print("--------------", request.form, "--------------")
    wynik = formulas_functions.rectangle_area(w, h)
  return render_template("rectangle.html", rectangle_area=wynik)

