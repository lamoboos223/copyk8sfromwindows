from kafka import KafkaConsumer, TopicPartition

try:
    consumer = KafkaConsumer(
        'foodmenu',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        group_id='group1',
        value_deserializer=lambda x: (x.decode('utf-8')))

    for message in consumer:
        print(message.topic, ':', message.value)

except Exception:
    print("exception")
