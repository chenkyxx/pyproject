# coding:utf-8
import pika
import uuid
import time

credentials = pika.PlainCredentials("keyun",password="123456")
parameters = pika.ConnectionParameters(host="127.0.0.1",
                                       virtual_host="/",
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue="hello")
while True:
    msg = str(uuid.uuid4())
    channel.basic_publish(exchange="",
                          routing_key="hello",
                          body=msg)
    print("发送消息：%s" % msg)
    while True:
        queue = channel.queue_declare(queue="hello", passive=True)
        messagecount = queue.method.message_count
        print("messagecount:%d" % messagecount)
        if messagecount > 100:
            break
        connection.sleep(1)
connection.close()



