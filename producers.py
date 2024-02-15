import json
from fastapi import FastAPI
from kafka import KafkaProducer

BOOTSTRAP_SERVERS = "localhost:29092"
ORDER_DETAIL_TOPIC = "order_detail"
ORDER_CONFIRMED_TOPIC = "order_confirmed"

app = FastAPI()

order_detail_producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

@app.post("/orders")
async def create_order(data: dict):
    order_detail_producer.send(ORDER_DETAIL_TOPIC, value=json.dumps(data).encode())
    return {"message": "Order created"}
