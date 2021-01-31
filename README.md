# choco_project [last update: 31.01.2021]
choco_project is REST API designed for working with products price informaion from shops like "sulpak.kz", "technodom.kz", "mechta.kz", "shop.kz". Project is developed as a part of the software engineering internship in Chocofamily Holding.

## Project structure:
<pre>
.                                                                 
├── choco_project               # Project settings files    
    └── <em>to be filled soon...</em>                         
├── myapi                       # REST API related files
    └── <em>to be filled soon...</em>    
├── .gitignore                  # .gitignore file      
├── celery.logs                 # Celery logs      
├── celerybeat-schedule         # Celery schedule (auto-generated)             
├── docker-compose.yml          # .yml file for docker-compose
├── Dockerfile                  # Dockerfile                      
├── manage.py                   # Django project manager                  
├── README.md                   # <-- you are here                
└── requirements.txt            # Python requirements       
</pre>      

## How to run:

1. Clone the repository:
```
git clone https://github.com/Rainhunter13/choco_project
```

2. Set project configurations:  <br/>
  2.1. Create PostgreSQL database and define related settings in the /choco_project/settings.py  <br/>
  2.2. Create config.py file in the root directory and define 'SECRET_KEY' (Django project key) and 'db_password' variables (PostgresQL database password)  <br/>
  2.3. Put the BigQuery credentials *file_name*.json file in the root directory and set a path to it in the updater.py  <br/>
  2.4. Download and put the encoder_model folder in the root directory - Universal Sentense Encoding model which could be downloaded from https://tfhub.dev/google/universal-sentence-encoder/4  <br/>

3. Run docker-compose:
```
sudo docker-compose up --build
```

## Usage:

### Application capabilities
With choco_project you could easily keep track of product prices for specific products you need. Products are availabale in 4 categories - "laptop", "tablet", "monitor", "eBook" from 4 shops "sulpak.kz", "technodom.kz", "mechta.kz", "shop.kz". Product information contains information such as product name, category, and prices for different dates and time slots. Prices are checked once an hour and updated when needed. You are also able to search for the cheapest or most expensive product in specific category. Currently avaialable categories are: 'laptop', 'tablet', 'monitor', 'eBook', 'fridge', 'freezer', 'electric_stoves', 'multicooker', 'meet_grinder', 'microwave'.

### REST API endpoints

1. Product list:
- Route: ``` /api/product ```
- Method: GET
- Response: Product object list

2. Specific product information:
- Route: ``` /api/product/{id} ```
- Method: GET
- Response: Product object

3. Product list from specific shop:
- Route: ``` /api/{shop} ```
- Method: GET
- Response: Product object list

4. Specific product information from specific shop:
- Route: ``` /api/{shop}/{id} ```
- Method: GET
- Response: Product object

5. Product List of specific category:
- Route: ``` /{category} ```
- Method: GET
- Response: Product object list

6. Cheapest product from specific category:
- Route: ``` /{category}/min_price ```
- Method: GET
- Response: Product object

7. Most expensive product from specific category:
- Route: ``` /{category}/max_price ```
- Method: GET
- Response: Product object

## Implementation details:
- The project is developed with Django Rest Framework connected to the PostgreSQL database. 
- Celery task queue is used to make periodical price updates. 
- Parsers are implemented with python requests, selenium and beatifioul soup libraries.
- Docker Compose is set for the easy outside-of-the-box project execution.
- Products from different shops are checked for similarity and merged when needed by using Universal Sentence Encoder and Cosine Similarity algorithms. 
- Filtered data is transfered to the Google BigQuery analytic cloud database. Top 3 cheapest and most expensive products are accessible with the Standard SQL Queries written in the BigQuery Console.
- Logs of celery tasks are put in the celery.logs file.
- Project is developed with Git VCS.

## Current limitations:
- parsing functionality is not finished for "technodom.kz" -> currently disabled
- parsing functionality for "sulpak.kz" lugs when running inside docker -> currently disabled
