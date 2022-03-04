# Task Manager #
A simple tool to help you get an overview of the workload.

![mockup](static/images/wireframes/mockup.png)

View the live site [here](#).  

Username and password for Admin: Admin - Admin


## Table of contents ##

* [UX](#ux)
    * [Introduction & Project Goals](#introduction--project-goals)
    * [User Stories](#user-stories)
    * [Development Planes](#development-planes)
    * [Skeleton](#skeleton)
    * [Design](#design)
    * [Features](#features)
* [Technologies](#technologies)
    * [Languages](#languages)
    * [Tools](#tools)
    * [Libraries](#libraries)
    * [Database Management](#database-management)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credit](#credit)
* [Acknowledgements](#acknowledgements)
---

## UX ##

### Introduction & Project Goals ###

Task Manager is a simple way to keep a comprehensive overview of the workload. It`s divided into different departments, but all departments can see all tasks on every department and also create a new task on the appropriate department.

The Project Goal is to make the days at the office more easy and transparent across the different departments. 

This is the third of four Milestone Projects the developer needs to complite, to achieve the Diploma in Software Development.

The main requirements on this project was to build a full-stack website, where users could manage a common dataset, using **HTML5**, **CSS3**, **JavaScript**, **Python**, **Flask** and **MongoDB**.

---
### User Stories ###

* As a general user I want to:

    * Se a simple application with calm colors without a lot of distractions
    * Se the workload accross the departments
    * See who made the task 
    * Have the opportunity to Sign Up for access to more features

* As a logged in user, in addition to the general above, I want to: 

    * Be able to create tasks on the department of my own choice
    * Edit and delete tasks created by me
    * See my created tasks on my profile page

* As an Admin user, in addition to the above, I want to:

    * Create a new department
    * Edit department
    * Delete department

---
### User Goals ###

* A simple Task Manager to keep track of the workload with the easy-to-use management system, using the basic **CRUD** functions: Create, Read, Update and Delete. 

    * Create Tasks
    * See all Tasks
    * Update Tasks
    * Delete Tasks

---
### Site Owner Goals ###

* Develop a tool to make the workdays more easy and transparent

 * The user feels included
 * The user have the opportunity to update on workload
 * The user gets a simpler and more clear workday

---
### Development Planes ###

In order to create an application that fulfilled the expectations as described above, the developer used her experience from her daily work.

---
### Strategy ###

Divided into three categories, the website will focus on the following target audiences:

* ### Roles: ###

    * Regular employees in all departments
    * Leaders in all departments
    * Top leaders
    * Business owners

* ### Demographic: ###

    * Newly hired
    * Old trotters
    * Likes to stay up to date

* ### Psychographics: ###

    * Organised
    * Structured
    * Work culture

---
### Scope ###

---
#### User Requirements And Expectations ####

* Content that is visually appealing with calm colors
* Content is well structured
* Easy to navigate the application using the respective buttons  
* Easy to understand how to use the application
* Easy to read typography
* Operational link to **GitHub**, **Slack** and **LinkedIn** that opens in a new tab  
* Opportunity to Sign In
* Opportunity to create, edit and delete own tasks
* Tasks have a descreption and due date
* See all tasks accross departments
* Admin user has the opportunity to mange the departments

---
### Skeleton ###

Wireframes was made in [Balsamiq](https://balsamiq.com/). As in previous projects feedback on using [Figma](https://www.figma.com/), was that Balsamiq was a better choice.

### Design for mobile device: ###

![all_tasks_landingp_mob](static/images/wireframes/all_tasks_landingp_mob.png)
![sign_up_mob](static/images/wireframes/sign_up_mob.png)
![sign_in_mob](static/images/wireframes/sign_in_mob.png)
![create_task_mob](static/images/wireframes/create_task_mob.png)
![manage_dep_mob](static/images/wireframes/manage_dep_mob.png)
![add_dep_mob](static/images/wireframes/add_dep_mob.png)

### Design for desktop device: ###

![all_tasks_landingp_desk](static/images/wireframes/all_tasks_landingp_desk.png)
![sign_up_desk](static/images/wireframes/sign_up_desk.png)
![sign_in_desk](static/images/wireframes/sign_in_desk.png)
![create_task_desk](static/images/wireframes/create_task_desk.png)
![manage_dep_desk](static/images/wireframes/manage_dep_desk.png)
![add_dep_desk](static/images/wireframes/add_dep_desk.png)

---
### Changes from wireframes to live site ###

First it was thought that each page would have different background image, but the developer thought the coffee-bean background was great on all pages to keep it consistent. The developer also desided to make a profile page, so that the signed in user have the opportunity to see only the tasks created by them.

---
### Design ###

The design of this application has been created based on a "keep it simple" mindset. It has a lot of different user personalities, and it is not an application to hang out on. The users is at work, and it is a quick in and out application. Calm colors without distractions and unnecessary content. 

When entering the application you immediately see all tasks, the user does not have to sign up / in unless they want to create, edit or delete a task. 

[Jinja](https://jinja.palletsprojects.com/) was used to extend the `base.html` page, for consistency accross all pages.

---
* Fonts

[Google Fonts](https://fonts.google.com/specimen/Roboto): Roboto, sans-serif.
This Font is used because it is a clean and simple Font. 

![roboto_sansserif](static/images/wireframes/roboto_sansserif.png)

* Icons

[Fontawsome](https://fontawesome.com/) provided all the icons used in the application.

---
* Colours

All the colours where picked to ensure a calm and harmonious impression. 

    * Navbar, Footer and Containers: Silver Pink, #bcaaa4
    * Buttons : Isabeline, #efebe9 and Cinereous, #a1887f
    * Text and Icons: White, #fff and Isabeline, #efebe9
    * Collapsible and dropdown: Cinereous, #a1887f
    * Hover: Pale Silver, d7ccc8
    
Color Sheme from [Coolors](https://coolors.co/)
![color_sheme](static/images/wireframes/color_sheme.png)

---
### Features ###

The web application has a responsive layout with a reverse mindset relative to the mobile-first way of thinking, as it will be used at the office, and desktop screen.
But of course it can also be used from a phone.

Features that have been implemented:

* Search Tasks
* Sign Up
* Sign In
* Create, edit and delete Tasks
* Create, edit and delete Departments
* Profile Page

* Flash messages if username exists or wrong password 
* Flash messages when logged in or out
* Flash messages when manage tasks or departments

* Custom 404 Page
* Custom 500 Page
* Favicon

* Links to the developers **GitHub** and **LinkedIn**
* General link to **Slack**, just because it is amazing

Features that will be implemented in the future:

* Sort Tasks by date
* See how many tasks that been solved
* Assign tasks to another user
* Warning when delete, and confirm button
* Anonnymous suggestion function
---
### Technologies ###

---
### Languages ###

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://no.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---
### Tools ###

* [Git](https://git-scm.com/)   
Git was used for version control by utilizing the GitPod terminal to commit to Git and push to Heroku and GitHub.

* [GitHub](https://github.com/)   
GitHub was used to store the project after pushing from Gitpod.

* [Heroku](https://id.heroku.com/)  
Heroku was used to deploy the website.

* [Balsamiq](https://balsamiq.com/)  
Balsamiq was used to create wireframes before starting on the project.

* [Am I Responsive?](http://ami.responsivedesign.is/)   
Am I Responsive? Was used througout the building of the project to make sure the it was responsive, and also for the Mockup.

* [Font Awsome](https://fontawesome.com/)   
Font Awsome was used to get all the icons on the website.

* [Unsplash](https://unsplash.com/)  
Unsplash was used to get the background image and the error image for error pages. 

* [Favicon](https://favicon.io/)    
Favicon was used to make the Favicon Image.

* [Black](https://black.vercel.app/)    
Black Playground, Python code formatter.

* [jShint](https://jshint.com/)  
Used to validate JavaScript code.

---
### Libraries ###

* [Materialize](https://materializecss.com/)    
Materialize was used for responsivenes along with custom components.

* [jquery](https://jquery.com/)  
jquery was used along with Materialize for installation of CSS components.

* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)    
Werkzeug is a comprehensive WSGI web application library

* [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))  
Flask was used as the web framework.

* [ItsDangerous](https://palletsprojects.com/p/itsdangerous/)   
Its Dangerous allows data to safely be sent and received using Python secret keys.

* [PyMongo](https://pymongo.readthedocs.io/en/stable/)   
Containing tools for working with MongoDB

* [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)   
Flask-PyMongo bridges Flask and PyMongo.

* [BSON](https://bsonspec.org/)  
This is a required dependency for MongoDB management system.

* [Jinja](https://palletsprojects.com/p/jinja/)  
Full-featured template engine for Python, used to extend from `base.html`.

---
### Database Management ###

* [MongoDB](https://en.wikipedia.org/wiki/MongoDB)   
MongoDB was the chosen NoSQL database for this project.

* [MongoDB Atlas](https://www.mongodb.com/atlas/database)   
MongoDB Atlas used to host the database in the cloud.

---
### Testing ###

The whole test process can be seen in the [TESTING.md](TESTING.md) file.

---
### Bugs ###

Bugs are stored in the [TESTING.md](TESTING.md) file.

---
### Deployment ###


---
### Credit ###

The developer has used previous README.md files from MS1 and MS2 as an inspiration. Also previos projects, and The Walkthroug Project with [Tim Nelson](https://www.youtube.com/watch?v=y72Dq3GRxhc).

Mentor Sandeep Aggarwal was really helpful with the bug related to not get the search function to work. As well as tips and tricks along the way.

Images

Background image by: [Justus Menke](https://unsplash.com/@justusmenke?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/coffee-beans?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Error image by: [Daniel Tatfjord](https://unsplash.com/@danieltafjord?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/broken-coffee-cup?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

---
### Acknowledgements ###

* My Mentor - Sandeep. He is really amazing to speak with. He is easy to understand, solution oriented and always in a good mood. He is also good at giving feedback on what could have been done in a better way for another time. Really feel I learned a lot from our sessions. He is also good at motivation, and tell me what is good. Really appreciate him!

* My kids and husband for their patience. The fact that they let me do this, I really appreciate it. My husband also participated in the user testing.

* My friends and family for support, and participation in the user testing. 

