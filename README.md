**Project Documentation ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.001.png)**

This documentation outlines the steps required to set up a Django project with FastAPI integration, process data from a CSV file using Jupyter and Pandas then import the data into a PostgreSQL database. 

**Prerequisites** 

1. **Python 3.12.3** ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.002.png)
1. **PostgreSQL Database** 

**Installation and Setup ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.003.png)**

**Step 1: Install Python 3.12.3** 

1.  Download and install Python 3.12.3 from the official Python website. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.004.png)

**Step 2: Install Django ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.005.png)**

1. Open a terminal or command prompt. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.006.png)
1. Run the command: **py -m pip install Django==5.0.6**. 

**Data Processing ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.007.png)**

**Step 1: Install Jupyter and Pandas** 

1. Activate your Python environment. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.008.png)
1. Run the command: **pip install jupyter pandas**. 

**Step 2: Process the CSV File ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.009.png)**

1. Create a new Jupyter notebook. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.010.png)
1. Use Pandas to process your CSV file. 
1. Importing Data into PostgreSQL from clean_food_truck.csv

**Step 1: Create a Django Project![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.011.png)** 

1.  Run the command: **django-admin startproject myproject**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.012.png)

**Step 2: Open the Project in PyCharm (IDE) ![ref1]**

1.  Open the newly created project in PyCharm. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.014.png)

**Step 3: Create a Virtual Environment ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.015.png)**

1.  Run the command: **python -m venv venv**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.016.png)

**Step 4: Activate the Virtual Environment ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.017.png)**

1. For Windows: **venv\Scripts\activate** ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.018.png)
1. For macOS/Linux: **source venv/bin/activate**

**Step 5: Install Required Packages ![ref2]**

1.  Run the command: **pip install fastapi django pydantic uvicorn ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.020.png)psycopg2-binary pandas aiofiles**. 

**Step 6: Start a New Django App ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.021.png)**

1.  Run the command: **python manage.py startapp food\_truck\_finder**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.022.png)

**Step 7: Configure settings.py![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.023.png)**

1. Add **food\_truck\_finder** to **INSTALLED\_APPS**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.024.png)
1. Configure the database settings for PostgreSQL. 
1. Set the **STATIC\_URL**. 

**Step 8: Create main.py for FastAPI App ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.025.png)**

1. Create a **main.py** file in the root of your project. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.026.png)
1. Set up the FastAPI app and Django environment in **main.py**. 

**Step 9: Create models.py in Your App ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.027.png)**

1.  Define the models according to the structure of the CSV file in ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.028.png)**models.py**. 

**Step 10: Make Migrations ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.029.png)**

1.  Run the command: **python manage.py makemigrations**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.030.png)

**Step 11: Apply Migrations ![ref1]**

1.  Run the command: **python manage.py migrate**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.031.png)

**Step 12: Create schema.py for Output ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.032.png)**

1.  Define the Pydantic models for the FastAPI output in **schema.py**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.033.png)

**Step 13: Create controller.py for Logic ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.034.png)**

1.  Implement the logic to handle data processing and API endpoints in ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.035.png)**controller.py**. 

**Step 14: Create Static Directory for Frontend ![ref2]**

1. Create a **static** directory in your project root. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.036.png)
1. Inside the **static** directory, create **index.html**, **app.js**, and **styles.css** for the frontend. 

**Step 15: Run the App Locally ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.037.png)**

1.  Run the command: **uvicorn main:app**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.038.png)

**Step 16: Access the Frontend ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.039.png)**

1. Open your browser and navigate to: **http://127.0.0.1:8000/**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.040.png)
1. Enter the latitude and longitude for finding the food truck on the map. 

![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.041.jpeg)

**Step 17: Access Swagger UI for API Documentation ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.042.png)**

1. Open your browser and navigate to: **http://127.0.0.1:8000/docs**. ![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.043.png)
1. Enter the latitude and longitude for finding the food truck as JSON output. 

![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.044.jpeg)

![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.045.jpeg)

![](Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.046.jpeg)

[ref1]: Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.013.png
[ref2]: Aspose.Words.d8d404f8-2adf-43eb-b1c9-0744cb870893.019.png
