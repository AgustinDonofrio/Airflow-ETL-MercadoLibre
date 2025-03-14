# script para consultar api de mercado libre
import os
from dotenv import load_dotenv
import requests
import json
import datetime

# Cargar variables de entorno
load_dotenv()

# Obtener el access token de la api de mercado libre
access_token = os.getenv("ACCESS_TOKEN")
if not access_token:
    raise ValueError("ACCESS_TOKEN no está definido en el archivo .env")

# Header para la consulta
headers = {
    "Authorization": f"Bearer {access_token}"
}

DATE=str(datetime.date.today())

def get_most_relevant_items_for_category(category):
    url = f"https://api.mercadolibre.com/sites/MLA/search?category={category}#json"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("results", [])
        with open('/opt/airflow/tmp/file.tsv', 'w', encoding="utf-8") as file:
            for item in data:
                _id = get_key_from_item(item, "id")
                site_id = get_key_from_item(item, "site_id")
                title = get_key_from_item(item, "title")
                price = get_key_from_item(item, "price")
                thumbnail = get_key_from_item(item, "thumbnail")
                
                print(f"{_id}\t{site_id}\t{title}\t{price}\t{thumbnail}\t{DATE}")
                file.write(f"{_id}\t{site_id}\t{title}\t{price}\t{thumbnail}\t{DATE}\n")

    else:
        print("Error al obtener datos de MercadoLibre:", response.text)
        return []

def get_key_from_item(item_id, key):
    return str(item_id[key]).replace(' ','').strip() if item_id.get(key) else "null"

def main():
    CATEGORY = "MLA1577" # Microondas
    get_most_relevant_items_for_category(CATEGORY)

main()
