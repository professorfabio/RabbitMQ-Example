import rabbitpy
from const import *

def consumer():
  connection = rabbitpy.Connection('amqp://myuser:abc123@' + RABBITMQ_ADDR + ':5672/my_vhost')
  channel = connection.channel()

  queue = rabbitpy.Queue(channel, 'example1')

  # While there are messages in the queue, fetch them using Basic.Get
  while len(queue) > 0:
    message = queue.get()
    print('Message Q1: %s' % message.body.decode())
    message.ack()

  queue = rabbitpy.Queue(channel, 'example2')    

  while len(queue) > 0:
    message = queue.get()
    print('Message Q2: %s' % message.body.decode())
    message.ack()

if __name__ == "__main__":
  consumer()
