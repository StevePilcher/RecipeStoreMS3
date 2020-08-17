# The Recipe Store -  Milestone 3 Project

![Site Image](https://github.com/StevePilcher/RecipeStoreMS3/blob/master/static/images/site-image.png)


This project was created for my Milestone 3 project for the Code Institute's Full Stack Dev course. The project requirements were to build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain using HTML, CSS, JavaScript, Python+Flask and MongoDB.

The app I created is a single page site. I chose to create an online recipe sapp which allows a user to be able to have an individual account for creating, editing and storing recipes.  

## Test User 
To showcase the app, a test user has been created with multiple recipes. Sign in these credentials;

Username: Steve
Password: ABC 

## UX
 
The UX is a simple single page. A standard navbar which concatenates to a burger icon when in mobile view allows users to recognise the simple nav structure. The 'log in' & 'Sign Up' buttons are only visible when the user isn't logged in, otherwise a 'Log Out' button replaces them. The recipes are displayed in a masonary pattern across the page when screen width allows once retrieved from MongoDB.

Simple form structures clearly identify input fields for the user to create any recipes. 

### Typical User Stories

**New Chefs**

- Aspiring cooks arrive at the site and will be welcomed with the login screen. This login form also has a note for non registered users to 'sign up!' by clicking the link. 

- Once the new cook has signed up, because they are yet to have created a recipe to view they will be taken to the create recipe page. 

- The create recipe page is a simple form where all of the required fields have a heading explaining what is required to be entered. Once all of the data has been entered the user clicks the save button, which is also recognisable by the disk icon. The new recipe is saved and user redirected to all of their recipes which are saved.

- The log out button logs the user out of the session and redirects to a login screen.

**Existing Chefs**

- Existing chefs arrive at the site and will be welcomed with a login screen. 

- Once they have logged in the navbar includes 'create recipe' and 'search categories', they auto redirect to all of their saved recipes.  

- The user can scroll down their list of recipes and click on the edit icon attached to each recipe. This click redirects and populates the 'create recipe' form with the desired recipe alreay filled in for editing. The user can then edit and resave with the save button. 

- Alternitavely the user can click the bin icon to delete the recipe from their collection.

- The user can search for all recipes listed in under a certain category by clicking on the 'search categories' link from the navbar. This redirects the user to a page with 6 buttons, each identified for a recipe category. Once clicked the user retrieves all recipes within thier own collection with the same category.

- The log out button logs the user out of the session and redirects to a login screen.

### Wireframe

The linked file to the wireframe mockup of the website.

[Wireframe PDF](https://github.com/StevePilcher/RecipeStoreMS3/blob/master/static/files/WireFrameMS3.pdf) 


## Features

### Existing Features
1. Main Page - Landing page with immediate login in form. Links in the nav bar for 'sign up' and 'log in' 

2. My Recipes - Displays a list of all user recipes saved in their collection, allows for editing and deletion of individual recipes.

3. Create Recipe -  A simple form to create individual recipes and save to their colleciton. 

4. Search Categories -  6 buttons that once the user is logged in will return all the recipes associated with that user and category.

5. Log Out - Log out button logs the user out of the session. 

### Features Left to Implement

1. Keyword search - Search bar that allows for individual recipes to be searched with any keyword rather than by category. Potential across all users recipes depending on GDPR. 

2. Images attachments - all image attachments to be store with recipes. 

3. Improved editing recipe features when in smaller screen sizes. Breadcrumbing each field as it's edited would be a better UX. This would require a complete overhaul of the current form submission function. 

## Technologies Used

The following technologies were used;

- HTML5 
- CSS3
- Materialize (with integrated Javascript)
- JQUERY (for easier DOM manipulation)
- Python+Flask
- MongoDB

## Testing

### Web Browser Testing

The following Web Browsers were tested and no errors found;

- Mozilla FireFox Version 79.0
- Google Chrome Version 84.0.4147.105
- Microsoft Internet Explorer 11.329.19041.0 
- Microsoft Edge 44.19041.1.0

### Mobile Device 

Chrome Dev tools were used to simulate the following devices for testing;

- iPhone X 
- Pixel 2 & 2XL
- Samsung S10 Plus 
- Samsung Galaxy Tab (Portrait)
- iPad 

### Known Issues

- Masonary display effect can sometimes not render correctly and does not leave a gap between recipes. Especially when changing from desktop view to smaller screen sizes. 

## Validators 

### W3C Markup Validator 

- 3 Warnings, 2 for lack of heading element used on sections (I feel headings are not required for UX), 1 for an h1 being used. 

### W3C CSS Validator 

- No errors or warnings were found on style.css
- 1 error associated with Materialize's minified css

### JSHint

- No errors were found after running JS through JShint
 
## Testing Scenarios

The following scenarios were manually tested;

1. App Loading/Login page:
    1. App Loads
    2. Attempt to click 'login' button before entering neither or 1 of the inputs
    3. 'Please fill in this field' appears below input field

2. App Loading/Login page:
    1. Attempt login with new user account
    2. Page returns red error text under the input 'Username does not exist'
    
3. App Loading/Login page:
    1. User clicks either 'sign up' button or 'Sign up here!' link
    2. User redirects to sign up page

4. Sign up page:
    1. Page Loads
    2. Attempt to click 'sign up' button before entering neither or 1 of the inputs
    3. 'Please fill in this field' appears below input field not fille in

5. Sign up page:
    1. User signs up an existing username. 
    2. Page returns red error text under the input 'The username already exists'
    
6. Sign up page:
    1. User signs up with unique username and password 
    2. Form accepts and redirects to my recipes page

7. User log out:
    1. On successful login.
    2. Nav bar now displays 'log out' button on all pages
    3. User clicks 'log out' button
    4. User is logged out and redirected to login page

8. Create Recipe:
    1. Logged in user clicks link 'Create Recipe' 
    2. Page redirects to Create Recipe form
    3. Dropdown field 'Category Select' populates with MongoDB categories
    4. Fields 'Recipe Name, Ingredients, Prep and Cook Instructions' highlight when clicked on
    5. Dropdown fields 'Prep & Cook Time' populate with list of timing options

9. Create Recipe:
    1. Attempt to submit without all of the fields selected
    2. 'Please fill in this field' flashes up for inputs that are required

10. Create Recipe:
    1. User fills in all of the required inputs
    2. User clicks submit 
    3. Recipe is inserted to MongoDB under that username
    4. Page redirects to disply all saved recipes 
    
11. Edit Recipe:
    1. From the My Recipes page, user scrolls to individual recipe and clicks edit icon
    2. Page redirects to the pre-filled in create form with requested recipe displayed for editing
    3. User edits any or all of the fields
    4. User clicks the form submit button
    5. On submission, user gets redirected back to all recipes with the updated recipe displayed. 

12. Edit Recipe:
    1. User tries to resubmit the recipe with blank fields 
    2. 'Please fill in this field' flashes up to stop blank submission

13. Search Category:
    1. User clicks on the search category nav link 
    2. Redirects to the search page
    3. 6 buttons representing each category are displayed
    4. User clicks on a button and page refreshes with any recipes the user owns in the particular category
    5. User clicks an alternate category button and page refreshes with new recipes. 

## Deployment

This project was deployed using Heroku and can found [here](https://recipestoremongo.herokuapp.com/). This version was off of the master branch from GitHub [here](https://github.com/StevePilcher/RecipeStoreMS3), there are no differences between the deployed and deployment versions. 

## Credits

- Fonts taken from [Google Fonts](https://fonts.google.com)

### Media

- Category Icons can be found at [Flat Icon](https://www.flaticon.com/)

### Acknowledgements
- Masonary CSS/JS layout copied from AndyBareFoot on [CodePen](https://codepen.io/andybarefoot/pen/QMeZda)
- Additional Flask learning from Pretty Printed's YouTube video 'Creating a User Login System Using Python, Flask and MongoDB [YouTube](https://www.youtube.com/watch?v=vVx1737auSE)
- I received inspiration for this project from [Pinterest](https://www.pinterest.co.uk/pilchy1983/developer-ideas/). 
- Code debugging help from my mentor Adegbenga Adeye
