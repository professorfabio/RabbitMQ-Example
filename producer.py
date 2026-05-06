import rabbitpy
from const import *

with rabbitpy.Connection('amqp://myuser:abc123@'+ RABBITMQ_ADDR + ':5672/my_vhost') as conn:
    with conn.channel() as channel:
        exchange = rabbitpy.Exchange(channel, 'my-exchange')
        exchange.declare()

        queue = rabbitpy.Queue(channel, 'my-queue', durable=True, auto_delete=False)
        queue.declare()
        queue.bind(exchange, 'my-routing-key')

        message = rabbitpy.Message(channel, 'Hello, world!')
        message.publish(exchange, 'my-routing-key')
