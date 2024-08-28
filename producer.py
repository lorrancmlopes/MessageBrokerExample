import pika
import os
from dotenv import load_dotenv

load_dotenv()

# Configure credentials
credentials = pika.PlainCredentials(
    os.getenv("RABBIT_USERNAME"), os.getenv("RABBIT_PASSWORD")
)

# Create a connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", credentials=credentials, heartbeat=0)
)

channel = connection.channel()

# Create a queue named "chitchat"
channel.queue_declare(queue="chitchat", durable=True)

while True:
    msg = input("Type a message: ")

    if msg == "exit":
        # Close connection
        connection.close()
        break

    # Send a message to queue
    channel.basic_publish(
        exchange="",
        routing_key="chitchat",
        body=msg,
    )