# choco_project
choco_project is a backend application designed for receiving products information from shops like "sulpak.kz", "technodom.kz", "mechta.kz", "shop.kz" and processing that data to the REST API endpoints. Project is developed as part of the software engineering internship in Chocofamily Holding.

## current progress [last update: 10.01.2021 - 4:20]
Please note that the application is not fully ready to production. Whole **aimed** functionality is described in next sections, however some tasks are still in development and the **limitations** for current version are as follow:
- parsing functionality is implemented _only_ for "sulpak.kz" shop
- celery queue is not connected, so parsing tasks are _not_ yet periodically managed
However, REST API is ready for the usage.

## application capabilities
With choco_project you could easily keep track of product prices for specific products you need. Products are availabale in 4 categories - "laptop", "tablet", "monitor", "eBook" from 4 shops "sulpak.kz", "technodom.kz", "mechta.kz", "shop.kz".
Product information contains information such as product name, category, description and prices from 4 shops for different dates and time slots. Prices are checked once an hour and updated when needed.

## installation
To install the application on your computer, first clone repository from github with the following command: <br/>
&nbsp;&nbsp;  git clone https://github.com/Rainhunter13/choco_project <br/>
You will need to install dependence packages on your local environment, you could do that with follwoing pip command based on requirements.txt file in the root folder: <br/>
&nbsp;&nbsp;  pip install -r /path/to/requirements.txt <br/>
Also, you need to have a Google Chrome installed on you machine. After installation, you would need to specify the Chrome verison in requirements.py file inside /myapi folder. *This is required for the proper work of Chrome webdriver used for parsing producs information.*
After that you can run the project on your machine with command: <br/>
&nbsp;&nbsp;  python manage.py runserver <br/>
You can change running options by editing /choco_project/settings.py file. For more information on this, please look at Django official documentation: https://docs.djangoproject.com/en/3.1/ref/settings/

## usage
Now you can connect to the choco_project REST API and work with data.
- To access all products list, go to /product route
- To access specific product information, go to /product/{id} route (product id could be checked in the product list information at /product)
Note that only GET request is allowed on these endpoints.

## implementation details
The project is developed with Django Rest Framework connected to the PostgreSQL database. Celery task queue is used to make periodical price updates. Parsers are implemented with selenium python package using Google Chrome driver. On more details, please look at project files.
