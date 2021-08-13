# Milestone Back-End Development Project

The following project was my attempt to create a book recommendation website for users who are trying watch
less television. To help with this the recommendations are based on the viewing habits of the visitors. Each film
is suggested and added to the site by a user, as are the respective recommendations for each film. This site currently
makes use of HTML, CSS, Python, Jinja, and Javascript. It also relies on Heroku for deployment and MongoDB for data
storage. 

[View live project](https://readflix.herokuapp.com/)

# UX

My goal was to create a website that would allow users interested in reading more to find books based
on their existing movie viewing habits. Specifically my goals were to:
- Allow unregistered users to search for films and view their respective book recommendations.
- Allow registered users to add films and recommendations to the site database. 
    - Only allow the admin and the user who created the film/recommendation to update
    or delete them from the database. [The admin login is username: admin / password: bookmark]

## User Stories

-   #### First Time User Goals

    1. As a First Time User, I want to easily locate different films, either by title or genre. 
    2. As a First Time User, I want to easily find the recommendations for the films. 
    3. As a First Time User, I would like the option to register for an account.   

-   #### Returning User Goals

    1. As a Returning User, I want to be able to login to my account.
    2. As a Returning User, I would like to add films to the site so that others might offer 
    reading suggestions based on my preferences. 
    3. As a Returning User, I would like to be able to upload my own book suggestions for certain films.
        - I would also like to be able to alter or delete any recommendations I may have made.   

# Wireframes:
<img src="static/img/wireframes/Landing Page.png">
<img src="static/img/wireframes/Poster Click [Logged In].png">
<img src="static/img/wireframes/Login:Register Page.png">
<img src="static/img/wireframes/Landing Page [Logged In].png">
<img src="static/img/wireframes/Add Poster:Film [Logged In].png">
<img src="static/img/wireframes/Poster Add Rec [Logged In].png">

# Database Schema:
MongoDB is used to store the data pertaining to this site. The relationship between the different databases can be seen
below. 

<img src="static/img/db_schema.png">

Each user has a name and password. When a user creates a film, their name is stored in the film. Likewise when a user 
creates a recommendation for a film their name, as well as the film's title, is stored in the recommendation. 

# Features

- Mobile, desktop, and tablet scalable.

- User can add/edit/delete films and books on the site database. 

# Technology Used

## Languages

- HTML
- CSS
- Javascript
- Python
- Jinja

## Frameworks, Libraries, Websites & Programs Used

- [W3schools](https://www.w3schools.com/): This site provided many useful templates in their lessons.

- [Materialize](https://www.materializecss.com/): Very helpful framework for figuring out initial design.

    - Jquery: Provided helpful code for navbar.

- [FontAwesome](https://fontawesome.com/): Provided icons for certain features.

- [Photoshop](https://photoshop.com/en): This was used to design the site's wireframes and database schema. 

- [FontMeme](https://www.fontmeme.com/): This was used to design the logo. 

- [MongoDB](https://www.mongodb.com/): MongoDB is used to store the database. 

- [Heroku](https://www.heroku.com/): Heroku was used to deploy the website.

- [GitHub](https://github.com/): GitHub was used to code the program.
    - Dependencies
        - click==8.0.1
        - dnspython==2.1.0
        - Flask==2.0.1 
        - Flask-PyMongo==2.3.0
        - itsdangerous==2.0.1 
        - pymongo==3.12.0
        - Werkzeug==2.0.1


# Testing
W3C Markup Validator, W3C CSS Validator, and Pep8Online were used to test the code. 

- WSC Markup - [Link to site](https://validator.w3.org/)
    - get_films.html - <a href="static/img/validation/get_films.html - Nu Html Checker.pdf"> Results PDF </a>
    - login.html - <a href="static/img/validation/login.html - Nu Html Checker.pdf"> Results PDF </a>
    - register.html - <a href="static/img/validation/register.html - Nu Html Checker.pdf"> Results PDF </a>
- W3C CSS - [Link to site](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - style.css - <a href="static/img/validation/W3C CSS Validator (CSS level 3 + SVG).pdf">Results PDF </a>
- Python - [Link to site](http://pep8online.com/)
    - app. py
        - <a href="static/img/validation/PEP8 online check - Results.pdf">Results PDF </a>
        - <a href="static/img/validation/result_20210812_193900.txt">Results TXT </a>


## Testing User Stories

-   #### First Time User Goals

    1. As a First Time User, I want to easily locate different films, either by title or genre. 
        - Site landing page clear presents links to available films.
            - Site landing page functions properly on all screen sizes. Only room for improvment
            would be the scalability of the images. At certain points the images become slightly
            distorted. 
        - Search bar is available to both registered and unregistered users, as is
        the genre selector.
            - Search bar functions on all screen sizes and scales properly to fit both search/exit button
            and genre search bar below it. 
    2. As a First Time User, I want to easily find the recommendations for the films. 
        - Upon selection the site displays all available recommendation for the film in question.
            - Film information is present and scalable, any overflow is visible through scrolling. 
    3. As a First Time User, I would like the option to register for an account.  
        - Register tab is visible in navigation bar on all pages. 

-   #### Returning User Goals

    1. As a Returning User, I want to be able to login to my account.
        - Login tab is visible in navigation bar on all pages and incorrect username/passwords will alert the user
        that a mistake has been made.
    2. As a Returning User, I would like to add films to the site so that others might offer 
    reading suggestions based on my preferences. 
        - The landing page for logged-in users clearly displays an add film feature as the first of the available 
        film selection options. 
        - Also includes feature on film profile for user to edit or delete any films they may have made.
    3. As a Returning User, I would like to be able to upload my own book suggestions for certain films. 
        - Film profile offers users the oppurtunity to add their own recommendations. 
        - Likewise includes a feature to edit/delete book recommendations.



## Further Testing

- Tested using Chrome/Firefox/Safari.

- Tested on iPhone 7.

# Known Bugs / Potential Improvements

- Minor issues with scaling the images. 

- I'm still having trouble getting the different search functions to work. Ideally the search bar
results would focus on the film titles while the genre navbar results would focus on the genre film genres. At the moment both Search() and Genre_Search() query a shared text index made of both film titles and genres,
so if a user were to Search("Horror") it would also bring up all the films of that genre, while if they were to select
Genre_Search("Romance") it would also bring up all the films with the word "Romance" in the title.

- In the future I may experiment with the JSON/BSON dependencies to better handle the database information.

# Deployment 

## GitHub Cloning/Coding Environment

1. Log into GitHub.

2. Go to the project's repository.

3. To open it in GitPod simply click the green GitPod button and a new workspace will open. 

To Create your own copy:

4. On the menu bar, click "Settings" which will redirect you to a separate page.

3. Above the menu bar containing the "Settings" tab notice the three buttons to the right: "Unwatch", "Star", and "Fork".
Click the "Fork" button and refresh your browser. You will now have a copy of the repository in your own account.


## Heroku Deployment 

0. (Open project in GitHub.)

1. To deploy from Heroku first note down all neccesary dependencies the project requires to function. To do this create a requirements.txt file in the terminal with the command: pip freeze > requirements.txt

2. Create Procfile with the commmand echo web: python app.py > Procfile. This will let Heroku know it's going to run a python file. 

3. Push these files to GitHub then go to the Heroku site. 

4. Login and create a new app. 

5. Go to deploy and select github as the method. You will then be asked to link the heroku app to a repository. Select the name of project. 

6. Then go to settings > "reveal config vars" which is where you will store the environment variables which were not pushed to github.  
    - "IP": "0.0.0.0")
    - "PORT": "5000")
    - "SECRET_KEY": "mYt905thou1W")
    - "MONGO_URI": "mongodb+srv://pokemongoDB:Pikachu25@myfirstcluster.4i2hj.mongodb.net/readflix?retryWrites=true&w=majority"
    - "MONGO_DBNAME": "readflix")

7. Then go back to the deployment section of the app and click "deploy branch". 


# Credits

- Code
    - Code Institute (Task Manager Project)
        - The mini Task Manager assignment served as a helpful jumping off point for developing my code.

- Content
    - I developed the code myself however many of the film and book recommendations were provided
    by friends and family I had test the site. 

- Media
    - [FontMeme](https://fontmeme.com/permalink/210729/7c4f14820fc13e73ba00a7ff096daf55.png) This was used to create the site logo.
    - [Google Images](https://google.com): This was used by myself, and presumbably, the testers to find images for the
    film posters. 


- Acknowledgements
    - Thank you to FontMeme!
    - Thank you to Code Institute!