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


@app.route("/edit_film/<film_title>", methods=["GET", "POST"])
def edit_film(film_title):
    if request.method == "POST": 
        submit = {
            "title": request.form.get("title"),
            "genre": request.form.get("genre"),
            "poster_url": request.form.get("user_poster_url"),
        }
        newTitle = request.form.get("title")
        mongo.db.film_list.update({"title": film_title}, submit)
        mongo.db.rec_list.update_many({"title": film_title}, {"$set": {"title": newTitle}})     
        return get_film(newTitle)

    film = mongo.db.film_list.find_one({"title": film_title})
    films = mongo.db.film_list.find()
    return render_template("get_films.html", film=film, films=films, 
    overlay_edit=True)


@app.route("/delete_film/<film_title>")
def delete_film(film_title):
    mongo.db.film_list.remove({"title": film_title})
    mongo.db.rec_list.remove({"title": film_title})     
    flash("Film Successfully Deleted")
    return redirect(url_for("get_films"))


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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username from form already exists in database
        existing_user = mongo.db.readflix_users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for('register'))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.readflix_users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Succesful")    
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username input in login.html exists in db
        existing_user = mongo.db.readflix_users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
        # if existing_user (the username) exists in database

            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], 
            request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return get_films()
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if existing_user, the username, doesn't exist
            flash("Incorrect Username and/or Password")    
            return redirect(url_for("login"))  

    # else if method != POST just return login.html
    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from the session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)