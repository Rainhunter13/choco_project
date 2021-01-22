# choco_project
choco_project is a backend application designed for receiving products information from shops like "sulpak.kz", "technodom.kz", "mechta.kz", "shop.kz" and processing that data to the REST API endpoints. Project is developed as part of the software engineering internship in Chocofamily Holding.

## current progress [last update: 22.01.2021 -11:39]
Please note that the application is not fully ready to production. Whole **aimed** functionality is described in next sections, however some tasks are still in development and the **limitations** for current version are as follow:
- parsing functionality is _not_ finished for "techndom.kz"
- parsing functionality for "sulpak.kz" lugs when running inside docker

## application capabilities
With choco_project you could easily keep track of product prices for specific products you need. Products are availabale in 4 categories - "laptop", "tablet", "monitor", "eBook" from 4 shops "sulpak.kz", "technodom.kz", "mechta.kz", "shop.kz". Product information contains information such as product name, category, and prices from 4 shops for different dates and time slots. Prices are checked once an hour and updated when needed. You are also able to searhc for the cheaest or most expensive product in specific category. Currently avaialable categories are: [laptop, tablet, monitor, eBook, fridge, freezer

## installation
To install the application on your computer, first clone repository from github with the following command: <br/>
&nbsp;&nbsp;  **git clone https://github.com/Rainhunter13/choco_project** <br/>
Now, you could run the application with a single command from project root directory: <br/>
&nbsp;&nbsp;  **sudo docker-compose -up --build** <br/>
NOTE: To successfully run the application, you need to put some additional files to the root directory which are not located inside github package due to private reasons:
- config.py with two parameters set: SECRET_KEY which is a key for django application and db_password which is a password for you account in PostgreSQL. (Change other database related condigurations in settings.py)
- *.json: credentials file for authorization to Big Query database (also set the path to it inside updater.py)
- encoder_model directory: a universal sentence encoding model used for recognizing similar products - you could download it from https://tfhub.dev/google/universal-sentence-encoder/4
You can change running options by editing /choco_project/settings.py file and running the docker command again. For more information on this, please look at Django official documentation: https://docs.djangoproject.com/en/3.1/ref/settings/

## usage
Now you can connect to the choco_project REST API and work with the data given.
- To access all products list, go to /api/product
- To access specific product information, go to /api/product/{id}
- To access all products list from specific shop, go to /api/{shop}
- To access all products list from specific shop, go to /api/{shop}
- To access specific product information from specific shop, go to /api/{shop}/{id}
- To access all products list from specific category, go to /{category}
- To acces the product with minimum price in the category, go to /{category}/min_price
- To acces the product with maximum price in the category, go to /{category}/max_price
Note that only GET requests are allowed on these endpoints.

## implementation details
The project is developed with Django Rest Framework connected to the PostgreSQL database. Celery task queue is used to make periodical price updates. Parsers are implemented with python request library and selenium python package using Google Chrome driver.
Docker files are set for the easy outside-of-the-box project execution.
Products from different shops are checked for similarity and merged when needed by using Universal Sentence Encoder and Cosine Similarity algorithms. 
Sorted data is transfered to the Google Big Query analytic cloud database. Top 3 max and min products are accessible with the Standard SQL Query written in the Big Query Console.
Logs of celery tasks are put in the celery.logs file.
For more detials, please look on the project files.
