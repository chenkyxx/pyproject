# coding:utf-8
import os, sys, time
import pika

# 接收处理消息的回调函数
def ConsumerCallback (channel, method, properties, body):
	print("Received %s" % body)


def Main():
	credentials = pika.PlainCredentials("keyun", "123456")
	parameters = pika.ConnectionParameters(host="127.0.0.1",
											virtual_host='/',
											credentials=credentials)
	connection = pika.BlockingConnection(parameters)    # 连接 RabbitMQ

	channel = connection.channel()          # 创建频道

	queue = channel.queue_declare(queue='queuetest')     # 声明或创建队列

	# no_ack=True 开启自动确认，不然消费后的消息会一直留在队列里面
	# no_ack = no_manual_ack = auto_ack；不手动应答，开启自动应答模式
	channel.basic_consume(ConsumerCallback, queue='queuetest', no_ack=True)
	print('Wait Message ...')

	channel.start_consuming()

if __name__ == '__main__':
	Main()
