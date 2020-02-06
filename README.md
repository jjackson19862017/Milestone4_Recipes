# Refreshing Edible Cuisine In Portable External Support
      R         E       C     I     P       E       S  

[Deployment on Heroku](https://ms4recipes.herokuapp.com/)

I plan to design and build, a forum of information that Users can contribute and share with the wider community.  I plan to use the information learnt in Flask, Python and using MongoDB

I also plan to try and promote Cooking Tools.
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
The main image used is from https://www.forksoverknives.com/plant-based-primer-beginners-guide-starting-plant-based-diet/#gs.w27a6h

### Acknowledgements

- I received inspiration for this project from X

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