# The Recipe Store -  Milestone 3 Project

![Site Image](https://github.com/StevePilcher/RecipeStoreMS3/blob/master/static/images/site-image.PNG)


This project was created for my Milestone 3 project for the Code Institute's Full Stack Dev course. The project requirements were to build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain using HTML, CSS, JavaScript, Python+Flask and MongoDB.

The webapp I created is a single page site. I chose to create an online recipe site which allows a user to be able to have an individual account for creating, editing and storing recipes.  

## UX
 
The UX is a simple single page. A standard navbar which concatenates to a burger icon when in mobile view allows users to recognise the simple nav structure. The 'log in' & 'Sign Up' buttons are only visible when the user isn't logged in, otherwise a 'Log Out' button replaces them. The recipes are displayed vertically down the centre of the site once retrieved from MongoDB. 

### Typical User Stories

**New Cooks**

- Aspiring cooks arrive at the site and will be welcomed with the login screen. This login form also has a note for non registered users to 'sign up!' by clicking the link. 

- Once the new cook has signed up, because they are yet to have created a recipe to view they will be taken to the create recipe page. 

- The create recipe page is a simple form where all of the required fields have a heading explaining what is required to be entered. Once all of the data has been entered the user clicks the save button, which is also recognisable by the disk icon. 

**Existing Cooks**



### Wireframe

The linked file to the wireframe mockup of the website.

[Wireframe PDF](https://github.com/StevePilcher/RecipeStoreMS2/blob/master/assets/WireframeMS3.pdf) 


## Features

### Existing Features
1. Main Page - The main landing welcomes the user with a popup message and a simple instruction on how to get started.  

2. Rules - The rules popup as soon as the 'New Game' button is pressed. This allows the players who haven't played the game before to simply read the short list of rules and start playing. 

3. Buttons - The game is controlled by 2 buttons. The 'New Game' button and the 'Roll' button. The roll button disables before and after a new game is pressed to stop the game. 

4. Active Player - Once the game is initiated the active player will have a highlighted background clearly identifying who is playing at that given roll. 

### Features Left to Implement

1. Historical win count for each player. Allowing them to see who won the last X number of games. 

2. Audio added to the roll, stuck and win states of the game. This would give more interactivity. 


## Technologies Used

The following technologies were used;

- HTML5 
- CSS3
- Bulma (with integrated Javascript)
- JQUERY (for easier DOM manipulation)
- Python+Flask
- MongoDB

## Testing

### Web Browser Testing

The following Web Browsers were tested and no errors found;

- Mozilla FireFox Version 77.0
- Google Chrome Version 83.0.4103.97 
- Microsoft Internet Explorer 11.836.18362.0 
- Microsoft Edge 44.18362.449.0

### Mobile Device 

Chrome Dev tools were used to simulate the following devices for testing;

- iPhone X 
- Pixel 2 & 2XL
- Samsung S10 Plus 
- Samsung Galaxy Tab (Portrait)
- iPad (Portrait) 
- 
### Known Issues

- Stuck modal appears after game has been won.
- Page header font does not display correctly on IE 11.

## Validators 

### W3C Markup Validator 

- 1 warning was found on index.html for an empty header, this can be ignored as it JQuery inserts a winner to the element when the game is won.  


### W3C CSS Validator 

- No errors or warnings were found on style.css

### JSHint

- No errors were found after running JS through JShint
 
## Testing Scenarios

The following scenarios were manually tested;

1. Page Load:
    1. Welcome popup message occurs on all browser types.
    2. User clicks to close pop up.
    
2. Roll Button is disabled:
    1. Load page. 
    2. Close welcome message.
    3. Roll button is disabled and greyed out. 
    4. New game button enables the roll but functionality. 
    5. Game concludes with a winner.
    6. Roll button disables on winner and game cannot continue.
    7. User can only press New game button to start again.

3. Clicking on elements:
    1. Clicking on elements other than the enabled buttons.
    2. No unwanted bugs or actions occur.


A further 3 people tested the game on thier own devices and reported no bugs or issues.

## Deployment

This project was deployed using GitHub pages can found [here](https://stevepilcher.github.io/Stuck-in-the-mud-MS2/). This version was off of the master branch, there are no differences between the deployed and deployment versions. 

## Credits
- Fonts taken from [Google Fonts](https://fonts.google.com) and [DaFont](https://www.dafont.com/run-to-the-hills.font)
- Dice images from [WP ClipArt](https://www.wpclipart.com)
- Pig Image from [TOP PNG](https://toppng.com)

### Media
- Background image by Photo by Riho Kroll found on [Unsplash](https://unsplash.com) 
- Dice images found on  

### Acknowledgements
- Additional Javascript learning from Jonas Schmedtmann's course The Complete JavaScript Course 2020 on Udemy.com [Udemy](https://www.udemy.com/course/the-complete-javascript-course/)
- I received inspiration for this project from [Pinterest](https://www.pinterest.co.uk/pilchy1983/developer-ideas/). 
- Code debugging help from my mentor Adegbenga Adeye