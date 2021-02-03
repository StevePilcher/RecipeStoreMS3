# The Recipe Store -  Milestone 3 Project

![Site Image](https://github.com/StevePilcher/RecipeStoreMS3/blob/master/static/images/site-image.png)


This project was created for my Milestone 3 project for the Code Institute's Full Stack Dev course. The project requirements were to build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain using HTML, CSS, JavaScript, Python+Flask and MongoDB.

The app I created is a single page site. I chose to create an online recipes store app which allows a user to be able to have an individual account for creating, editing and storing their own recipes. 

## Test User
To showcase the app, a test user has been created with multiple recipes. 

Sign in with these credentials;

Username: Steve

Password: ABC 

*The login details are case sensitive*

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

4. Signup redirect is not very user friendly, taking you back to the login page. An improvement should be signing up and being logged in to the create recipe page. 

5. Adding the ability to clone someone else's recipe to your own collection.

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
- iPad & iPad Pro

### Known Issues

- Masonary display effect can sometimes not render with larger gaps between grid items than desired. Especially when changing view dynamically to smaller screen sizes.

## Validators 

### W3C Markup Validator 

HTML was firstly parsed through Google chrome browser before running the HTML through W3C Validator. No Errors were found however warnings relating to headings were encountered on pages. This [Document](https://github.com/StevePilcher/RecipeStoreMS3/blob/master/static/files/RecipeStoreHTMLValidation.pdf) explains all of the warnings and reasons them to be ignored.

### W3C CSS Validator 

- No errors were found on style.css
- 1 warning was found referring to Imported style sheets that are not checked in direct input and file upload modes. It can be ignored 

### JSHint

- No errors were found after running JS through JShint

### PEP8online

- No errors were found after running python code through PEP8online. Result file can be found [here](https://github.com/StevePilcher/RecipeStoreMS3/blob/master/static/files/PEP8CheckCodeResults.txt)
 
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
    2. Form accepts and redirects to login page

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

To copy and deploy this project follow the 3 main platform steps below. 

### GitHub

This version was off of the master branch from GitHub [here](https://github.com/StevePilcher/RecipeStoreMS3), there are no differences between the deployed and deployment versions. 

#### Cloning this Project

If you have a GitHub account move to step 1. If not, firstly go to [GitHub](https://github.com/) and create an account. Verify as requested and now follow the below steps to clone this repository; 

1. Follow the [link](https://github.com/StevePilcher/RecipeStoreMS3)
2. Click the **'Use this template'** button
3. User will be redirected to a create repository from template page
4. Fill in the name of the repository you want to create
5. Choose public or private
6. Click the green **Create repository from template** button

### MongoDB

If you have a MongoDB account move to step 1. If not, firstly go to 
[MongoDB](https://www.mongodb.com/cloud/atlas/register) Now follow these steps to setup your DB with Mongo. 

1. Follow the link to login to [MongoDB](https://account.mongodb.com/account/login) 
    1. Click **Create** a Shared cluster for free
    2. By default AWS will be highlighted. Choose your closest region
    4. Next choose the M0 cluster tier. *This is Free forever* 
    5. Scroll to bottom and select the Cluster name, you can leave it default 
    6. Click **Create Cluster** button. *This can take some minutes*


2. Under securities, click **Database Access**
    1. Click **Add New Database User** 
    2. Enter a new **Username** and **Password**
    3. Set Database User priviledges to **Read and Write to any Database**, click accept

3. Under securities, click **Network Access**
    1. Click the **Add IP Address** button
    2. Select the option **Add access from anywhere** *this will populate the IP 0.0.0.0/0* and click **Confirm**

4. Under Data Stroage click **Clusters** 
    1. You Cluster should be provisioned, if not wait a few more mins. 
    2. Once provisioned, click the **collections** button
    3. Click the button **Add my own data** *This is where you create your recipe DB* 
    4. Add a name to your DB *eg MyRecipeDB*
    5. Add a name to your collection *eg Recipes* and **create**

5. Click the far right option heading **Command Line Tools** 
    1. Under the option **Connect to your Cluster** click the **Connect Instructions** button
    2. Choose **Connect your Applicaton** 
    3. Select the dropdown **Python** and the version **3.6 or higher**
    4. You will now have a the **MONGO_URI**, you will need this later when you deploy your app. To connect to your recipe DB remember, replace <password> with the password for the root user. Replace <dbname> with the name of the database that connections will use by default.

You are now ready to setup the 3rd and final part of deploying the Recipe store project.

### Heroku

This project was deployed using Heroku and can found [here](https://recipestoremongo.herokuapp.com/). 

#### Deploying to Heroku

To deploy the project on Heroku yourself, follow these steps. 

If you already have created an Heroku account move on to step 1, if not create an account by following this [link](https://signup.heroku.com/). Verify as requested and once complete, move on to step 1.

1. Login to your [Heroku](https://id.heroku.com/login) account
2. Click the button **New** , with further dropdown **create new app**
3. Create the app with a unique name and selecting the region, Europe or USA, click the **Create App** button
4. Click the **Deploy** tab 
5. The Deployment Method can be connected to GitHub. Click and follow the steps below to connect your new repository to Heroku. This will keep the deployed version updated with every commit to the branch in Github.  
6. Click the **Settings** tab
7. Scroll down and click **Reveal Config Vars** 
8. This settings menu allows you to set your secret keys and other sensitive info so it's hidden from public view
9. Config Vars should be entered for the following; 


| Key  | Value  |
|---|---|
| IP | 0.0.0.0 |
|PORT|8080|
|MONGO_DBNAME|*Your MongoDB Name that you created in step 4.iv of the MongoDB*|
|MONGO_URI|*Your MongoDB URI that you popluated and edited in step 5.iv of MongoDB*|
|secret_key|*Your Secret Key set in your env.py file*|

Your recipe app can now be launched by clicking the **Open App** button.


## Credits

- Fonts taken from [Google Fonts](https://fonts.google.com)

### Media

- Category Icons can be found at [Flat Icon](https://www.flaticon.com/)

### Acknowledgements
- Masonary CSS/JS layout forked and used from [GitHub](https://github.com/desandro/masonry) & Masonary Desandro website [Masonry](https://masonry.desandro.com/)
- Additional Flask learning from Pretty Printed's YouTube video 'Creating a User Login System Using Python, Flask and MongoDB [YouTube](https://www.youtube.com/watch?v=vVx1737auSE)
- I received inspiration for this project from [Pinterest](https://www.pinterest.co.uk/pilchy1983/developer-ideas/). 
- Code debugging help from my mentor Adegbenga Adeye
