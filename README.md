
# Milestone Project 5 - Office Lunches Website
![All devices](https://github.com/renatalantos/office_lunch_website/blob/main/static/documents/screenshots/Responsivity.JPG) 

[View the live project here.](https://renatalantos-office-lunches.herokuapp.com/)

This is the main marketing website for the fictitious e-commerce business, Office Lunches. It is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential users and buyers.

## Table of Contents

* [Introduction](#introduction)

* [UX](#ux) 
    - User Stories
        -  First Time Visitor Goals
        -  Returning and Frequent Visitor Goals
        -  Site Administrator Goals  
* [Layout](#layout)

    - Design
        - Colour scheme
        - Typography
        - Images
    - Wireframes
        - Discrepancy with Original Ideas
        - Links to Wireframes
* [Features](#features)
    - Responsivity
    - Interactive Elements
    - Features to add in future

* [Technologies Used](#technologies-used) 
    - Languages Used
    - Frameworks, Libraries and Programs Used  

* [Testing](#testing)
    - Testing User Stories from User Experience (UX) Section
    - Further Testing
    - Unresolved Bugs 

* [Search Engine Optimization](#SEO)
    - Techniques Implemented
    - Linking to Other Websites
    - Other Backend Solutions
    - Handling Nonexistent Content and User Errors

* [Deployment](#deployment)

* [Credits](#credits)

# Introduction

The product Office Lunches is a fictitious E-commerce webpage where users can buy quick lunches that will be delivered to them. 
Beside being able to view pages like the Home page, All Products, Food, Drinks and Contact Us pages, users are also able to 
* create an account
* sign in
* sign up for a newsletter
* view the company's privacy policy
* search for products
* sort products by category and other criteria
* view all products
* view individual product details
* place products in basket
* update product quantity
* delete products from basket
* place an order for a product
* make a payment
* create a profile
* save profile details 
* view profile details
* view order history 
* write, edit, and delete user reviews
* add products to favourites list and remove them from there
* contact the company by submitting an enquiry
* get feedback on all actions they are performing.

Certain features are available for registered users only, however unregistered users can buy from the site as well.  Site administrators are able to add end edit product and to add and delete reviews.
The site has been designed to be fully responsive on desktop, laptop, tablet and mobile devices.


# UX

-   ### User stories 

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the business and its products.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time Visitor, I want to sign up for a user account to access restricted contentd.
        4. As a First Time Visitor, I want to search for products, view all products, view individual product details.
        5. As a First Time Visitor, I want to place an order.
        6. As a First Time Visitor, I want to make a safe payment.
        7. As a First Time Visitor, I want to create a user profile, so that I can save my details in them and make next-time interaction with the site faster and easier.
        8. As a First Time Visitor, I want to sign out of my user account at the end of the session to keep my account related details safe.
        9. As a First Time Visitor, I want to get feedback on all activities performed other than viewing products.
        

    -   #### Returning and Frequent Visitor Goals

        1. As a Returning and Frequent Visitor, I want to sign into my user account.
        2. As a Returning and Frequent Visitor, I want to create orders and view my current and previous orders.
        3. As a Returning and Frequent Visitor, I want to create reviews and alternatively edit them or delete them.
        4. As a Returning and Frequent visitor I want to send messages and queries to the site owner.
        5. As a Returning and Frequent visitor I want to add products to my favourites list, to make reordering easier, alternatively, I would like to delete them from there.
        6. As a Returning and Frequent Visitor, I want to subscribe to the companies newsletter to find out about new products and deals.
        7. As a Returning and Frequent Visitor, I want to sign out of my account at the end of the session to keep my account safe.
        9. As a Returning and Frequent Visitor, I want to get feedback on all activities performed other than viewing products.

    -   #### Site Administrator Goals
        1. As a Site Administrator I would like to be able to add, view, edit and delete products.
        1. As a Site Administrator I would like to be able to create, view, and delete reviews.
        
        
# Layout
-   ### Design
    -   #### Colour Scheme
        -   The main colours in the website theme for header, background, footer and text labels are yellow, very light olive green, and green. For small details, like small links to products, I use red.
    -   #### Typography
        -   I used a standard Bootstrap theme with all the components and styling. Montserrat and Quicksand are the main fonts used, with Montserrat representing the more factual content and Quicksand is more used for product detail or where I'm hoping to attract the user to the site - e.g footer headers.
    -   #### Imagery
        -   Imagery was chosen to go with the website's colour and content theme. I'm using product images with bright, cheerful colours and attractive graphics. The navbar, the home page, the footer and the display all products and product detail layout come from 3 separate Bootstrap templates, which I customized for my own use. I use Boostrap cards to display multiple products, this way product image and product information are strongly tied together. Information whether a product is vegan, vegetarian, glutenfree is displayed with small images on the products page. Users who are interested in these products are familiar with the imagery.

*   ### Wireframes
    -   #### Discrepancy with original ideas
        -   I originally intended to closely follow the Boutique Ado tutorial, which is strongly reflected in my wireframes. However, the home page and the all products and the product detail pages come from 3 different separate Bootstrap templates.
        [Bootstrap template for home page](https://startbootstrap.com/theme/agency)
        [Bootstrap template for all products page](https://startbootstrap.com/template/shop-homepage)
        [Bootstrap template for product detail page](https://startbootstrap.com/template/shop-item)

        The layout for the rest of the pages comes from Boutique Ado. However, I don't use 2 separate headers but one and the search, user and basket icons are in the same line as the nav links. Other than that, the finished site is very similar as drawn up in the wireframes, only I gave forms 100% width in mobile view as it was done in the tutorial.
    -   #### Links to Wireframes

        -   Wireframes in Desktop View - [View](https://github.com/renatalantos/office_lunch_website/blob/main/static/documents/wireframes/Wireframes%20for%20Desktop%20view%20MS5%20PDF.pdf)

        -   Wireframes in Tablet View - [View](https://github.com/renatalantos/office_lunch_website/blob/main/static/documents/wireframes/Wireframes%20for%20Mobile%20view%20MS5%20PDF.pdf)

        -   Wireframes in Mobile View - [View](https://github.com/renatalantos/office_lunch_website/blob/main/static/documents/wireframes/Wireframes%20for%20Mobile%20view%20MS5%20PDF.pdf)


# Features

-   ### Responsivity

The application is responsive on all device sizes, thanks to Boostrap. In mobile view there is a collapsible menu icon. All images, text labels, forms get appropriately resized. I followed the code refactoring tutorial in Boutique Ado for the shopping bag page, so the only one that caused problems is resizing properly now. 

-   ### Interactive elements
    -   #### Nav links for Home, Menu, All in Our Store, Food, Drinks, Contact Us, Register, Login and Logout pages
    -   #### Form input fields on signup, register, signout, checkout (till), user profile, contact us, subscribe to newsletter, search for product, write review and edit review forms plus add and delete product form for superuser
    -   #### Buttons - including form buttons (signup, register, signout, checkout (till), user profile, contact us, subscribe to newsletter, write review, edit and review buttons plus add, delete product and upload product form buttons for superuser)
    -   #### Dropdown boxes - including dropdown boxes for All Products, Food, Drinks, User, Sort by, Rating, Grill Option dropdowns
    -   #### Edit and Delete links - including edit and delete product link for superuser, delete product link on Favourites page, update product quantity and delete product on shopping bag (basket) page.
    -   #### Update Quantity buttons - enable user to increase or decrease product quantity, present on product detail and shooping bag (basket) pages
  

-   ### Features to add in future   
    -   #### I would like to add a lunch deal functionality which allows users to choose 3 products from 3 different categories and get a discount then. This was beyond the scope of this project, yet certain items have a Lunch Deal Item label.

### Technologies Used 
# Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used
1. [Django:](https://www.djangoproject.com/)
    - The Python-based Django framework was used to set up the structure, functionalities,  data model and database of the website.
1. [Bootstrap 5.1.3:](https://startbootstrap.com/theme/agency)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    -    Montserrat and Quicksand are the main fonts used, Quicksand for label titles and Montserrat for body text.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript. It is also used for the date picker, the dropdown list, the up arrow button and the toat messages.
1. [Javascript:](https://en.wikipedia.org/wiki/JavaScript)  
    - Javascript was used to define visibility duration for popup messages, the functionality of the product quantity updates, navbar toogling, the sort dropdown box, Stripe payment and webhook handling.
   [Json:](https://en.wikipedia.org/wiki/JSON)
   - Json files were used to upload fixtures for categories and product categories.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
1. [Lucidchart:](https://www.lucidchart.com/)
    - Lucidchart was used to create the data model of the project . 
    * [View data models for Product, Category and Order:](https://github.com/renatalantos/office_lunch_website/blob/main/static/documents/database%20schema/Product%2C%20Category%20and%20Checkout%20Model.pdf)   
    * [View data models for OrderLineItem and UserProfile:](https://github.com/renatalantos/office_lunch_website/blob/main/static/documents/database%20schema/OrderLineItem%20and%20User%20Profile%20Models.pdf)
1. [SQLite3 database:](https://en.wikipedia.org/wiki/SQLite)
    - SQLite3 is Django's default database system.
1. [Cloudinary:](https://cloudinary.com/)
    - I used cloudinary for cloud-based storage of my images, so that I could give my images a linking URL when uploading them into the products json file.
   [AWS:](https://aws.amazon.com/)
   - AWS is used to store static and media files in the cloud from the project to host them for deployed application in Heroku.
   [Stripe:](https://stripe.com)
   - Handles user payments
   [Mailchimp](https://mailchimp.com/)
   - Handles form for newsletter sending
1. [Heroku:](https://www.heroku.com/)
    -  Heroku is used for the deployment and ultimate cloud-based storage of my application.

# Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every pagefor HTML and CSS of the project to ensure there were no syntax errors in the project. I used the inbuilt pylint compiler to validate the Python files.

-   [W3C URI Validator](https://validator.w3.org/#validate_by_uri)
    - See the [URI Validator Results](ADD LINK TO FOLDER)
    - Please note that I wasn't able to assign alt tags to images on the AWS server. Other errors come from the Bootstrap template in HTML. I'm most likely responsible for stray and unclosed tags and I did my best to refactor my code, however, all HTML pages show some standard errors in this project: [Standard errors:](https://github.com/renatalantos/office_lunch_website/tree/main/static/documents/validation/html)

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - See the [CSS Validator Results](https://github.com/renatalantos/office_lunch_website/blob/main/static/documents/validation/css/CSS%20Validation%20jigsaw.JPG)
-   [Gitpod Pylint](https://pylint.org/)
    - See the [Gitpod Pylint Results](https://github.com/renatalantos/office_lunch_website/tree/main/static/documents/validation/python)    
    - I'm getting two main errors on these files - "Line too long" and "Class class_name has no object member" I do not want to break the long lines as I might break the code if I'm not attentive and the other one is a standard error in Django that can be ignored when in the views and if the views are set up correctly. 

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the business.
        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero Image with Text and an "Order Food Now!" Call to action button. The name of the site is described in the logo in the upper left corner of the page. A different letter type makes the logo stand out. There is also a little sandwich favicon in the browser. Hero image and questions "Stuck in that Office? Hungry for Lunch?" make sites purpose even clearer and the "Order food now!" button reassures user that this is an online service. 
        2. The user has the option to click the call to action button or go to the navbar and select a link. Also, in the footer there is basic information about product ingredients, a newsletter signup form and links to the company's social media presence, so the user might decide to take a look.

    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        1. The site has been designed to have minimum content per page so that the user is not entrapped. The content is limited to what it says in the navigation links. Each link clearly describes what the page where the user will end up does. The navbar always displays on top of the page, and if users scrolls way down, an up arrow link enables them to get back to the top of the page, instead of having to scroll up. At every critital point of site use where user needs to make a product adding or purchasing decision, there is a button on the given page that provides an alternative so that user can leave the page. These are action buttons (Keep Shopping on product detail and basket pages and Adjust Basket on checkout (till) pages. They enable users to leave the given page but also encourage them to stay on the site. This works really well for both first time and returning users. Also, page content is rather minimalistic, it's basic information and instructions. 

    3. As a First Time Visitor, I want to sign up for a user account to access restricted content.
        1. Once the new visitor has gone through the site links, has looked at all products and individual products, has had a look at what the Login and Register pages do, they might decide to order a product. They can do this without logging in. However, if they would like to create a profile page, they must register first. The link under the user details on the checkout (till page) informs users of this. They are also unable to write reviews, but this won't make sense for the first time anyway. They cannot add products to the favourites page without registering first, either. For unregistered users the favourites button will simply display as an empty heart and won't respond to clicking.
        2. The login page sign in form contains a link where user can create an account from: "If you have not created an account yet, then please sign up first." This way users can understand that all restricted functionalities are only accessed for registered users.
        3. Alternatively, the user might want to create an account from the navbar link "Register", which will take them straight to the signup form. 
        4. Once the user signs up by creating after creating a username, optionally adding an email address, creating and repeating the password, verifying the email address and now signing in, they are redirected to the home page. 
        5. In the navbar now, the username is displayed now beside the user logo. In the dropdown list user can see the additional options Create a Profile and Favourites.
    4. As a First Time Visitor, I want to search for products, view all products, view individual product details.
        1. User can view all products when clicking on the All in Our Store link or after clicking the Order Food Now! button on the home page. If they wish to search for a product, they can click on the magnifying glass icon in the navbar. This will take them onto an extra page, which is styled like the home page, except for there is no footer. (Footer is only present on home page as it has no value to the product viewing, adding, and buying) Keyword will return match in both product description and product name. No match will return user to the all products page, with the message "0 product found for keyword "keyword".
        User can view products by sorting criteria from the dropdown-box (by price, by category, by calory count, by lifestyle choice or all products),
        Additional sort criteria (Name, Vegan, Vegetarian, Gluten-free) are added to the dropdownbox on the All products page. When there are multiple products displayed, they have labels for Lunch Deal Items (if assigned by me), category tag, product name, lifestyle choice label and product price. 
        2. Products can be viewed from the All Products page without sorting and by clicking on the product image, user can get to the individual product page. Here there is additional information to the multiple product display: calory count, whether product can be grilled at request and of course, a detailed description.
    5. As a First Time Visitor, I want to place an order.
        1. When user decides to place an order from the product detail page, they can add it into the basket. Product quantity can be increased to 99 and decreased to 1. Users can change the quantity before or after adding the product to the basket. If they change the quantity after adding product they will get a quantity update success message. Adding product to the basket will trigger a success message as well, with option to go to secure checkout for the user.
        As mentioned, user can chose to go back to browse for additional products as well. Shopping basket icon in the navbar will update when user adds a product to the basket. BAsjet page is available form here if user clicks on it, otherwise they can use the success message link to got to the checkout.
        2. If user has added the items to the basket and decides to go to the checkout page, there are given the option of either browsing for other products (Keep shopping button), updating item quantity in the quantity box beside the product and then overwrite old quantity by selected quantity by using the little pencil icon or even deleting their item. These latter user activities will trigger a success message. Detailed price and delivery charge information is also displayed. If user decides to proceed to the checkout page, he needs to fill in the checkout form with his details (personal, contact, address, delivery date). A first-time user will understand form the link under the address section that in future, he needs to log in in order to be able to save those details. Order summary details display on the right like on the basket page. User can adjust the basket from here if he decides to.

    6.  As a First Time Visitor, I want to make a safe payment.
        1. Once user got to the checkout page and entered his details, he can enter his credit card number under the order form. 
        2. This is straighforward, as there are placeholders in this form and Stripe will handle any incorrect user input and error messages will come from Stripe. If user has filled in the form correctly and the credit card details are also correct, user will get a confirmation message if order has gone through, containing user email address and a generated order number. There is a validation in place in the till models.py - past dates are not allowed for delivery. There is a hint to that in my customized error message (doublecheck delivery date). 

    7. As a First Time Visitor, I want to create a user profile, so that I can save my details and make  next-time   interaction with the site faster and easier.
        Users can see when on the checkout page, that in order to be able to save their details, they need to be logged in. They can follow the link or go to the User icon in the navbar, select Register, create a user account, verify their email address and then log back in.
        Then in the dropdown list under the user icon, they can create the profile page and when making a purchase, view their order history. 

    8.  As a First Time Visitor, I want to get feedback on all activities performed other than    viewing p  roducts. All actions are fed back to the user, successful or failed registration         (handled by allauth), login, adding, editing and deleting products in basket, checkout form handling, purchase (handled by project code). If there are items in the shopping bag while user performs another successful activity, the success message will display with the basket content and the secure checkout button. Credit card related messages are from Stripe. 

   9. As a First Time Visitor, I want to sign out of my user account at the end of the session to  keep my account related details safe. 
   User can do this through the logout button in the dropdown list under the user Icon. Success message will display after user clicked the Sign Out button.
 

-   #### Returning and Frequent Visitor Goals

    1. As a Returning and Frequent Visitor, I want to sign into my user account to access restricted content.
        1. Users can signing in from the dropdown box under the navbar's user icon. They are given access to additional activities like adding an item to favourites, adding, editing and deleting own item reviews in the product detail page and save their checkout to data to profiles. The latter can be achieved by checking the Save this delivery information to my profile box under personal details and address on the checkout form. For this functionality to work for name and email address, in the development environment the superuser needs to allow the user and the email address in the admin panel under Email addresses and Users. As mentioned above, this will give user the chance to view their order history as well from now on. This covers User Story nr 2 in User Stories, too.
    3.  As a Returning and Frequent Visitor, I want to create reviews and alternatively edit them or delete them.
        1. Reviews can be added under individual products on the product detail page. All review activities require a logged in user. 
        2. User can add a rating, title and content to their reviews and then click on "Submit Review". Review  will display on left hand side of the page, with all the information the user has entered. User can edit their reviews in a form that is in the same place as the write review form. They select Update review and the edited review appears. Successful adding and editing reviews are confirmed by a success message and so does the deleting review. However, as there is an edit and delete button assigned to each review, users will get an error message if they are trying to edit or delete a review by someone else. Superusers can add and delete reviews but have no permission to edit them.

    4. As a Returning and Frequent visitor I want to send messages and queries to the site owner.
        1. This can be achieved through the Contact Us link, where both logged in and anonymous users can fill in a conact form with name, email and content and send it. As this form currently has no custom validation, user should receive a success email if they have provided valid data. However, this form is not set up to send real emails. There is also a phone number displayed on this page.

    5. As a Returning and Frequent visitor I want to add products to my favourites list, to make reordering e easier, alternatively, I would like to delete them from there.
        1. This can be achieved by the product detail page for logged in users. If user adds a product to their favourites, a full heart will be displayed instead of the empty one and a success messages will appear. If    product is already in the favourites list, user will receive and info message. If they go into the favourites page and remove an item from there, they will receive an info message also.

    6. As a Returning and Frequent Visitor, I want to subscribe to the companies newsletter to find out about new products and deals.
        1. User should go into the footer and submit their email address. This functionality works with MailChimp.
        User will get a customized message from mailchimp.
    7. As a Returning and Frequent Visitor, I want to sign out of my account at the end of the session to keep my account safe.
        1. This process has been described above.
    8. As a Returning and Frequent Visitor, I want to get feedback on all activities performed other than viewing products.
        1. As mentioned, customer is fed back all add, edit, delete functionality.


-   #### Site Administrator Goals

    1. As a Site Administrator I would like to be able to add, view, edit and delete products.
        1. Site administrator have superuser access. When they log in, they can see a Product Management Link in their prodown under the user icon. They navigate to a product form that contains all product information as described in the model. They can upload files here. Editing and deleting happens though the product pages. The edit/ delete product functionalities are only displayed for superusers.
    1. As a Site Administrator I would like to be able to create, view, and delete reviews.
        1. This is the same for site administrators as for any other user. It happens through the same review form and buttons. Their reviews are displayed just as well. Superusers have full CRUD functionalities for their own products, however, they cannot edit other users' products. They can delete them, however. 
### Further Testing

-   The Website was tested on Google Chrome, Firefox, Microsoft Edge, Opera and Internet Explorer browsers. The site renders fine in all browsers. In IE the body fonts revert from Lora to Times New Roman.
-   The website was viewed on a variety of devices such as Desktop, Laptop, Samsung Galaxy A51 and Google Developer Tools. It is responsive on all devices and all features work as expected.
-   A large amount of testing was done to ensure that all pages were linking correctly. - See Testing User Stories
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Unresolved Bugs

-   #### In general
    1. At the moment all features of the product work as expected. However, the added 505 and 404 pages luckily 
    haven't presented themselves yet. In my understanding, these must just be added to the root folder templates and django will pick them up if necessary. 
    #### Errors in development
    1. Most errors I got were fairly common and could be troubleshooted through Slack or StackOverflow. However, 
    I got a CircularImport error when creating the Review model twice. This issue was resolved by the help of my mentor.
 
    
# Deployment

### Heroku

The project was created in Github first and then transferred to the Gitpod development environment by the use of the green Gitpod button.

## Initial Deployment  
- ### When creating a Django project, it is highly advisable to deploy early, due to the compexities of the development process and the actual application.

1. In the Gitpod environment a skeleton django project was created (project, app and relating files).
2. A Heroku app was created in Heroku.
3. In Heroku, under the Resources tab, in Add-ons, I searched for Postgres. When found I submitted a request to use it. 
This attached Heroku Postgres to my project in Heroku.
4. In the Heroku Settings tab I clicked on "Reveal Config Vars" and copied the automatically added postgres link from beside the DATABASE_URL variable. 
5. In Gitpod dev environment, I installed dj_database_url, and psycopg2. I froze these in requirements.txt.
6. In Gitpod settings.py I imported dj_database_url.

7. Still in the settings.py file, I commented out the present code to replace the default database with a call to dj_database_url.parse.
8. I gave it the database URL from Heroku.
9. I migrated these changes in Gitpod using python3 manage.py migrate.

10. I imported all my product data, to be able to use the fixtures again by first loading in the categories and then the products.
11. I created superuser for Heroku in Gitpod using python3 manage.py create superuser
12. I removed the Heroku database config by commenting it and commenting out the original database.
13. I used an if statement in settings.py so that when the app is running on Heroku the database connects to Postgres and otherwise, it connects to sqlite.
14. I installed gunicorn to act as web server, froze it and added it the relating code.
15. I created a Procfile so that it can run gunicorn.
16. I also added DISABLE_COLLECTATIC = 1 to the Heroku config vars. 
17. I added the Heroku name followed by herokuapp.com to the ALLOWED_HOSTS variable name in settings.py, followed by a comma and 'localhost' (to allow running in the development environment).
15. I added cloudinary and cloudinary_storage to the installed apps in settings.py. 
16. I set up the static file storage, static file directory, the static root, the media url, the default file storage and the templates directory in settings.py.
17. I added the Heroku name followed by herokuapp.com to the ALLOWED_HOSTS variable name in settings.py, followed by a comma and 'localhost' (to allow running in the development environment).
18. I did a git push.
19. I did a git push heroku main to deploy to Heroku.
20. I generated a secret key, and added it to my config variables in Heroku.
21. In settings.py, I replaced the secret key setting with the call to get it from the environment.
22. In the Deployment tab in Heroku, in Deployment method, I added Github, set up Enable Automated Deployment, looked for my Github repository, connected my Heroku app to it and clicked on Deploy Branch at the bottom of the page.
23. I did a git push.
24. I set up an AWS account.
25. I created an AWS bucket there.
26. I generated a policy and added this policy into the bucket policy editor with /*.
27. I saved these changes.
28. I created a group called renatalantos-office-lunches.
28. I created an access policy giving the group access to the s3 bucket.
29. I attached the policy to the user group.
30. I creted user.
31. I downloaded the CSV file containing this user's access key and secret access key.
32. In Gitpod I installed boto3 and django-storages and froze them.
33. I added storages to installed apps.
34. I added AWS variables to Heroku.
35. I added AWS variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY (from csv file) to Heroku.
36. I added USE_AWS to Heroku with value True.
37. I set up if statement in settings to AWS if not in development environment.
38. I created custom_storages.py in Gitpod, poulated by code by instructor.
39. I set up static and media urls for AWS use in settings.py.
40. I added AWS_S3_OBJECT_PARAMETERS in settings.py.
41. I did a git push.
42. I created a media folder in AWS and uploaded my image files manually.
43. I added Stripe variables to Heroku (STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET)

# [Search Engine Optimization and Marketing](#SEO) a
### Techniques Implemented

- I used meta keywords relating to my site in the base.html head Included were site profile, products and location.
- I used the Facebook site template provided by CI [Facebook](https://github.com/renatalantos/office_lunch_website/tree/main/static/documents/facebook)
- I included the built-in Mailchimp logo with the Mailchimp newsletter form as a link to another site. I added the nollow link to this as it is not related to the site.
- I included Sitemap.xml and robots.txt files.
- for handling Nonexistent Content and User Errors I added 404.html and 505.html error pages in the root directory templates folder.


# Credits

### Code

-   The structure and the code of the project was almost based on two project walkthroughs by Code Institute:
    * Boutique Ado - I created all functionalities based on this walkthrough.
    * I was given a helping hand by my classmates Moira and Siobhan. The add to favourites functionality comes from Moira, and I could fix the bug with the quantity buttons thanks to Siobhan. I cannot claim these solutions as my own.

-   [Bootstrap5 Template](https://startbootstrap.com/templates/ecommerce),
-   [Bootstrap5 Template](https://startbootstrap.com/template/shop-item)
-   [Bootstrap5 Template](https://startbootstrap.com/theme/agency)
-   Bootstrap Theme used throughout the project  to style pages and make site responsive.
-   [Official Django Documentation](https://docs.djangoproject.com/en/3.2/) was researched for syntax, code expressions, code functionalities.

-   Stack Overflow and Slack was was researched for syntax, code expressions, code functionalities, problem solving. Validation function for reservation date and time is from there.
-   I contacted Tutor Support on a few occasions while 
-   My mentor helped me implement adding reviws.

-   How to implement widgets for form fields was answered by tutor on FullStack Slack channel.


### Content

-   Content comes from the Bootstrap template, I made slight changes to the prewritten content there.


### Media

-   Images are from pexels.com and from the Bootstrap template.
### Acknowledgements

-   My Mentor Rohit for continuous helpful feedback.
-   Kasia for supporting all of us in all circumstances and for being available for individual support.
-   My classmates for their ongoing support and solidarity, I mentioned two of them, but all do deserve praise and acknowledgement.
-   My children for their patience. Thanks for putting up with me in these intense times.