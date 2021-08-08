import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
# This is the instance of our Flask app using pyMongo

searching = False
searchQuery = ""

@app.route("/")
@app.route("/get_films")
def get_films():
    global searching
    searching = False

    films = mongo.db.film_list.find().sort("date", -1)
    recs = mongo.db.rec_list.find().sort("date", -1)
    return render_template("get_films.html", films=films, recs=recs)


@app.route("/get_film/<film_title>")
def get_film(film_title):
    global searching
    global searchQuery

    films = mongo.db.film_list.find().sort("date", -1)
    film = mongo.db.film_list.find_one({"title": film_title})
    recs = mongo.db.rec_list.find().sort("date", -1)

    if searching:
        films = list(mongo.db.film_list.find({"$text": {"$search": searchQuery}}))
        return render_template("get_films.html", film=film, films=films, recs=recs,
        search=searching, searchQuery=searchQuery, overlay_profile=True)

    return render_template("get_films.html", film=film, films=films, recs=recs, 
    search=searching, searchQuery=searchQuery, overlay_profile=True)


@app.route("/search", methods=["GET", "POST"])
def search():
    global searching
    global searchQuery
    
    if request.method == "POST":
        query = request.form.get("query")
        searching = True
        searchQuery = query

        films = list(mongo.db.film_list.find({"$text": {"$search": query}}))
        recs = mongo.db.rec_list.find().sort("date", -1)
        return render_template("get_films.html", films=films, recs=recs, 
        search=searching, searchQuery=searchQuery) 
        
    return render_template("get_films.html", films=films, recs=recs, 
    search=searching, searchQuery=searchQuery) 


@app.route("/genre_search/<genre>")
def genre_search(genre):
    global searching
    global searchQuery

    searching = True
    searchQuery = genre

    films = list(mongo.db.film_list.find({"$text": {"$search": genre}}))
    recs = mongo.db.rec_list.find().sort("date", -1)
    return render_template("get_films.html", films=films, search=searching, searchQuery=searchQuery, recs=recs)


@app.route("/add_film", methods=["GET", "POST"])
def add_film():
    if request.method == "POST":
        # Check if film already exists
        exists = mongo.db.film_list.find_one({
            "title": request.form.get("title")
            })
        if exists:
            return get_films()

        film = {
            "title": request.form.get("title"),
            "genre": request.form.get("genre"),
            "poster_url": request.form.get("user_poster_url"),
            "creator": session["user"],
            "date": datetime.datetime.now(),
        }
        title = request.form.get("title")
        mongo.db.film_list.insert_one(film)
        return redirect(url_for("get_film", film_title=title))

    # Won't be called. Only POST.
    return render_template("get_films.html")


@app.route("/edit_film/<film_title>", methods=["GET", "POST"])
def edit_film(film_title):
    global searching
    global searchQuery
    film = mongo.db.film_list.find_one({"title": film_title})
    films = mongo.db.film_list.find().sort("date", -1)
    recs = mongo.db.rec_list.find().sort("date", -1)

    if request.method == "POST": 
        # Check if film already exists
        exists = mongo.db.film_list.find_one({
            "title": request.form.get("title")
            })
        if exists:
            return get_film(film_title)

        # Check if user created film
        userfilm = mongo.db.film_list.find_one({
            "title": request.form.get("title"),
            "creator": session["user"]
        })
        
        filter = {'title': film_title} 

        # New values for film
        submit = {
            "title": request.form.get("title"),
            "genre": request.form.get("genre"),
            "poster_url": request.form.get("user_poster_url"),
            "creator": session["user"],
            "date": datetime.datetime.now(),
        }

        # Only update if user is creator or "admin"
        if userfilm or session["user"] == "admin":
            newTitle = request.form.get("title")
            mongo.db.film_list.update(filter, submit)
            mongo.db.rec_list.update_many(filter, {"$set": {"title": newTitle}})                 
            return get_film(newTitle) 

        return get_film(film_title)
        
    if searching:
        films = list(mongo.db.film_list.find({"$text": {"$search": searchQuery}}))

    return render_template("get_films.html", film=film, films=films, recs=recs,
    overlay_edit=True, overlay_profile=True, search=searching, searchQuery=searchQuery)


@app.route("/delete_film/<film_title>")
def delete_film(film_title):
    global searching
    global searchQuery

    # Deletes film only for creator
    mongo.db.film_list.remove({
        "title": film_title, 
        "creator": session["user"].lower()})
    mongo.db.rec_list.remove({
        "title": film_title, 
        "creator": session["user"].lower()})   

    # Deletes film for admin
    if session["user"].lower() == "admin":   
        mongo.db.film_list.remove({
            "title": film_title})
        mongo.db.rec_list.remove({
            "title": film_title})  

    films = mongo.db.film_list.find().sort("date", -1)
    recs = mongo.db.rec_list.find().sort("date", -1)

    if searching:
        films = list(mongo.db.film_list.find({"$text": {"$search": searchQuery}}))

    return render_template("get_films.html", films=films, search=searching, searchQuery=searchQuery,
    recs=recs)


@app.route("/add_rec", methods=["GET", "POST"])
def add_rec():
    if request.method == "POST":
        # Check if rec already exists for film
        exists = mongo.db.rec_list.find_one({
            "title": request.form.get("title"),
            "book": request.form.get("book")
            })
        if exists:
            return get_film(request.form.get("title"))

        rec = {
            "title": request.form.get("title"),
            "book": request.form.get("book"),
            "author": request.form.get("author"),
            "creator": session["user"],
            "date": datetime.datetime.now(),
        }
        
        mongo.db.rec_list.insert_one(rec) 
        return get_film(request.form.get("title"))
    
    # Won't be called. Only POST.
    return get_film(request.form.get("title"))


@app.route("/edit_rec/<film_title>/<book>", methods=["GET", "POST"])
def edit_rec(film_title, book):
    global searching
    global searchQuery

    film = mongo.db.film_list.find_one({"title": film_title})
    films = mongo.db.film_list.find().sort("date", -1)
    recs = mongo.db.rec_list.find().sort("date", -1)
    editedRec = mongo.db.rec_list.find_one({"book": book, "title": film_title})

    if request.method == "POST": 
        # Check if rec name already exists for film
        exists = mongo.db.rec_list.find_one({
            "title": request.form.get("title"),
            "book": request.form.get("book")
            })
        if exists:
            return get_film(request.form.get("title"))

        # Find IF user recommended book for the film
        filter = {
            'book': book, 
            'title': film_title,
            'creator': session["user"]
        } 

        # If user is admin just find the book for film
        if session["user"].lower() == "admin":
            filter = {
                'book': book, 
                'title': film_title,
        }  

        # New values for recommendation
        newvalues = {"$set": {
            "title": request.form.get("title"),
            "book": request.form.get("book"),
            "author": request.form.get("author"),
            "creator": session["user"],
            "date": datetime.datetime.now()
        }}

        mongo.db.rec_list.update_one(filter, newvalues)

        if searching:
            films = list(mongo.db.film_list.find({"$text": {"$search": searchQuery}}))

        return get_film(request.form.get("title"))

    if searching:
        films = list(mongo.db.film_list.find({"$text": {"$search": searchQuery}}))

    return render_template("get_films.html", film=film, films=films, recs=recs, 
    editedRec=editedRec, overlay_profile=True, overlay_edit_rec=True, 
    search=searching, searchQuery=searchQuery)


@app.route("/delete_rec/<film_title>/<book>")
def delete_rec(film_title, book):
    mongo.db.rec_list.remove({
        "book": book,
        "title": film_title, 
        "creator": session["user"].lower()})  

    if session["user"].lower() == "admin":
        mongo.db.rec_list.remove({
            "book": book, 
            "title": film_title})  

    return get_film(film_title)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username from form already exists in database
        existing_user = mongo.db.readflix_users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            return render_template("register.html", fail=True)
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.readflix_users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        return redirect(url_for("get_films"))
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
                return redirect(url_for("get_films"))
            else:
                # invalid password match
                return render_template("login.html", fail=True)

        else:
            # if existing_user, the username, doesn't exist
            return render_template("login.html", fail=True)

    # else if method != POST just return login.html
    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from the session cookies
    session.pop("user")
    return get_films()
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)