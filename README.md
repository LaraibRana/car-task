# Car Registration Assesment Task
# Flask app with Marshmallow Schemas

### Use-Case
You have been given a real world challenge to generate reports on registration of cars. Let’s
suppose a small startup wants to build this app which would help the end user to search and view
the reports generated. Let’s suppose you got the opportunity to join this startup as a backend
Intern. You must provide clear and complete documentation about how to run your program. You
should be able to handle different routes in your app. The following features Restful APIs
implementation is given to you as a first task to implement.


### Requirements

#### Functional Requirements
Following are the functions which the application will be able to perform.
* **User Register and Login**
The User will be able to register to this app by providing his/her email or password. And with the same email/password, the person will be able to login to this app.
* **Sync data to localdatabase:**
Using the URL provided above, make automated calls once a
day to retrieve and store data into a local relational database. You only need to maintain a
data set for the last 10 years i.e. 2012-2022. This operation should be performed as a
background task. Keep in mind that discovered data should only update & not overwrite
the current data stored. 

* **Search car based on year, model and make**
User will be able to search the car based on above fields.
* **Marshmallow  Json Validation**
All of the API's will be validated through marshmallow schemas
#### Requirements

### Detail Design and Architecture
The application include mysql database for development phase.
 
### Environment setup

#### **Step-1** Clone the repo

```
# git clone project
https://github.com/LaraibRana/car-task.git
```
#### **Step-2** Python-vitual environment and dependencies installation

```
# create app-env python-virtual environment
python3 -m venv app-env

# to install the required packages
pip install -r requirements
```

#### **Step-3** Activate python-virtual environment (venv)
```
# 
source venc/bin/activate
```

#### **Run application
```

#run app
 pyhton main_app.py

```
