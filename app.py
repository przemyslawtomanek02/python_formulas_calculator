from flask import Flask, request, render_template
from views import views

app = Flask(__name__)
app.register_blueprint(views, ulr_prefix="/")

if __name__ == '__main__':
  app.run(debug=True, port=8000)  

@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404