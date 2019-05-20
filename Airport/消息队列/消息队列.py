# coding:utf-8
import pika
import xml.etree.ElementTree as ET
import time

def send_msg(msg):
    """
    将消息体发送到队列中
    :param msg: 要发送的消息
    :return:
    """
    credentials = pika.PlainCredentials(username="root", password="123456")
    parameters = pika.ConnectionParameters(host="192.168.0.234",
                                           port=5672,
                                           virtual_host="/",
                                           credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters,)
    channel = connection.channel()
    channel.queue_declare(queue="bt_sec_queue",
                          durable=True)
    channel.basic_publish(exchange="",
                          routing_key="bt_sec_queue",
                          body=msg,)
    print(" [x] Sent %r:%r" % ("bt_sec_queue", msg))
    connection.close()

def msg_str(filepath,Type):
    """
    定义要发送的消息体
    :param filepath: 打开的文件路径
    :param Type: 打开的文件流形式 “rb”，“r”，“w”
    :return:
    """
    with open(file=filepath,mode=Type) as fp:
        data = fp.read()
        return data


if __name__ == '__main__':
    with open(r"D:\work file\project\智慧机场全流程\报文样例\11.xml", "rb") as fp:
        data = fp.read().decode(encoding="utf-8")  # errors="ignore"
        # print(data)
        print(type(fp))
        print(data)
        # while True:
        #     time.sleep(1)
        #     send_msg(data)








