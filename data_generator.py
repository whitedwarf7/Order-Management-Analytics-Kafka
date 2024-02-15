import time
import random
import requests

API_URL = "http://127.0.0.1:8000/orders"

MAX_ORDER_ID = 1000

ITEMS = ["T-shirts", "Hoodies", "Hats", "Accessories"]

while True:
    order_id = random.randint(1, MAX_ORDER_ID)

    user_id = random.randint(1000, 2000)  
    total_cost = random.randint(100, 500)  

    items = random.sample(ITEMS, k=random.randint(2, 3))
    items_string = ", ".join(items)

    payload = {
        "order_id": order_id,
        "user_id": user_id,
        "total_cost": total_cost,
        "items": items_string
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  
        print(f"API call successful: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")

    time.sleep(3) 
