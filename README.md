# Milestone Back-End Project

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
    - Only allow the user who created the film/recommendation OR admin to update
    or delete them from the database. [The admin login is Username: admin / Password: bookmark]

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

## Wireframes:
<img src="static/img/wireframes/Landing Page.png">
<img src="static/img/wireframes/Poster Click [Logged In].png">
<img src="static/img/wireframes/Login:Register Page.png">
<img src="static/img/wireframes/Landing Page [Logged In].png">
<img src="static/img/wireframes/Add Poster:Film [Logged In].png">
<img src="static/img/wireframes/Poster Add Rec [Logged In].png">


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

- [Photoshop](https://photoshop.com/en): This was used to design the site's wireframes. 

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
W3C Markup Validator, W3C CSS Validator, and JSHint were used to test the code. 

- WSC Markup - [Link to site](https://validator.w3.org/)
    - get_films.html - <a href=""> Results PDF </a>
    - login.html - <a href=""> Results PDF </a>
    - register.html - <a href=""> Results PDF </a>
    - base_templates.html - <a href=""> Results PDF </a>
- W3C CSS - [Link to site](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - style.css - <a href="">Results PDF </a>
- JSHint - [Link to site](https://jshint.com/)

## Testing User Stories

-   #### First Time User Goals

    1. As a First Time User, I want to easily locate different films, either by title or genre. 
        - Site landing page clear presents links to available films.
        - Search bar is available to both registered and unregistered users, as is
        the genre selector.
    2. As a First Time User, I want to easily find the recommendations for the films. 
        - Upon selection the site displays all available recommendation for the film in question.
    3. As a First Time User, I would like the option to register for an account.  
        - Register tab is visible in navigation bar on all pages. 

-   #### Returning User Goals

    1. As a Returning User, I want to be able to login to my account.
        - Login tab is visible in navigation bar on all pages and incorrect username/passwords will alert the user
        that a mistake has been made.
    2. As a Returning User, I would like to add films to the site so that others might offer 
    reading suggestions based on my preferences. 
        - The landing page for logged-in users clearly displays and add film feature as the first of the available 
        film selection options. 
        - Also includes feature for user to edit or delete any films they may have made.
    3. As a Returning User, I would like to be able to upload my own book suggestions for certain films. 
        - Film profile offers users the oppurtunity to add their own recommendations. 
        - Likewise includes a feature to edit/delete book recommendations.



## Further Testing

- Tested using Chrome/Firefox/Safari.

- Tested on iPhone 7.

# Known Bugs / Potential Improvements
- Minor issues with scaling the images. 

- In the future I may experiment with the JSON/BSON dependencies to better handle the database information.

# Deployment
 X 


# Credits

- Code
    - Code Institute (Task Manager Project)
        - The mini Task Manager assignment served as a helpful jumping off point for developing my code.

- Content
    - I developed the code myself however many of the film and book recommendations were provided
    by friends and family I had test the site. 

- Media
    - [FontMeme](https://fontmeme.com/permalink/210729/7c4f14820fc13e73ba00a7ff096daf55.png) This was used to create the site logo.


- Acknowledgements
    - Thank you to FontMeme!
    - Thank you to Code Institute!