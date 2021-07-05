from flask import Flask
from kafka import KafkaProducer, KafkaConsumer

TOPIC = 'foodmenu'
VALUE = 'Pasta'
try:
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
    value_serializer=lambda x: (x.encode('utf-8')))

    producer.send(TOPIC, value=VALUE)
    print("Value: %s sent to topic: %s" %(VALUE, TOPIC))

    producer.flush()
    producer.close()

except Exception:
    print("exception")

