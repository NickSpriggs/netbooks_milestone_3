# Milestone Front-End Game Project

The following project was my attempt to create an online memory game with the tools provided to me in the first two modules of the Code Institute course. 
This project makes use of HTML, CSS, and Javascript.

[View live project](https://readflix.herokuapp.com/)

# UX

My goal for this project was to creaet a simply but fun game that could engage the player. It was my hope that the game would not only
strengthen the users memory and attention but also provide them with entertainment. Specifically my goals were to:
- Create a menu with instructions that allow the user to quickly learn the rules of the game.
- Have a gameplay area separate from the main menu to get engage them undistracted.
- Have a results screen that shows how well they performed.

* The the rules of the game are as follows. The user watches a series of tanks move across a 10 by 10 grid. After they finish their first run through the player has ten seconds to place mines in the paths that they remember.
Ideally the paths will intersect, forcing the user to try and remember where the was so that they can eliminate the most number of tanks with the fewest number of mines.  


## User Stories

-   #### First Time User Goals

    1. As a First Time User, I want to easily find different information about how exactly the game is played.
    2. As a First Time User, I reasonable control over the difficulty.
    3. As a First Time User, I would like to know how well I've down.    

-   #### Returning User Goals

    1. As a Returning User, I want to comfortably access more difficult stages of the game.
    2. As a Returning User, I want to be able to play without needing to review the rules.

## Wireframes:
<img src="static/img/wireframes/Landing Page.png">
<img src="static/img/wireframes/Poster Click [Logged In].png">
<img src="static/img/wireframes/Login:Register Page.png">
<img src="static/img/wireframes/Landing Page [Logged In].png">
<img src="static/img/wireframes/Add Poster:Film [Logged In].png">
<img src="static/img/wireframes/Poster Add Rec [Logged In].png">


# Features

- Mobile, desktop, and tablet scalable.

- Elements react to user decisions.

# Technology Used

## Languages

- HTML
- CSS
- Javascript
- Python
- Jinja (Spelling?)

## Frameworks, Libraries, Websites & Programs Used

- [W3schools](https://www.w3schools.com/): This site provided many useful templates in their lessons.

- [Photoshop](https://photoshop.com/en): This was used to design the games logo, assets, and even wireframes. 

- [GitHub](https://github.com/): GitHub was used to launch the program.



# Testing
W3C Markup Validator, W3C CSS Validator, and JSHint were used to test the code. 

- WSC Markup - [Link to site](https://validator.w3.org/)
    - Index.html - <a href="assets/PDF/validation-HTML.pdf"> Results PDF </a>
- W3C CSS - [Link to site](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Stylesheet.css - <a href="assets/PDF/validation-CSS.pdf">Results PDF </a>
- JSHint - [Link to site](https://jshint.com/)


## Testing User Stories

-  #### First Time User Goals

    1. As a First Time User, I want to easily find different information about how exactly the game is played.
        - Landing page has a menu with instructions on how to play.
    2. As a First Time User, I reasonable control over the difficulty.
        - All users are prompted to select the level of diffuclty they would like to play on.
    3. As a First Time User, I would like to know how well I've down.  
        - Every game ends with alert telling the user how the performed. In addition, the game also provides live updates on what is happening as you play.


## Further Testing

- Tested using Chrome, Firefox, and Safari.

# Known Bugs

- On some devices the game board scales awkwardly which can negatively impact the user's experience and performance.

- The tanks do not always spawn randomly and occasionally the same one or two rows will be ones utilized. This can make gameplay unchallenging.

# Deployment

I deployed the project on GitHub using the application GitHub Pages. The steps to do so were as follows:
1.  Log into GitHub. 
2.  Go to the project's repository and on the menu bar and click "Settings" which will redirect you to a separate page.
3.  Scroll down unti you find "GitHub Pages".
4.  Under source change the dropdown menu from "None" to "Main". Then click "Save"

In order to make a clone follow the previous section up to step #2:
1.  Above the menu bar containing the "Settings" tab notice the three buttons to the right: "Unwatch", "Star", and "Fork".
2.  Click the "Fork" button and refresh your browser. You will now have a copy of the repository in your own account.

# Credits

- Content
    - Developer wrote all the text.

- Media
    - [BestWallpapers](https://besthqwallpapers.com/textures/summer-camouflage-texture-dark-green-camouflage-texture-dark-green-camouflage-background-camouflage-texture-138419) This was used to create the camoflouge background.

    - [iStockPhoto](https://www.istockphoto.com/vector/top-view-of-the-city-with-a-desert-gm922427730-253211217): This was were I obtained the game space background.

    - [OpenGameArt](https://opengameart.org/content/top-down-painted-tanks): Provided the assets I used to make the tanks.    

    - [DeviantArt](deviantart.com/toraiinxamikaze/art/Halo-Reach-Landmine-243453712): Provided the landmines.

    - [NeedPix](needpix.com/photo/950289/comic-blast-blast-effect-explosion-effect-comic-blast-effect-comic-explosion-effect-boom-bang-cartoon): Provided the explosion effects.

    - [ClipartKey](clipartkey.com/view/ombTxT_popart-cartoon-comicbook-crash-textstickers-text-onomatopoeia-crash/.png): Provided the crash effects.

- Acknowledgements
    - Thank you to those mentioned in the media section; iStockPhoto, OpenGameArt, BestWallpapers, NeedPix, and ClipartKey.
    - Thank you to Code Institute!