# coding:utf-8
import pika

def consumercallback(channel, method, properies, body):
    print("recive:%s" % body)

def main():

    credentials = pika.PlainCredentials("keyun",password="123456")
    parameters = pika.ConnectionParameters(host="127.0.0.1",
                                           virtual_host="/",
                                           credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="hello")
    channel.basic_consume(consumer_callback=consumercallback,
                          queue="hello",
                          no_ack=True)
    print("WaitMessahe:-----")
    channel.start_consuming()
if __name__ == '__main__':
    main()