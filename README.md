# Last Trophy

![Am I Responsive Last Trophy](static/images/am-i-responsive-last-trophy.png)

Welcome to Last Trophy this project was created using HTML, CSS, JavaScript and Django the main premise of this project is to help users with Trophy hunting this application will allow users to view achievement guides, create an account, comment, rate other guides and more more features that will be showcased down below.


## CONTENTS

- [Last Trophy](#last-trophy)
    - [CONTENTS](#contents)
    - [UX](#ux)
        - [Strategy Plane](#the-strategy-plane)
            - [Site Goals](#site-goals)
            - [Epics](#epics)
            - [User Stories](#user-stories-list)
        - [Scope Plane](#the-scope-plane)
            - [Features list](#features-list)
        - [Skeleton Plane](#the-skeleton-plane)
            - [Wireframes](#wireframes)
                - [GameList Wireframe](#games-list-wireframe)
                - [Sign up Wireframe](#sign-up-wireframe)
                - [Login Wireframe](#login-wireframe)
                - [User Guides wireframe](#user-guides-wireframe)
            - [Database Relationship Model](#database-relationship-models)
                - [Database Schema](#database-schema)
                    - [Games Model](#games-model)
                    - [Trophies Model](#trophies-model)
                    - [Guides Model](#guides-model)
                    - [Comments Model](#comment-model)
        - [Design plane](#design-plane)
            - [Color Palette](#color-palette)
            - [Typography](#typography)
                - [Headings](#headingss)
                - [Body](#body)
                - [Trophy Title](#trophy-title)
        - [Surface Plane](#surface-plane)
            - [Key Features](#key-features)
                - [Home Page](#home-page)
                    - [Mobile Home page](#mobile-home-page)
                    - [Desktop Home page](#desktop-home-page)
                - [Navigation Bar](#navigation-bar)
                    - [Mobile Navigation View](#mobile-navigation-view)
                    - [Desktop Navigation View](#desktop-navigation-view)
                - [Games List](#games-list)
                    - [Mobile Games view](#mobile-games-view)
                    - [Desktop Games view](#desktop-games-view)
                    - [Admin Games view](#admin-games-view)
                - [Sign up](#sign-up-page)
                    - [Mobile Sign up view](#mobile-sign-up-view)
                    - [Desktop Sign up view](#desktop-sign-up-view)
                - [Sign in](#login-in-page)
                    - [Mobile login view](#mobile-sign-in-view)
                    - [Desktop login view](#desktop-sign-in-view)
                - [User Guides](#user-guides)
                    - [Mobile user guides view](#mobile-user-guides-view)
                    - [Desktop user guides view](#desktop-user-guides-view)
                - [Categories](#categories)
                    - [Mobile Categories view](#mobile-category-view)
                    - [Desktop Categories view](#desktop-category-view)
                - [Comments](#comments)
                    - [Mobile comments view](#mobile-view-comment)
                    - [Desktop comments view](#desktop-view-comment)
                - [Guides and Comments List](#guides-and-comments-list)
                    - [Mobile guides and comments list](#mobile-view-guides-and-comments-list)
                    - [Desktop guides and comments list](#desktop-view-guides-and-comments-list)
                - [Favicon](#favicon)
                    [Desktop favicon view](#desktop-favicon-view)
    - [Technology](#technology)
        - [Languages](#languages)
            - [Frameworks & Tools](#frameworks--tools)
    - [Deployment](#deployment)
        - [Heroku Deployment](#heroku-deployment)
        - [Running Application locally](#running-application-locally)
        - [Fork Project](#fork-project)
    - [Testing](#testing)
    - [Credits](#credits)
        - [Content](#content)
        - [Code](#code)
        - [Imagery and Trophy Descriptions](#imagery-and-trophy-descriptions)
    - [Acknowledgements](#acknowledgements)

                    

[To view the deployed project click here](https://last-trophy-f32c1bd6dcec.herokuapp.com/)

## UX

### The Strategy Plane

#### Site Goals

This site intends to help users unlocking trophies with users being able to create accounts, create there own guides, leave feedback to other users, like and dislike guides to provide feedback to other users and join an ever growing community of trophy hunters.

* To allow users to join an ever growing community
* Create and edit, delete there own guides
* Up vote guides they find useful
* Dislike guides they do not find useful
* Help users to unlock difficult trophies with detailed guides


#### Epics

I created seven epics which were then developed into User stories, every detail regarding the epics and the user stories can be found on the Last Trophy kanban board which can be found at the following [link](https://github.com/users/mattthughes/projects/3)

* Inital Django Project Setup [[#12](https://github.com/mattthughes/Last-Trophy/issues/12)]
* User Profile [[#13](https://github.com/mattthughes/Last-Trophy/issues/13)]
* User Sign in or sign out [[#14](https://github.com/mattthughes/Last-Trophy/issues/14)]
* User Guides [[#15](https://github.com/mattthughes/Last-Trophy/issues/15)]
* Games Searching[[#16](https://github.com/mattthughes/Last-Trophy/issues/16)]
* Guides Interaction [[#17](https://github.com/mattthughes/Last-Trophy/issues/17)]
* Rate Guides Interaction [[#18](https://github.com/mattthughes/Last-Trophy/issues/18)]


#### User Stories list

1. Inital Django setup

* UserStory [[#21](https://github.com/mattthughes/Last-Trophy/issues/21)] - As a **Developer **I want to deploy the app to Heroku so that I can confirm everything works on the deployed site before distribution of the app

2. User Profile

* UserStory [[#19](https://github.com/mattthughes/Last-Trophy/issues/19)] - As a site user I can Create an account so that I canCreate update or delete my own guides or comment on other user guides
* UserStory [[#3](https://github.com/mattthughes/Last-Trophy/issues/3)] - As a site user I can create an account so that I can comment on a guide

3. User Sign in or Out

* UserStory [[#22](https://github.com/mattthughes/Last-Trophy/issues/22)] - As a site user I can login or logout of my account so that I can keep my account secure

4. User Guides 

* UserStory [[#4](https://github.com/mattthughes/Last-Trophy/issues/4)] - As a registered user I can create my own trophy hunting guides so that I can help other users
* UserStory [[#7](https://github.com/mattthughes/Last-Trophy/issues/7)] - As a site user I can click on a guide so that I can read the full text
* UserStory [[#23](https://github.com/mattthughes/Last-Trophy/issues/23)] - As a site user I can delete a guide I have created so that I can remove this from the site

5. Games Searching

* UserStory [[#10](https://github.com/mattthughes/Last-Trophy/issues/10)] - As a site user I can click on the games tab so that can pick a game genre and view all the games of that genre

6. Guides Interaction 

* UserStory [[#1](https://github.com/mattthughes/Last-Trophy/issues/1)] - As a site user I can view a list of guides so that I can pick the achievement guide I am looking for
* UserStory [[#23](https://github.com/mattthughes/Last-Trophy/issues/23)] - As a site user I can delete a guide I have created so that I can remove this from the site
* UserStory [[#2](https://github.com/mattthughes/Last-Trophy/issues/2)] - As a site user/Admin user I can view comments so that I can read the conversation
* UserStory [[#6](https://github.com/mattthughes/Last-Trophy/issues/6)] - As a site Admin I can approve or disapprove comments so that I can filter out objectionable comments
* UserStory [[#5](https://github.com/mattthughes/Last-Trophy/issues/5)] - As a site user I can modify or delete my comment on a guide so that I can be involved in the conversation

7. Rate Guides Interaction

* UserStory [[#20](https://github.com/mattthughes/Last-Trophy/issues/20)] - As a site user I can receive notifications on guides I have written so that I can respond to comments or view the likes and dislikes

### The Scope Plane

#### Features List

* Games - Users can read and view all the games there is.
* Trophies - Users can read and click on specific trophies to gain more information.
* Guides - Users can create edit and delete there own guides using full CRUD functionality.
* Likes and Dislikes - Users can update the database by adding likes and dislikes.
* Comments - Users can Create, edit and delete there own comments and leave comments under other user guides, using full CRUD functionality.
* Account Registration - Users can create and update the database by creating an account.
* Login and Logout - Users can login and logout to keep there information secure.
* Responsive Design - This application needs to have good UX and make sure the application is responsive for all screen sizes.

### The Skeleton Plane

#### Wireframes

##### Games List Wireframe

![Mobile Wireframe Game List](static/images/game-list-mobile.png)

![Desktop wireframe Game List](static/images/game-achievement-desktop.png)


##### Sign up Wireframe

![Sign up Wireframe Mobile](static/images/mobile-sign-up.png)

![Sign up Wireframe Desktop](static/images/sign-up-desktop.png)


##### Login Wireframe

![Login Wireframe Mobile](static/images/login-mobile.png)

![Desktop Wireframe Desktop](static/images/login-desktop.png)

##### User Guides Wireframe

![Mobile user guides wireframe](static/images/guide-page-mobile.png)

![Desktop user guides wireframe](static/images/guide-page-desktop.png)

## DataBase Relationship Models

### Database Schema

The Database Schema for this application is using the Game model as the primary model, which will contain the Trophies model, which will then contain the Guides model, and the guides model will contain the comment model. Each model will have full CRUD functionality, the games and trophies model will only have this for the admin user whereas the comments and guides model will have full crud for the user. Each model is referenced by it's primary key the id of the actual model, to allow other models to use the primary model this will be done by using Foreign keys to gain access to the trophies, comments and guides models all of these models are children from the main game model. 

![Database Schema](static/images/database-schema.png)

### Games Model

This model will be the primary model containing the trophies, with the trophies then containing the guides as well, which will lead to the user being able to create, update, read and delete there own guides while also being able to like and dislike other guides as well. The games model takes its Id as the primary key which will be used when the game is referenced the game has a slug field which will be used in the view and url to determine which game to load. The game has different attributes such as the amount of hours it will take to unlock every trophy, the trophy count, the featured image which will be shown on the game profile, the author which is the admin user, which will be the only user that can create games on the backend and front end, the rating and finally the genre which will placed in a genre form to control which games are shown when selecting a specific genre.

### Trophies Model

The Trophies model takes its Id as the primary key to reference the correct trophy. The model will also have a slug field as well to be used in the url and the view. This model also uses the game model as a foreign key to link the trophy with the correct game, the model will have full CRUD functionality for the admin user only. The Trophies model has many attributes such as featured image the image that will be shown with the trophy, there is a rarity field which will be a float field which will be used with a meta tag to order each trophy based on this attribute, The title field which will be a char field and will be displayed above the trophy description field, which is also a char field providing a brief description of how to unlock this trophy. The model will have a difficulty field as well showcasing how hard this trophy is to unlock which will also be a float field.
### Guides Model

Thie Guides model takes its Id as the primary key to reference the correct guide. This model will give the user full CRUD functionality allowing users to create guides, if logged in to edit guides, if they are the author and finally delete guides as well if they are the author. The user will also be able to add likes and dislikes to other user guides. This model has many attributes such as the author which will be selected as the logged in user making this request. The Trophies model will be the foreign key linking the guide to the correct trophy. The model will also have a likes and dislikes field which will be a many to many field allowing the users to add and update the database in the front end, by leaving likes and dislikes to other guides if logged in. The model will have a body field which will be the text area allowing the user to write a guide in detail. The model will also have a approved section this section will be a boolean field which will default to false, which will allow the admin user to control which guides appear on the application, a user will recieve visual feedback stating there guide is awaiting approval. The admin user will be able to approve guides and also delete guides they find inappopriate. 

### Comment Model

This model uses its Id as the primary key which will be used when editing and deleting a comment. This model will have full CRUD functionality allowing a user to create a comment if logged in edit there comment and delete there comment if they are the author. This model uses the guide model as a foreign key to link the comment to the correct model. This model has many different attributes such as the approved field like the Guide model the comment model has an approved field which will allow the admin user to control which comments are approved and deleted. The model also contains a text area field allowing the user to write there comment in detail if needed.

## Design Plane

### Color Palette

This is the Color Palette I decided to go with, The red will be used for the errors on the application and delete buttons, while the green will be used for any login or sign up buttons on the home page. There will also be a blue colour that is used for upvoting other user guides and for the sign in and sign up views. While the floral white will be used for the background, the color grey will be used for the trophies detail to make the trophies stand out. The application has a very simplistic look to not take away any attention from the content on the application.

![Color Palette](static/images/colors-last-trophy-color-palette.png)

## Typography

### Headings

The heading I have decided to go for is the Arimo font. This font stands out and fits well with the overall style of the application, making the headings stand out.

![Heading Typography](static/images/heading-typography.png)

### Body

The body font I decided to go for was the Raleway font I liked the way this fit with the overall colour scheme of the application where the text was not taking away from the content on the application

![Body Typography](static/images/body-typography.png)

### Trophy Title

The Trophy Title font I decided to go with is the Sedan font. This font is slightly different as there are 258 trophies, I felt the trophies needed to stand out more on the application as otherwise the font could of all blended into one, having this different style allowed the trophies to stand out from the rest of the application.

![Trophy Title Typography](static/images/trophy-title-typography.png)

## Surface Plane

### Key Features

### Home Page

This Feature will show two different screens depending if the user is logged in or not if the user is not logged in a short welcome message will appear asking the user to either login or register, Once logged in the welcome message will change welcoming the user back to Last Trophy where a random game will appear showing the user the type of Games the website has if they would like to view the full details regarding this game they can click on the games button and then click on the games title which will lead them to the full details regarding this game.

#### Mobile Home Page

`Not Logged in`

![Index Mobile not logged in](static/images/index-mobile-not-logged-in.png)


`Logged in`

![Index Mobile logged in](static/images/index-logged-in-mobile.png)


#### Desktop Home Page

`Not Logged in`

![Index Desktop not logged in](static/images/index-not-logged-in-desktop.png)

`Logged in`

![Index Desktop Logged in](static/images/index-logged-in-desktop.png)

### Navigation Bar

This feature will collapse on mobiles and stretch on desktops, allowing users to click on the the game title leading them to the categories, clicking register to create an account or click login to login to an exisiting account.

#### Mobile Navigation view

![Navigation mobile](static/images/navigation-bar-mobile.png)

#### Desktop Navigation view

![Navigation Desktop](static/images/navigation-bar-desktop.png)

### Games List

This element will be shown to the user once they have clicked on a game showing the games rating the amount of trophies and how long it could take to unlock every trophy. Underneath this information the games trophies will be listed below showing a brief description how to unlock this trophy.


#### Mobile Games view

![Mobile Game List](static/images/mobile-game-user-view.png)


![Mobile Games Trophies](static/images/trophies-mobile-user-view.png)


### Trophies view

#### Mobile Trophies view

This is the Trophy title and its description

![Mobile Trophy](static/images/trophy-detail-mobile.png)

This is the Guide detail view Associated with this trophy

![Mobile Guide](static/images/guide-detail-mobile.png)


#### Desktop Trophies view

This is the Trophy title and its description

![Desktop Trophy](static/images/trophy-detail-desktop.png)

This is the Guide detail view Associated with this trophy

![Desktop Guide](static/images/guide-detail-desktop.png)

#### Admin Trophies view

![Admin Trophy view](static/images/trophy-detail-admin.png)


#### Desktop Games view

![Desktop Game List](static/images/desktop-game-user-view.png)

##### Admin Games view

This is what the admin user will see when logged in allowing them to either delete the game edit the game or add further trophies 

![Admin Game](static/images/admin-game-detail.png)

The admin user will be able to edit or delete trophies if they wish

![Admin Game Trophies](static/images/trophies-admin-view.png)

### Sign up page
The sign up page will be showcased to the user allowing them to create an account to gain access to the features of the last trophy site such as creating guides, editing there own guides and deleting there own guides. They will also be able to provide feedback to other users such as adding comments and liking and disliking guides.


#### Mobile Sign up view

![Sign up Mobile view](static/images/register-sign-up-mobile.png)

#### Desktop Sign up view

![Sign up Desktop view](static/images/sign-up-desktop-view.png)


### Sign in Page

The login page will be showcased to the user, allowing them to login to an existing account to review the guides they have created, create other guides or respond to feedback.


#### Mobile Sign in view

![Login Mobile](static/images/login-mobile-view.png)

#### Desktop Sign in view

![Desktop Login](static/images/login-desktop-view.png)

### User Guides

This page will allow the user to view the exisiting guides, create a new guide, delete there guides if logged in or edit there guides if logged in.


#### Mobile User Guides view

When there is a guide created this view will be shown if the user is not logged in

![Mobile user not logged in](static/images/mobile-desktop-guide-not-logged-in-guides.png)

When there is a guide created this view will be shown if the user is logged in

![Mobile user logged in](static/images/mobile-guides-created-logged-in.png)

When there isnt a guide created this view will be shown if the user is not logged in

![Mobile user not logged in zero guides](static/images/zero-guides-mobile-not-logged-in.png)

When there isnt a guide created this view will be shown if the user is logged in

![Mobile user logged in zero guides](static/images/logged-in-user-zero-guide-mobile.png)

If the site user is the admin user this view will be shown

![Admin user logged in](static/images/admin-logged-in-guide.png)

This is the view to edit a guide

![Mobile Edit guide](static/images/edit-guide-mobile.png)

This is the view to delete a guide

![Mobile Delete guide](static/images/delete-guide-user.png)

This is the view for the admin user to delete a guide

![Mobile Delete guide admin user](static/images/delete-guide-admin-mobile.png)

#### Desktop User Guides view

When there is a guide created this view will be shown if the user is not logged in

![Desktop user logged in guides created](static/images/logged-in-user-guide.png)


When there is a guide created this view will be shown if the user is logged in

![Desktop user not logged in guides created](static/images/desktop-guide-not-logged-in.png)

When there isnt a guide created this view will be shown if the user is not logged in

![Desktop user zero guides not logged in](static/images/zero-guides-desktop-not-logged-in.png)

When there isnt a guide created this view will be shown if the user is logged in

![Desktop user zero guides not logged in](static/images/logged-in-user-zero-guide-desktop.png)

This is the view to edit a guide

![Desktop Edit guide](static/images/edit-guide-desktop.png)

This is the view to delete a guide

![Desktop Delete guide](static/images/delete-guide-desktop-user.png)

If the site user is the admin user this view will be shown

![Desktop guide admin user](static/images/admin-logged-in-guide.png)


This is the view for the admin user to delete a guide

![Desktop Delete guide admin user](static/images/delete-guide-admin.png)

### Categories 

#### Mobile Category view
This is the form and form results view on mobile.

![Mobile view Category form](static/images/form-mobile.png)

![Mobile view category results ](static/images/form-results-mobile.png)

#### Desktop Category view

This is the form and form results view on desktop

![Desktop view category form](static/images/form-desktop.png)

### Comments

This element will allow users to leave comments on user guides whether there own or other user guides if logged in.

#### Mobile view Comment

![Mobile view comments](static/images/comment-mobile.png)

This is the edit view for Mobile if the user is logged in

![Mobile edit comment](static/images/edit-comment-mobile.png)

This the delete view for Mobile  if the user is logged in

![Mobile delete comment](static/images/delete-comment-mobile-user.png)

This is the delete view if the user is the Admin user.

![Mobile delete comment admin user](static/images/delete-comment-admin.png)

#### Desktop view Comment

![Desktop view comments](static/images/comment-desktop.png)

This is the edit view for Desktop if the user is logged in

![Desktop edit comment](static/images/edit-comment-desktop.png)

This the delete view for Desktop  if the user is logged in

![Desktop delete comment user](static/images/delete-comment-desktop-user.png)

This is the delete view if the user is the Admin user.

![Desktop delete comment admin user](static/images/admin-user-delete-comment.png)


### Guides and Comments List

This view will allow the admin user to specify which Guides to approve, which guides to delete and which Comments to delete which allows the admin user to have full control over the site.

#### Mobile view Guides and Comments List

This is the view of guides awaiting approval 

![Mobile Guides awaiting approval](static/images/approve-guide-mobile.png)

This is the approval form

![Mobile Guides approval form](static/images/approve-guide-form-mobile.png)

This is the delete Guide list

![Mobile Guides list](static/images/guide-list-mobile.png)

This is the delete Comments list

![Mobile Comments list](static/images/comment-list-mobile.png)

This is the view if all guides are approved

![Mobile Guides all approved](static/images/guide-approval-mobile.png)



#### Desktop view Guides and Comments List

This is the view of guides awaiting approval 

![Desktop Guides awaiting approval](static/images/approve-guide-desktop.png)

This is the approval form

![Desktop Guides approval form](static/images/approve-guide-form-desktop.png)


This is the delete Guide list

![Desktop Guides list](static/images/guide-list-admin.png)

This is the delete Comments list

![Desktop Comments list](static/images/comment-list-admin.png)

This is the view if all guides are approved

![Desktop Guides all approved](static/images/guides-approved.png)


### Favicon

This will be shown when the user is on the webpage the design is very simple a trophy symbolising what the application is about.


#### Desktop Favicon view

![Desktop Favicon view](static/images/favicon-last-trophy.png)

## Technology 

### Languages

#### Frameworks & Tools
* Python

    * The following python modules and libraries were used for this application
        * asgiref==3.7.2
        * cloudinary==1.36.0
        * crispy-bootstrap5==0.7
        * dj-database-url==0.5.0
        * dj3-cloudinary-storage==0.0.6
        * Django==4.2.11
        * django-allauth==0.57.2
        * django-crispy-forms==2.1
        * django-filter==24.1
        * gunicorn==20.1.0
        * oauthlib==3.2.2
        * psycopg2==2.9.9
        * PyJWT==2.8.0
        * python3-openid==3.2.0
        * requests-oauthlib==2.0.0
        * sqlparse==0.4.4
        * urllib3==1.26.18
        * whitenoise==5.3.0

* Django
    * Django was used as the main python full stackframe work for the development of this application
    * Django allauth was used to improve the security of the application to prevent unauthorised users viewing content they shouldnt

* Heroku
    * Heroku was used as the cloud based platform which the project was deployed on any change that was made on the development site was deployed on Heroku to ensure the application worked as intended.
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project.
* Bootstap 5.13
    * Bootstrap 5.13 was used for the layout of this application along with generic styling
* Font Awesome
    * Font Awesome was used for many icons such as the Game detail view which specifies the hours as a clock rather than the word hours.
* CSS
    * Custom CSS was included in the site to give the site an orginal design.
* Django/Templating
    * Django templating was used to insert data from the database onto the front end, this was also used for adding extra logic if certain users were logged in to display specific information.
* HTML'
    * HTML was used as the base language for the templates on this site.



## Deployment

This application was created using GitPod and was then pushed to GitHub to the respository called [Last-Trophy](https://github.com/mattthughes/Last-Trophy)

To make sure I was able to keep updated with the changes I used the following git commands:

git add- This command was used to add the changes to the staging area before changes are commited.

git commit -m "message"- This command was used to add the changes to the repository queue.

git push - This command pushes all the commited code in the repository queue to Github.

### Heroku Deployment

1. Log in to Heroku or set up an account.
2. From the dashboard click create new app.
3. Name your app this will need to be unique as you cannot use an existing application name.
4. This will create the app within Heroku and will bring you to the deploy tab. From this navigate to the resources tab.
5. Add the database to the app, to do this navigate to the add ons section and search for Heroku Postgres select the pckage that appears and add Heroku Postgres as the database.
6. Navigate to the settings tab, within the config vars section copy this DATABASE_URL to the clipboard to use this later in your django app.
7. Within the djanjo app repository create a new file called env.py to do this type into the terminal touch env.py. Within the file create an environment variable for the DATABASE_URL pasting the address from your clipboard you copied from heroku.
8. Add a SECRET_KEY to the app using another another environment variable you can obtain a secret key from a random secret key generator paste this secret key into the environment variable your secret key variable should be written like this os.environ.setdefault(
    "SECRET_KEY", "Yoursecret key")
9. Add the secret key just created to your heroku config vars by adding SECRET_KEY and the key you created as the value.
10. In the settings.py file  import Path from pathlib, import os and import dj_database_url
11. insert this line if os.path.isfile("env.py"): import env into the settings.py file 
12. Remove the default secret key that django has in the settings.py file and type SECRET_KEY = os.environ.get('SECRET_KEY')
13. Next replace the default database by either commenting out the code or deleting it you can use the default database for any automated testing later, replace this database with DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.config(),}
14. In the terminal migrate over any changes you have just made by typing python3 manage.py migrate you may need to make the migrations first if you do type python3 manage.py makemigrations and then the migrate command after.
15. Navigate to cloudinary in the browser and create an account or login if you already have an account.
16. From the dashboard copy the CLOUDINARY_URL and navigate over to the django app and create a new environment variable by typing os.environ[Cloudinary_URL] paste the url that you just copied after the assignment operator.
17. In Heroku add the CLOUDINARY_URL and the value you copied to the config vars.
18. Add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars.
19. Make sure to delete this key value par prior to final project deployment.
20. Navigate back to the settings.py file and add the cloudinary libaries to the installed apps the order should be cloudinary_storage then django.contrib.staticfiles and then cloudinary below this make sure you follow this order.
21. Next add the STATIC files settings which are the url, storage path, directory path, root path, media url and default file storage path.
22. Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
23. Add Heroku to the ALLOWED_HOSTS list. It should read as .herokuapp.com
24. Create a static, templates folder in the code editor.
25. Createa new file in the top level directory and call it Procfile
26. In the Procfile add the following code web: guincorn PROJECT_NAME.wsgi
27. Make sure to add, commit and push changes to GitHub.
28. Navigate back to Heroku and click on the deploy tab scroll down to the  deployment method, select GitHub and confirm you would like to connect to GitHub.
29. Enter your GitHub repository Id and then select connect.
30. If you would like every change you make on your IDE to appear on the deployed app click Enable Automatic Deploy. Otherwise you can deploy this manually each time to have more control of deploys.
31. For the last step click Deploy Branch in the manual deploy section this will start to the build the app slowly once this has been built a deployed link will appear allowing to to view your deployed app.


### Running Application Locally

Navigated to the GitHub Repository:

1. Click on the code drop down and click on HTTPS
2. Copy the Repository link to the clipboard
3. Open your IDE such as GitPod, CodeAnywhere or any of your choosing making sure git is also installed
4. Type git cone alongside the repository link you have just copied into the IDE terminal, the project will now be cloned for use.


### Fork Project

1. Log in or sign u to GitHub.
2. Go to the repository for this project [mattthughes/last-trophy](https://github.com/mattthughes/Last-Trophy)
3. Click the Fork button on the right corner to fork the project.

## Testing 

* I tested this project extensively, making sure everything worked as intended this was all documented in the TestingMd file which can be viewed here [TestingMd](https://github.com/mattthughes/Last-Trophy/blob/main/TESTING.md)

## Credits

### Content

* All content was written by Matthew Hughes

### Code

* Creating and filtering genre form inspired and customised to project needs [Django genre form](https://www.youtube.com/watch?v=FTUxl5ZCMb8)
* Displaying query set in generic display view inspired and customised to project needs [Django list view query set](https://www.geeksforgeeks.org/listview-class-based-views-django/)
* Creating Likes and adding them to the correct model was inspired from here and customised to my projects needs [Likes creation](https://www.youtube.com/watch?v=PXqRPqDjDgc)
* Remove likes from the model was inspired from here and customised to my projects needs [Remove likes](https://www.youtube.com/watch?v=dwgIi8dspa4&t=13s)
* Restricting access for views inspired and customised to projects needs from here [Django restricting views](https://www.codu.co/articles/securing-django-views-from-unauthorized-access-npyb3to)
* Creating and running tests inspired and customised to projects needs from here [Django testing](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
* Using the random module to randomise the game model on the index home screen from here and customised to my projects needs[Random model](https://www.youtube.com/watch?v=RfwzB7-qw7E)
* Adding an if statement to determine which database to use provided by Code Institute Mentor Daisy and taken from here [Settings if statement] (https://github.com/Dee-McG/LGBTQ-Networking-Platform/blob/28227b43140be4b99d0b08d720fd9a48659f36e4/lgbqt/settings.py#L107)



### Imagery and Trophy Descriptions

* Elden Ring Game Image on [Ebay](https://www.ebay.co.uk/itm/304348648747)
* Elden Ring Game detail from [True Achievements](https://www.trueachievements.com/game/Elden-Ring/achievements)
* Elden Ring Trophies Description and rarity from [Psn Trophies](https://psnprofiles.com/trophies/15539-elden-ring)
* Celeste Game Image on [MobyGames](https://www.mobygames.com/game/101142/celeste/cover/group-162329/cover-654261/)
* Celeste Game detail from [True Achievements](https://www.trueachievements.com/game/Celeste/achievements)
* Celeste Trophies Images, Description and rarity from [Psn Trophies](https://psnprofiles.com/trophies/7173-celeste)
* Resident Evil 7 Game Image on [Wccftech](https://wccftech.com/resident-evil-7-new-teasers-showcase-familiar-franchise-features/)
* Resident Evil 7 Biohazard Game detail from [True Achievements](https://www.trueachievements.com/game/Resident-Evil-7/achievements)
* Resident Evil 7 Biohazard Trophies Images, Description and rarity from [Psn Trophies](https://psnprofiles.com/trophies/5776-resident-evil-7-biohazard)
* Tekken 8 Game Image on [Insider-gaming](https://insider-gaming.com/tekken-8/)
* Tekken 8 Game detail from [True Achievements](https://www.trueachievements.com/game/Tekken-8/achievements)
* Tekken 8 Trophies Images, Description and rarity from [Psn Trophies](https://psnprofiles.com/trophies/25534-tekken-8)
* Alien Isolation Game Image on [David muscat Literature](https://davidmuscatliterature.wordpress.com/2019/02/03/game-review-alien-isolation/)
* Alien Isolation Game detail from [True Achievements](https://www.trueachievements.com/game/Alien-Isolation/achievements)
* Alien Isolation Trophies Images, Description and rarity from [Psn Trophies](https://psnprofiles.com/trophies/2967-alien-isolation)
* F1 23 Game Image from [Tech Gameworld](https://techgameworld.com/all-about-f1-23-features-trailers-and-release-date-of-the-new-game/)
* F1 23 Game detail from [True Achievements](https://www.trueachievements.com/game/F1-23/achievements)
* F1 23 Trophies Images, Description and rarity from [Psn Trophies](https://psnprofiles.com/trophies/22490-f1-23)
* Placeholder Game image [City of Mebanenc](https://cityofmebanenc.gov/parks-facilities-trails/placeholder-image/)
* Placeholder Trophy image [Icon Finder](https://www.iconfinder.com/icons/1552464/image_photo_placeholder_screenshot_icon)


## Acknowledgements

* I would like to thank my mentor Graeme for his help during our sessions, which helped me make changes where needed and constantly keep me on track during this project.
* I would like to thank everyone in the code institute slack community that took there time to help in giving out feedback.
* I would like to thank all my friends and family, who took the time to help test the project and provide me with any feedback to improve the project.