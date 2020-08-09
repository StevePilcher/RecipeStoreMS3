# The Recipe Store -  Milestone 3 Project

![Site Image](https://github.com/StevePilcher/Stuck-in-the-mud-MS2/blob/master/assets/images/site-image.PNG)

This project was created for my Milestone 2 project for the Code Institute's Full Stack Dev course. The project requirements were to build a interactive frontend website using HTML, CSS and Javascript. 

The website I created is a single page site that is designed for desktop. I chose to make this site to showcase Javascript as a traditional dice playing game called stuck in the mud. 

## UX
 
The UX is a simple single page with areas cleary defined. The player scores are left and right with the dice being rolled and displayed in the centre of the page. The user transitions through the game by using 2 simple buttons and is signposted with modal popups when significant moments in the game occur. Active classes are added when the player turn switches between players to help identify who is active at each given round of the game.


### Typical User Stories

**New Players**

- Players arrive at the site and on loading get a welcome message and an instruction that they need to click new game to be able to start playing.

- Once the new game button is clicked the rules of the game popup as a modal. The rules are set out clearly for the new player to understand and start playing.


### Wireframe

The linked file to the wireframe mockup of the website.

[Wireframe PDF](https://github.com/StevePilcher/Stuck-in-the-mud-MS2/blob/master/assets/WireframeMS2.pdf)


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
- Bootstrap (with integrated Javascript)
- JQUERY (for easier DOM manipulation)

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