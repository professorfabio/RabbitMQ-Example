import rabbitpy
from const import *

with rabbitpy.Connection('amqp://myuser:abc123@' + RABBITMQ_ADDR + ':5672/%2f') as conn:
    with conn.channel() as channel:
        for message in rabbitpy.Queue(channel, 'my-queue'):
            print(message.body)
            message.ack()
