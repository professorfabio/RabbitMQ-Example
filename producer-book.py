import rabbitpy
from const import *

def producer():
  connection = rabbitpy.Connection('amqp://myuser:abc123@' + RABBITMQ_ADDR + ':5672/my_vhost') # Connect to RabbitMQ server
  channel = connection.channel()     # Create new channel on the connection

  exchange = rabbitpy.Exchange(channel, 'exchange') # Create an exchange
  exchange.declare()

  queue1 = rabbitpy.Queue(channel, 'example1', durable=True, auto_delete=False) # Create 1st queue
  queue1.declare()

  queue2 = rabbitpy.Queue(channel, 'example2', durable=True, auto_delete=False) # Create 2nd queue
  queue2.declare()

  queue1.bind(exchange, 'example-key1') # Bind queue1 to a single key
  queue2.bind(exchange, 'example-key2') # Bind queue2 to the same key

  message = rabbitpy.Message(channel, 'Test message')
  message.publish(exchange, 'example-key1') # Publish the message using the key
  exchange.delete() 

if __name__ == "__main__":
  producer()
