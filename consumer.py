import rabbitpy
from const import *

with rabbitpy.Connection('amqp://myuser:abc123@' + RABBITMQ_ADDR + ':5672/my_vhost') as conn:
    with conn.channel() as channel:
        queue = rabbitpy.Queue(channel, 'my-queue', exclusive=True)
        for message in queue:
            print(message.body)
            message.ack()
