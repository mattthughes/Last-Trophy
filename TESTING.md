# Testing



## Testing Content 

### HTML Validation

### Python Validation

### Solved Bugs

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
- Fixed python structure bugs by changing how many characters a specific line of code was, adding extra space and removing empty white lines etc which fixed these errors.
- Fixed 500 error which was not displaying correctly because  there were to many arguments in the function, to fix this I removed the exception argument which fixed this issue.
- Fixed create view error when trying to use user permission mixin. The logic I was using was trying to get the author of the guide and match that with the logged in user, when there wasn't one. To fix this I added the login required mixin which redirected the user to the login page, once logged in the users was  then able to create a guide.
- Fixed guide bugs I was unable to reference the specific trophy in the guide view, to fix this I changed the trophy.title to trophies which referenced the spelling in the view which loaded the specific trophy to the web page.
- Fixed user authentication create game error, orginally the create game button would not appear regardless of which user was logged in. In order to fix this I added an if statement making sure the user was the superuser user which checked if the logged in user was the super user, if they are the button would show allowing the admin user to create a game in the front end.
- Fixed approving guide bugs orginally the guides awaiting approval were not being shown. To fix this I created a new template and a new view to sort the guides awaiting apporval as approved equals false. I displayed this in a list view. To then approve the guides I created a new form which used the approved field where the admin user can tick this box to approve the guide which is then added to the trophy fixing this issue.
- Fixed Guide model does not have the guide attribute. Orginally I was trying to access the guides primary key in the success url and the guide attribute did not exist, in order to fix this I changed the success url to the url not approved guides. Which returned the admin user to the unapproved guides page fixing this issue.
- Fixed Likes error when the user was not logged in, this would return a status code. To fix this I added an if statement to the view checking if the user was logged in, if they were logged in this would add a like if the user was not logged in the user would be returned to the login page asking the user to login which fixed this issue.
- Fixed Likes bug by seperating the guide view into another view orginally I was targeting the trophy model which would not let show the specific likes for that guide, to fix this I created a new view using the detail view of that specific guide. To see all the information regarding this guide, such as leaving likes and comments. I did this by using the get context data method overriding the default behaviour of the detail view to show more content in this view which fixed this issue.
- Fixed comment error, originally the comments were being shown under every guide of that specific trophy, to fix this I removed the field trophy from the comment model. After this I then targeted the comment by using dot notation to find the comment model. If there was not a comment created the user could create a comment. By using dot notation to find the comment model and removing the trophy field section from the comment model fixed this issue.
- Fixed Admin Guide deletion error. Orginally one of the user stories was to allow the admin user to delete guides on the front end if they needed to. Originally this didnt work with the test function I was using. In order to fix this I added an if statement checking if the admin user was making the request, if they were to return the objects author allowing the admin user to access this view. To make sure I also allowed the orginal guide user to still delete there own guides, I added an else statement to return this view if the author was making this request which fixed these issues.

### Known Bugs

### Lighthouse Testing

#### Mobile Lighthouse Testing

#### Desktop Lighthouse Testing

### Wave Report

### Manual Testing

#### Aims

* The aim of testing is to make sure all elements work as intended without any console or server errors on the front end or the back end, make sure this application is responsive on all screen sizes.

* This will be done by allowing the user to login, logout, register create, edit and delete there own comments and guides. The user will be able to click on each trophy leading to the information regarding this trophy such as any guides that have been created.

* Make sure created error pages are shown rather than generic django errors.

* When the user tries to view content via a url make sure the user is redirected to a login page making sure the user has the permissions for this.

### Testing Steps 

* I will test the responsiveness for all screen sizes by firstly clicking on the application and using the inspect tool to open the google chrome developer tools.
* After this I will click on the laptop display and change the aspect ration to 280px which is the lowest screen size, after this I will begin adjusting the screen sizes to make sure all elements are displaying correctly on all screen sizes.
* I will make sure all trophies go to the correct trophy and none are duplicated, if a user is logged in they can create guides, if they are the guide author they can edit and delete this guide otherwise redirect the user.
* I will make sure all links open in seperate tabs not taking the user from the pain page.
* I will make sure the created error pages are shown rather than django generic errors. 
* All testing will be completed using Google Chrome, Internet Explorer.


### Testing Results

`Celeste Game`

**Element**|**Expected Outcome**|**Testing Performed**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Forsaken Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Gateway Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Archaeology Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Checking Out Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Strawberry Badge Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Breathe Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
In the Mirror Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Reflection Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Celeste Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Pointless Machines Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Strawberry Medal Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Resurrections Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Eye of the Storm Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Scattered and Lost Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Black Moonrise Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Sever the Skyline Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Real Gamer Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Heart of the Mountain Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Heavy and Frail Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Good Karma Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Quiet and Falling Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Golden Feather Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Pink Sunrise Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Mirror Magic Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Center of the Earth Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
No More Running Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Say Goodbye Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Impress Your Friends Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
1UP Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Thanks For Playing Trophy|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Heartbeat|Load Trophy detail when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass

`Alien Isolation Game`

**Element**|**Expected Outcome**|**Testing Performed**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
A Record of Disaster|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Awake|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
The Missing|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Build to Survive|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Welcome to Sevastopol|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
A Perfect Organism|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
A Hunt Begins|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Every Bullet Counts|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
She's in the Vents...|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Fault Detected|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Not a Scratch|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
You Shouldn't Be There|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Light 'em Up|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Power Games|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
How Do You Feel?|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Back Off|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Stunned|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Shock to the System|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Caught in the Trap|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
I Admire its Purity|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Seegson Security Bypass|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
An Outpost of Progress|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Not the First|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Self Defense|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Use With Caution...|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Bait|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Hazard Containment|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
A Synthetic Solution|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Consultation|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
This Should Work|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Seegson Systems Expert|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Throwing the Switch|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
The Message|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Transmission|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Free the Torrens|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Ripley, Signing Off|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
End of the Hunt|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
A True Engineer|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Voices of Sevastopol|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Retreat From Fire|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
My Turn Now|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Hide. Run. Survive.|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Just out of Reach|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
100 Times Too Many|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Survivor|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Mind Your Step|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Mercy or Prudence?|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Archivist|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
The Taken|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
One Shot|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass
Alien: Isolation|Load Trophy when clicked|Clicked Trophy Title|Trophy Detail loaded|Pass

### Automated Testing