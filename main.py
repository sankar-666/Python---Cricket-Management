from flask import Flask,render_template
from public import public
from admin import admin
from team import team
from player import player
from api import api

app=Flask(__name__)

app.secret_key="prayulla"

app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(team,url_prefix="/team")
app.register_blueprint(player,url_prefix="/player")
app.register_blueprint(api,url_prefix="/api")
app.register_blueprint(public)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

app.run(debug=True,port=5072,host="0.0.0.0")