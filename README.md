# Last Trophy 


Welcome to Last Trophy this project was created using HTML, CSS, JavaScript and Django the main premise of this project is to help users with Trophy hunting this application will allow users to view achievement guides, create an account, comment, rate other guides and more more features that will be showcased down below.


## CONTENTS

## UX

### The Strategy Plane

### Site Goals

### Epics

### User Stories

### The Scope Plane

#### Opportunities

### The Skeleton Plane

## DataBase Relationship Models

### Database Schema

### Games Model

### User Model

### Comment Model

### Guides Model

## Design Plane

### Color Palette

## Typography

### Headings

### Body

## Wireframes

### Mobile Wireframes

This is the mobile wireframes for the key features of the last trophy application such as register an account, login to an existing account, view other guides and create guides just to name a few.

### Desktop Wireframes

This is the desktop wireframes for the key features of the Last Trophy application as stated above.

## Key Features

### Navigation Bar

#### Mobile view

#### Desktop view

### Games List

#### Mobile view

#### Desktop view

### Sign up page

#### Mobile view

#### Desktop view

### Login in Page

#### Mobile view

#### Desktop view

### User Guides

#### Mobile view

#### Desktop view

### Detailed Guides

#### Mobile view

#### Desktop view

### Categories 

#### Mobile view

#### Desktop view


### Favicon

#### Mobile view

#### Desktop view


## Technology 

### Languages

#### Frameworks & Tools

## Testing

- Fixed function attribute error by going back into the trophy model and adjusting some key values such as the related name component and the trophy field name on the game model.
- Fixed an error where the trophies were not appearing, after completing the migrations for the model changes this fixed this issue.
- Fixed Slug field error by renaming the slug field to include a slug field and not a char field which fixed this issue.
- Fixed view error by first seperating the category and genre model into the trophy hunter app, I did this so I could reference the game model to link the game to the category. After this in the category view I imported the trophy hunter model and in particular the categories model so I could reference the model and then created the view. There was an issue with the url to fix this I added the url to the project and created the url within the category app which fixed the view error.
- Fixed migrations database model bugs where a field already existed to fix this I deleted the existing migrations and created the database model again.
- Fixed database already exists error by deleting all database models and creating them again starting with the genre model as when trying to delete the game orginally this would clash with the genre model not allowing me to create or add new migrations to the database model. Deleting and creating the models and the model structure again fixed this issue.
- Fixed slug errors by adjusting spelling mistakes to make sure the correct slug was being loaded.
- Fixed a bug where the games were not being seperated into different genres to fix this I created a form and used a table to allow the user to specify which genre, game title or trophy count they were looking for. Once this was done I was able to use the slug url to then allow the user to click on the game title, which takes the user to the game details, such as the trophies and where the written guides will be. The creation of the genre form fixed these errors.
- Had many errors when trying to link the guides to the game model, at first doing this showcased this under every trophy which was not the intended behaviour, to fix this I first added a slug field to the trophy model and then created a slug for all the trophies. After this I created a new app called guides and created a new view, new urls and a new template called guide_detail. Doing this allowed me to access the trophy slug url and link this to the trophy title, which showcased the correct guides under the correct trophies which fixed the guides errors.
- Fixed Warning errors for all urls that had a slash before the pathway removing the slash removed this warning.
- Fixed front end guide bugs originally when I was trying to use the create view class, this did not work as the slug could not be found. I tried to make a new function with a request and recieving the guide id. This did not work as the fields were appearing as being null, in order to fix this I went back to the create view solution and changed the spelling from trophies to trophy which targeted the right slug and fixed this issue.
- Fixed an error where the trophy  needed to be selected, to fix this I added a function called form valid, which would get the value of the primary key of the trophy I had clicked on, which set the trophy title to the one I clicked on which fixed this issue.
- Fixed redirect error originally the create guide view was redirecting the user to the game form, which wasnt a good user experience (UX). To fix this I created a new function called get success url, and then used the function name to get the url and dot notation to get the trophy model and its slug. Which redirected the user to the page they were visiting which fixed this error.
- Fixed update view error when I was trying to edit the current guide again the url was trying to access the same pathway. To fix this I changed the form pk from the trophy pk to the guide pk which fixed this issue.
- Fixed an error where the styling for the guide form was not stying with bootstrap or css. To fix this I went back to the forms.py file for the guide form, created a widgets dictionary for all the form fields. I also used the class form-control which loaded the bootstrap styling for the form fixing this issue.
- Fixed guide if statement by starting the if statement before the for loop, before this the intended behavoiour was not working placing the if statement before the for loop and placing the for loop inside the if statement as part of the else condition fixed this error.
- Fixed create guide bugs, the user could click create guide without being signed in with an error appearing stating no user defined. In order to fix this I added two if statements to first determine if there were any guides created, if there were the first if statement checked if there were no guides and the user was not logged in, if that was the case a login below button appeared for the user to log in. To make sure the user could not login twice I changed the login button to a create guide button to make sure the user could not login twice. After this the button and text would change asking the user to create a guide if there were no guides created.
- Fixed the last create guide error, the error orginally occured when there were guides created and the user was not logged in. To fix this I created another if statement which checked if there were guides created and if the user was not logged in to login. Otherwise the user can create a guide which fixed these erorrs.
## Deployment

## Credits

## Acknowledgements
