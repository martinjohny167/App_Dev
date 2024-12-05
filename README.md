# Job Portal Project Using Python 

We have developed a fully functional web application using python as backend with SQL Server database and HTML and bootstrap for frontend.
We have created several views for all functions in views.py.
Testing are done and all the test cases for user master, candidate and company models are added tests.py file.

## Modules and basic functions:
	Employee – View the Job posts and can apply for the jobs. 
	Employer – Post Jobs and view them.
	Admin   - Delete and update users. 
	
## Steps to be followed to run the application :

- Before running the application make sure that you installed all the requirements given in requirement.txt <br />
- Go to settings.py and change the database connection details to your server.<br />
	```
	 DATABASES = {
    	  'default': {
          'ENGINE': 'mssql',
          'NAME': 'Database Name',
          'USER': 'User Name',
          'PASSWORD': 'Password',    
          'HOST': 'Server Name',
          'PORT': '',

          'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
                     },
    	            },
	           }
	```
- For running the application: <br />
	```
	python manage.py runserver
	```
## Commands for Database Migrations if any changes needed(Optional):

```
python manage.py makemigrations <app-name>
python manage.py migrate
```

## Command for Test the application :
```
python manage.py test

```
## Dive into application features :

- Either select as company or candidate and register with details, if you are already registered go with login. <br />
- Login to the application either as company or candidate with user credentials.<br />
- If loggined as candidate(employee) :
	- Update profile if needed which includes updation of resume, profile photo,contact,address etc
	- Candidate can check the Job listing and can apply for interested jobs.
- If loggined as Company(Employer)
	- View the dashboard
	- Update profile if required which includes updation of company contact,address,company logo etc
	- Can post jobs by using Post a Job option in the sidebar
	- View application lists by checking the Application List option in the sidebar
	- View the posted jobs by selecting the Job Lists option
- If the admin want to login,go to /adminloginpage and have to use admin credentials(username : admin, password : admin)
	- Admin can view the dashboard
	- View the users list by selecting the Users List option in the sidebar and can manage(delete) the users if needed
	- Admin can view the company list by selecting the Company List option in the sidebar and can manage(delete,update) campanies if needed 

# Detailed explanation
Modules and Features

1. Employee (Candidate)

Register as a candidate and update your profile with resume, profile photo, contact information, and address.
Explore job listings and apply for positions that match your skills and interests.

2. Employer (Company)

Post job openings and manage them through a dynamic dashboard.
Update your company profile, including contact information, address, and logo.
Review and manage job applications received.

3. Administrator
Access an admin-specific login portal at /adminloginpage.
Manage users and companies by viewing, updating, or deleting them as needed.
Oversee the platform through an admin dashboard.

Setup and Installation
Follow these steps to set up the application on your local machine:

Install Python and SQL Server: Ensure Python 3.x and SQL Server are installed on your system.

Clone the Repository:



git clone <repository-url>  
cd job-portal  

Install Dependencies:


pip install -r requirements.txt  

Set Up the Database Configuration: Update settings.py with your server details (see the Database Configuration section).

#Database Configuration
To connect the application to your SQL Server database, modify the DATABASES setting in settings.py as follows:
*already connected to cloud hosed database 

DATABASES = {  
    'default': {  
        'ENGINE': 'mssql',  
        'NAME': '<Database Name>',  
        'USER': '<User Name>',  
        'PASSWORD': '<Password>',    
        'HOST': '<Server Name>',  
        'PORT': '',  
        'OPTIONS': {  
            'driver': 'ODBC Driver 17 for SQL Server',  
        },  
    },  
}  
#Running the Application
After completing the setup:

Run the server:

python manage.py runserver
  
Open a web browser and navigate to http://127.0.0.1:8000.

Database Migration Commands

#For any changes made to database models, run the following commands:


python manage.py makemigrations <app-name>  
python manage.py migrate  
Testing the Application
To validate the application's functionality, run the test suite:


python manage.py test
  
#Covered Test Cases:

User registration and authentication.
Job application process.
Admin management features.
Dive into Application Features
For Employees (Candidates)
Register or log in with your credentials.

Update your profile, including uploading a resume and profile picture.
Explore job listings and apply for positions that suit your expertise.

#For Employers (Companies)

Register or log in to access the employer dashboard.
Post job openings and manage them effectively.

Review job applications and interact with potential candidates.

#For Administrators

Log in to the admin portal using the credentials (username: admin, password: admin).
Manage user accounts and company profiles.
Monitor platform activity through the admin dashboard.1	
	

