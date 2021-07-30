import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
# This is the instance of our Flask app using pyMongo

@app.route("/")
@app.route("/get_films")
def get_films():
    films = mongo.db.film_list.find()
    return render_template("get_films.html", films=films)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        films = list(mongo.db.film_list.find({"$text": {"$search": query}}))
        search = True
        return render_template("get_films.html", films=films, search=search)
    return get_films()


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)