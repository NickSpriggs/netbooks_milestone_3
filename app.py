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
    recs = mongo.db.rec_list.find()
    return render_template("get_films.html", films=films, recs=recs)


@app.route("/get_film/<film_title>")
def get_film(film_title):
    film = mongo.db.film_list.find_one({"title": film_title})
    films = mongo.db.film_list.find()
    recs = mongo.db.rec_list.find()
    return render_template("get_films.html", film=film, films=films, recs=recs, overlay_profile=True)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        films = list(mongo.db.film_list.find({"$text": {"$search": query}}))
        recs = mongo.db.rec_list.find()
        search = True
        return render_template("get_films.html", films=films, recs=recs, 
        search=search) 
    return get_films()


@app.route("/genre_search/<genre>")
def genre_search(genre):
    films = list(mongo.db.film_list.find({"$text": {"$search": genre}}))
    recs = mongo.db.rec_list.find()
    search = True
    return render_template("get_films.html", films=films, search=search, recs=recs)


@app.route("/add_film", methods=["GET", "POST"])
def add_film():
    if request.method == "POST":
        film = {
            "title": request.form.get("title"),
            "genre": request.form.get("genre"),
            "poster_url": request.form.get("user_poster_url"),
        }
        mongo.db.film_list.insert_one(film)
        flash("Film Successfully Added")
        return redirect(url_for("get_films"))

    return render_template("get_films.html")


@app.route("/add_rec", methods=["GET", "POST"])
def add_rec():
    if request.method == "POST":
        rec = {
            "title": request.form.get("title"),
            "book": request.form.get("book"),
            "author": request.form.get("author"),
        }
        mongo.db.rec_list.insert_one(rec) 
        flash("Successfully Added")
        return get_film(request.form.get("title"))
    
    return get_film(request.form.get("title"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)