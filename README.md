# Refreshing Edible Cuisine In Portable External Support
 

[Deployment on Heroku](https://ms4recipes.herokuapp.com/)

I plan to design and build, a collection of information that Users can contribute and share with the wider community.  I plan to use the information learnt in Flask, Python and using MongoDB.

I also plan to try and promote Cooking Tools.
 
## UX

I want to create something that is consistant, but is easily browseable.  I plan to have a central page, that links to other features.

It would need to provide the following features:-

1. Somewhere to View all the recipes in the collection
2. Somewhere to Add Recipes
3. A Search feature
4. Someway for a User to Edit or Delete their own Recipes

Following on from the previous lessons, I have continued to use Materlize.  This should speed up the creating side of things.

### Users Stories

| User      | Story                                                                         |
| :--------:|-------------------------------------------------------------------------------|
| FIRST     | I want to be able to Search for different recipes, that are in the collection.|
| SECOND    | I want to be able to add my own recipes.                                      |
| THIRD     | I want to be able to edit and remove my own recipes.                          |

Deployment Diagram - 

![alt text](/static/images/deploymentdiagram.png "Deployment Diagram")

Index Wireframe - 

![alt text](/static/images/indexwireframe.png "Index Wireframe")

This is what I started with and then I just changed it to suit what my ability was.

## Features

The website, allows you to browse on a Desktop, Tablet or Mobile Device with various changes in the way the website appears.  Ie the Navbar shrinks when on smaller devices.  There is a central picture so that it appears on each screen, to bring consistency to the User so they arnt surprised by anything.  Below the image there is the Title of the Page.

The content below each title will change according to the other pages.  However the look of the content will be consistant using CSS.

On the Index Page,
There is a feature to let the user search for a recipe, then below that there is a feature to allow the user to login and edit their own recipes.

Below the search and login elements there are recipe cards for people to browse.

At the bottom of the page, is the Footer where some information is there about myself. 


### Existing Features
On the Index page is a list of all the recipes are displayed in order of how many views each recipe has had.

Each recipe can be clicked on to view the full recipe as a single recipe. 

### Features Left to Implement
- Better search feature, instead of searching everything in the Collection
- Auto complete in the Search feature to make it more user friendly
- Quick searches IE Easy, Medium, Hard or by Breakfast, Lunch, Evening, Dessert, Baking
- The more recipes there are the longer it would take to load, so maybe add some form of pagination.  This is to limit what is seen and used on resources by the system.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

| Technology      | How it was used                                                 | Website                                            |
| :--------------:|-----------------------------------------------------------------|---------------------------------------------------:|
| HTML            | Backbone of everything                                          | https://www.w3schools.com/html/default.asp         |
| CSS             | Styling for the MATERLIZE to work on                            | https://www.w3schools.com/css/default.asp          |
| MATERLIZE       | A modern responsive front-end framework based on Material Design| https://materializecss.com/                        |
| JAVASCRIPT      | Used for some functionality on the website                      | https://www.w3schools.com/js/default.asp           |
| PYTHON          | Used for the main functionality on the website                  | https://www.w3schools.com/python/default.asp       |
| PYMONGO         | Interaction for Python and Mongo                                | https://www.w3schools.com/python/python.asp        |
| MONGO           | Non-Relational Database                                         | https://cloudmongo.com                             |
| FLASK           | Microframework                                                  | https://en.wikipedia.org/wiki/Flask_(web_framework)|
| HEROKU          | Cloud Platform to Host the Flask App                            | https://id.heroku.com/login                        |
| GITHUB          | Stores my work so that other people and myself can reference it | https://www.github.com                             |
| GITPOD          | An IDE allowing me to code on any browser                       | https://www.gitpod.io                              |
| VSCODE          | An IDE allowing me to code on my computer                       | https://code.visualstudio.com/                     |
| SLACK           | An chat application to allow others to communicate              | https://slack.com/intl/en-gb/                      |


Recipe Table in Mongo

| Field        | Type       | Properties - All are Required                                         |
| :-----------:|------------|----------------------------------------------------------------------:|
| recipe_name  | Autonumber | Unique                                                                |
| author       | String     |                                                                       |
| recipe_image | String     | Has to be a string as an image cannot be stored when using Heroku     |
| meal_type    | String     | Gets the values from a mealtype table                                 |
| difficulty   | String     | Gets the values from a difficulty table                               |
| healthy      | String     |                                                                       |
| prep_time    | Integer    |                                                                       |
| cooking_time | Integer    |                                                                       |
| serves       | Integer    |                                                                       |
| description  | String     |                                                                       |
| notes        | String     |                                                                       |
| ingredients  | String     |                                                                       |
| method       | String     |                                                                       |
| email        | String     |                                                                       |
| views        | Integer    | Cannot be edited by User                                              |


## Testing

#### Test

### Purpose
Added a recipe without an image, for the purpose of seeing if a default image can be shown.
### Result
The default image works, I then edited it so that the actual Curry Picture was shown.

***

##### Purpose
To see if a users email would match up with the email stored in their recipe.
##### Method
Typed in jjackson19862017@gmail.com in the search field on the detailsrecipe.html
##### Outcome
Fails
##### Fix
Researching into PyMongo website and Slack.

***

##### Purpose
To see if a user could click on a recipe card instead of just the 'view' link.
##### Method
Clicked on the image of the recipe
##### Outcome
Went to details of the recipe - Expected

***

##### Purpose
To see if a user could search for their recipes
##### Method
Typed in jjackson19862017@gmail.com in the search field on the index.html
##### Outcome
It finds everything - Not Expected
##### Fix
I have now changed the find feature in the App.py, it now finds if the email address is there.

***

##### Purpose
To see if a user could search for their recipes
##### Method
Typed in jjackson19862017@gmail.com in the search field on the index.html
##### Outcome
Took me to the usersrecipe.html - Expected

***

##### Purpose
To see if a user could delete their recipes
##### Method
Clicked on "Delete Recipe"
##### Outcome
Error - Previously I tried to have an if statement with the condition, if the two emails matched then it would delete the recipe.
##### Fix
However I changed the way I was checking and so I just replaced this with my original delete code using Github History.

#### Device Testing

The site works on the following devices:
- Huawei P20 Pro running Chrome
- 13" Macbook Pro
- Pixel 2 (Emulated using Chrome Dev Tools)
- iPhone X (Emulated using Chrome Dev Tools)
- iPad (Emulated using Chrome Dev Tools)
- iPad Pro (Emulated using Chrome Dev Tools)

The site works in the following broswers:
- Chrome
- Firefox
- Safari

#### Code Testing

- HTML - This was attempted using https://validator.w3.org/, however because of the Flask language it couldnt understand that the HTML works.

- CSS - This was attempted using https://jigsaw.w3.org/css-validator/validator, however it gave out errors for the code provided my Materlize for customising its forms.

It also threw some warnings for my CSS, because of repeat values.

## Deployment

The application was started on GITPOD. I then found out how to customise my VSCode Application so that I could code on my MacBook without the internet.

I pushed my work to GITHUB https://github.com/jjackson19862017/Milestone4_Recipes

The application was deployed from GITHUB to Heroku at http://ms4recipes.herokuapp.com/

My database is stored on MongoDB and is setup within Heroku.

## Credits

I would like to thank, 
- Aaron (mentor at code insitutite) for making sense out of it and giving me the pushes I needed.
- Kitty from Slack for always providing help when I needed it, she doesnt even know me either.  Which I think is great. 
- Sam for giving my site a once over and thinking of some good improvements.
- YouTube, for various videos.  Some panned out, and someothers didn't
- Slack Community

### Media
The main image used is from https://www.forksoverknives.com/plant-based-primer-beginners-guide-starting-plant-based-diet/#gs.w27a6h

The images and recipes that I used were from the https://www.bbcgoodfood.com/

### Acknowledgements

Due to being marked down on my previous project, I tried to make an effort with the write up this time.

The Readme finishes here, however if you wish to proceed beyond this point this is my diary to show you how I achieve my project.


# Timeline

## Tuesday 4th Feb 2020,

### Setup

Picked which project I would like to do, I chose the Recipe Project.
I have created my website structure from my initial clone of the Code Institute Full Template.
This includes folder and file structure.
I decided to do this as my initial setup as I am trying to make best use of my time.

### Inserting Content Block

Just inserted the Content Block code to all templates except base.html

### Update app.py and base.html

Added MongoDB connection code to app.py
Added test code to base.html so I could see if my connection worked.

### Created Procfile and Requirements.txt

This allows flask to run in Heroku.

## Wednesday 5th Feb 2020,

### Securing my IDE

After a chat with my mentor, I have decided to secure my chosen IDE which is VSCode.  I have failed to do this in previous tasks, however I have fixed that issue now. :)

I used the "sudo pip3 install -r requirements.txt", to install all requirements to my Macbook.

I then had a problem because my enviroment secret codes weren't being read, so I created a file and used gitignore.  This prevents the file from being uploaded to GitHub.

I have just confirmed that this works.

### File Structure Cleanup

I have just deleted some files that I thought I might.

My first thought was to setup a user login space so people could login and create recipes, and edit or delete their recipes.  This would stop other users from deleting other users recipes.

However I have thought of a different view, with the input of my mentor.  I am going to use a users email address to validate them.

For example when a user creates a recipe, a field that would be required would ask them for their email address.  This wouldn't be seen by other users and is only known to them.  This would be needed to either edit or delete a recipe that they contribute to the site.

### Created NavBar and Theme Colors

I have updated base.html with Materialize's NavBar and Customize Options.

I have gone for a Navbar that displays the Logo on the left with Links on the right-hand side.

I have also gone for a pull out side bar for mobile devices.

I have chosen a theme of blue.  The Navbar itself is Dark Blue, and the text is a lighter blue.

For the main content on the page, I will reverse this.

### Added Image Card

I added an Image Card to the index.html, the image was taken from https://www.forksoverknives.com/plant-based-primer-beginners-guide-starting-plant-based-diet/#gs.w27a6h

I modified the image so that the white card text could be seen more clearer.

### Updated Image Card

I added a bit of content to introduce people and what the purpose of the site is for.

### Added Footer to base.html

I added a footer just to round off the site.  I also removed the about link in the Navbar due to the information being accessible in the footer.

## Thursday 6th Feb 2020,

### Created Add Recipe Form

I have put together a form that can take input, from a user.  I haven't setup the actual form submit yet.

### Add Recipe Form Styling

I changed the default colours, to something that would match my colour theme.

## Friday 7th Feburary 2020,

### Fixed Mongo Reading Error

The Mongo Collection Recipes was failing to show in the recipes.html, after finding the problem in the beginning For Loop.  
Problem was fixed.

### Maintaining Consistancy

I decided, to change my original idea.  Originally I decided that having a different page after the index page would look nice however, I found that adding the page_title to app.py.  I could consistantly have a image at the top of each page and just have the wording change.  Personnally I don't like having a picture at the top of each page.  However from a User Experience, its more pleasing on the eye.

### Added Add Recipe Functionality

Connected the sumbit button on addrecipe.html to MongoDB

Also added a few extra fields, that could be used in the future as possible search parameters.

### Added Toast and Recipes.html Basic Styling

Added a Toast function to the submit button, on addrecipe.html.  This is to give feedback to the user.

Modified the Recipes in the recipes.html to appear in a seperate Materialize Card, will style properly later down the line after all functionality to the site is complete.

### Added Edit Recipe Function

Added the Edit Recipe Function to editrecipe.html, also updated the toast to say edited instead of add.

Had to modify my MongoDB, with two extra collections. Meal_Type and Difficulty, so that the for loop would work in the editrecipes file.

### Added Comments to HTML code

Added some comments to the html pages to make it a little easier to see what does what.

Also changed the slider for healthy, into a drop down list.

### Changed Side Nav

I decided to make the Side Navigation Bar, more appealing to the user on mobile devices.

### Added Code Comments, Block Header

I started by trying to enable the user to upload an image to the MongoDB.  I researched it using Youtube, however after two hours of trying it wouldn't work.  It looks like the image in the form field wasn't being put into the recipes collection.

I tried to research the issue on slack, and found out that in deploying to heroku this is something that isn't supported.

So I have added comments to my html's instead.

I have also introduced a Header Block to clean up my code instead of relying on one Content Block

### Added Delete Recipe Function

Added Delete Recipe Function to recipes.html and app.py.

I will add a function to validate user in the future.

### Changed Nav Title and removed Hello from index.html

Quick change


## Saturday 8th Feburary 2020,

### Added Recipe Image Field, and updated recipes.html

Added recipe_image to the
- recipes.html
- addrecipe.html
- editrecipe.html

Also added a default image to the addrecipe.html just incase other people dont have an image for the recipes they are adding.

Also updated recipes.html recipe cards.

#### First User Test

### Purpose
Added a recipe without an image, for the purpose of seeing if a default image can be shown.

### Result
The default image works, I then edited it so that the actual Curry Picture was shown.

### Changed Recipe Cards

Changed it to an horizontal card style from an action reveal card.


## Sunday 9th Feburary 2020,

### Updated App.py

Added comments to app.py, to make decorators easier to understand there function.

Also removed the 'insert_recipe' decorator as this is no longer required.  This was originally added as I was watching the original code institute videos for building a task_manager and that was involved in the steps.

On the website itself I used the add recipe function to insert a few recipes, so that I could work on the search function.
This could be seen as a second test to make sure different 'meal_types', 'difficultys' were working as should do.

Updated Readme file.

## Monday 10th Feburary 2020,

### Updated index.html

I have moved the recipes.html to index.html so I can get rid of the recipes.html and change it to a detailsrecipe.html.  I have changed the app.py to reflect this.

The purpose of this is to show people the most viewed recipes, and then they can either click on them, or search for them.  This will then send them to a more detailed page.

## Tuesday 11th Feburary 2020,

### Improved Index.html Appearance to User

I have been experimenting with what I liked the best.

The problem was that the paragraphs I had used under the CARD IMAGE or HEADER for each page wasn't showing the full text.  So in the end I just seperated the CARD IMAGE and created a BASIC CARD.

I have added custom CSS code, modified the base.html and all the other pages in regards to the HEADER BLOCK.

I also re inserted the 'insert_recipe' decorator as the 'addrecipe.html' wouldn't load

### Customizing AddRecipe and EditRecipe Form

I have added CSS Styles and Validation and Limits to the AddRecipe and EditRecipe Forms

## Thursday 13th Feburary 2020,

### Listing Ingredients

I have now made the Ingredients store as a visit in Mongo

### Made Recipes Details Page

Made the Recipes Details Page.

Also had to update the 'editrecipe.html' as the 'views' field wasn't there so when I updated a recipe, the views would reset to NULL.

Also when a Recipe Details is viewed then the views would increase by 1.

Changed in app.py, how the form gets stored so that I could add the views field in as an interger and I wouldnt have to hide it on an HTML Form.

### Added Search Functionality

Added a search bar into the base.html so that people can search to see if any recipes can be found.

### Changing Appearance of NavBar, Recipe Details

Trying to make everything come together and try different outcomes for better User Experience

### Changed Recipe Details Page

Nearly completed changing Details Page, just need to put the Recipe Protection in that allows only the creator to edit or delete the Recipes.

## Friday 14th February 2020,

### Updated Buttons at bottom of recipe details

Tried to setup the email input validation, so that it would check to see if your email would match up with the email stored, unfortunately need to work it out.  As its not as easy as i first thought.

#### Test

##### Purpose
To see if a users email would match up with the email stored in their recipe.
##### Method
Typed in jjackson19862017@gmail.com in the search field on the detailsrecipe.html
##### Outcome
Fails
##### Fix
Researching into PyMongo website and Slack.


### Changed Add and Edit Recipe Pages/Forms

I made them look more like the Recipe Details page for consitancy.

### Clickable Recipe Cards

Made Recipe Cards clickable, this was on feedback saying that most people expect them to be.

#### Test

##### Purpose
To see if a user could click on a recipe card instead of just the 'view' link.
##### Method
Clicked on the image of the recipe
##### Outcome
Went to details of the recipe - Expected


## Thursday 20th February 2020,

### Created Modal Box

Using some help from https://www.w3schools.com/howto/howto_css_modals.asp .

I have managed to create a simple modal box, that I plan to make sure that the emails match so that a recipe can only be editted if the email addresses match.

### Edit and Delete Modal

I have modified the Modal box to suit to my Edit Function

I modified the Modal box from the Edit Function to the Delete Function

### Email Address to editdetails working

Forgot to put the name in the form attributes - Thanks Kitty for pointing this out.

### Fix

Broke App.py, because I was halfway through doing something and I then uploaded to Github so I had to finish doing what I was doing.

### Changed Header layout on all pages and added Secure Edit Feature

Have changed the header code, to make it more user friendly.  

Have added the Edit Search Feature to find a users Email to show them there recipes.  However on my test of it, unfortunately it shows all.

#### Test

##### Purpose
To see if a user could search for their recipes
##### Method
Typed in jjackson19862017@gmail.com in the search field on the index.html
##### Outcome
It finds everything - Not Expected
##### Fix
I have now changed the find feature in the App.py, it now finds if the email address is there.

I have also modified the search function so that once it has found a email address it gives you the option of deleting or editing the recipes that the user has made.

However on writing the read me I have just thought of an over sight, I will change this in my next update.

### Created User Recipe Page

To fix my little oversight, I copied the searchrecipes.html.  Renamed it userrecipes.html, then used Github to look up the history of the file and replaced the edit and delete feature with the view feature.

I also removed the edit and delete buttons and modal boxes from the detailsrecipe.html

### Fixed Delete Error

#### Test

##### Purpose
To see if a user could search for their recipes
##### Method
Typed in jjackson19862017@gmail.com in the search field on the index.html
##### Outcome
Took me to the usersrecipe.html - Expected

#### Test

##### Purpose
To see if a user could delete their recipes
##### Method
Clicked on "Delete Recipe"
##### Outcome
Error - Previously I tried to have an if statement with the condition, if the two emails matched then it would delete the recipe.
##### Fix
However I changed the way I was checking and so I just replaced this with my original delete code using Github History.

### Clean up Time

Deleted my Javascript file as this was meant to be used for the Modal Boxes, however I removed this feature.
Deleted my modalbox.css file as this was meant to be used for the Modal Boxes, however I removed this feature.

Updated app.py with comments to make it more readable for other people.
Updated base.html with comments to make it more readable for other people.
Updated index.html with comments to make it more readable for other people.
Updated mystyle.css with comments to make it more readable for other people.

### Feedback off Sam

After a bit of a chat with a fellow web designer, I was given some feedback.

1st - Change the Email text so that its more understandable to users using the system.
2nd - Add a sorry not found in the search feature, so again its more user friendly.

Thank you Sam

### Readme File

Check out all the additions above.

### Shameful Cheat

I changed the banner to a image of Kitchen Tools, so that it mentions that we sell Kitchen Tools.
Like it says in the brief.  I should really do more, however I could add this feature later.  I really need to finish the course and time is not a luxury.

## Friday 21st February 2020,

### Updated Forms

Updated addrecipe.html and editrecipe.html with removing the labels and adding required elements.
