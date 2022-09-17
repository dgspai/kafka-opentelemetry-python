import os 

dir_path = os.path.dirname(os.path.realpath(__file__)).replace("/", "-")

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Asynchronous by default
future = producer.send(dir_path, b'raw_bytes')
