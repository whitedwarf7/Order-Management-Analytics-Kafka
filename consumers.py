import json
from kafka import KafkaConsumer, KafkaProducer
import threading

# Consumer configurations
CONSUMER_GROUP_ID = "order_processor"
BOOTSTRAP_SERVERS='localhost:29092'
ORDER_DETAIL_TOPIC = "order_detail"
ORDER_CONFIRMED_TOPIC = "order_confirmed"


def consume_order_details():
    
    consumer = KafkaConsumer(
    ORDER_DETAIL_TOPIC, 
    bootstrap_servers="localhost:29092"
    )
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
    
    print("Gonna start listening for transactions...")
    while True:
        for message in consumer:
            print("-----------------------Transactions--------------------------")
            print("Ongoing transaction..")
            consumed_message = json.loads(message.value.decode())
            print("consumed_message", consumed_message)
            
            user_id = consumed_message["user_id"]
            total_cost = consumed_message["total_cost"]
            data = {
                "customer_id": user_id,
                "customer_email": f"{user_id}@gmail.com",
                "total_cost": total_cost
            }
            
            print("Successful transaction..")
            producer.send(ORDER_CONFIRMED_TOPIC, json.dumps(data).encode("utf-8"))


def consume_order_confirmed_for_emails():

    consumer = KafkaConsumer(
    ORDER_CONFIRMED_TOPIC, 
    bootstrap_servers="localhost:29092"
    )

    emails_sent_so_far = set()

    print("Gonna start listening for emails...")
    while True:
        for message in consumer:
            print("-----------------------Emails--------------------------")
            consumed_message = json.loads(message.value.decode())
            
            customer_email = consumed_message["customer_email"]
            print(f"Sending email to {customer_email} ")
            
            emails_sent_so_far.add(customer_email)
            print(f"So far emails sent to {len(emails_sent_so_far)} unique emails")


def consume_order_confirmed_for_analytics():

    consumer = KafkaConsumer(
    ORDER_CONFIRMED_TOPIC, 
    bootstrap_servers="localhost:29092"
    )

    total_orders_count = 0
    total_revenue = 0

    print("Gonna start listening for analytics...")
    while True:
        for message in consumer:
            print("-----------------------Analytics--------------------------")
            print("Updating analytics..")
            consumed_message = json.loads(message.value.decode())
            total_cost = float(consumed_message["total_cost"])
            total_orders_count += 1
            total_revenue += total_cost
            
            print(f"Orders so far today: {total_orders_count}")
        print(f"Revenue so far today: {total_revenue}")


thread1 = threading.Thread(target=consume_order_details)
thread1.start()

thread2 = threading.Thread(target=consume_order_confirmed_for_emails)
thread2.start()

thread3 = threading.Thread(target=consume_order_confirmed_for_analytics)
thread3.start()
