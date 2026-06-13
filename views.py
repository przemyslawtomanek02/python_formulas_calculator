from flask import Blueprint, render_template, request
import formulas_functions



views = Blueprint(__name__, "views")

@views.route("/square", methods=['GET', 'POST'])
def square_area():
  wynik = None
  if request.method == 'POST':
    bok = request.form.get('side-square')
    if bok == "":
      error = "this is message"
      return render_template("index.html", square_area=error )
    na_liczbe = float(bok)
    wynik = formulas_functions.square_area(na_liczbe)
  return render_template("index.html", square_area=wynik )


@views.route("/rectangle", methods=['GET', 'POST'])
def rectangle_area():
  wynik = None
  if request.method == "POST":
    w_string = request.form.get('w')
    h_string = request.form.get('h')
    if w_string == "" and h_string == "":
      error = "this is message"
      return render_template("index.html", rectangle_area=error )
    w = float(w_string)
    h = float(h_string)
    print("--------------", request.form, "--------------")
    wynik = formulas_functions.rectangle_area(w, h)
  return render_template("index.html", rectangle_area=wynik)

