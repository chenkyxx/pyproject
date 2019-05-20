# coding:utf-8

queue_manager = "Data"
channel = "SVER"
host = "100.100.100.84"
port = "2413"

queue_name = "S_TMP"
message = "hello world"
conn_info = "%s(%s)" % (host, port)
qmgr = pymqi.Queue(queue_manager, channel, conn_info)

queue = pymqi.Queue(qmgr, queue_name)
queue.put(message)
queue.close()

qmgr.close()