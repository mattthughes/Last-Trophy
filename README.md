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

## Deployment

## Credits

## Acknowledgements
