from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/", methods=['GET', 'POST'])
def home():
  wynik = None
  if request.method == 'POST':
    bok_z_html = request.form.get('side-square')
    bok = float(bok_z_html)
    wynik = bok * bok
  return render_template("index.html", pole=wynik )
