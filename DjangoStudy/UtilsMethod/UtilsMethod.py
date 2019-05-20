# coding:utf-8
import psutil
m = psutil.virtual_memory()


class UtilsMethod(object):
    def __init__(self):
        pass

    @classmethod
    def get_total_cpu_percent(cls):
        return str(psutil.cpu_percent(interval=1))

    @classmethod
    def get_process_info(cls, pid):
        aa = {}
        mm = psutil.Process(pid)
        aa["process memory"] = round((mm.memory_percent()*cls.get_total_memory())/1024/1024/1024, 2)
        aa["process cpu"] = mm.cpu_percent(interval=1)
        return aa

    @classmethod
    def get_userd_memory(cls):
        used = m.used
        return used

    @classmethod
    def get_total_memory(cls):
        total = m.total
        return total

    @classmethod
    def get_used_memory_percent(cls):
        return round(float(cls.get_userd_memory())/float(cls.get_total_memory())*100, 2)

    @classmethod
    def get_all(cls):
        m = {}
        m["cpu使用率"] = cls.get_total_cpu_percent()
        m["内存使用率"] = cls.get_used_memory_percent()
        return m


if __name__ == '__main__':
    while True:
        print(UtilsMethod().get_process_info(38288))