import pymysql
from dotenv import load_dotenv
import os
import requests

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT"))
    )

def read_customer(customer_id):
    url = f"http://3.227.130.252:5000/get_customer/{customer_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()