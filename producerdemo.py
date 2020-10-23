from pykafka import kafkaClient

client = kafkaClient(hosts="localhost:9092")

topic = client.topics['sales_topic']
producer = topic.get_sync_producer()
producer.produce('Welcom in pykafka'.encode('ascii'))