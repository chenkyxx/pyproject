# coding:utf-8
import os
import shutil
import time
import base64


class ReadW(object):
    """
    封装一个对照片文件处理与提取特征公共文件夹适应的读写类
    """
    def __init__(self, live_p_path, id_p_path, common_p_path):
        """
        实例化类
        :param live_p_path: 现场照片的存放路径
        :param id_p_path: 证件照片的存放路径
        :param common_p_path: 公共文件夹的存放路径
        :return:
        """
        self.live_picture_path = live_p_path
        self.id_picture_path = id_p_path
        self.common_picture_path = common_p_path

    def get_live_list_name(self):
        live_list_name = os.listdir(self.live_picture_path)
        return live_list_name

    def get_id_list_name(self):
        id_list_name = os.listdir(self.id_picture_path)
        return id_list_name

    def copy_all_picture_to_common(self, i):
        """
        将照片复制到公共文件夹中
        :param i: 现场照片和证件照返回的list索引
        :return:
        """
        shutil.copy((self.live_picture_path+"/"+self.get_live_list_name()[i]),
                    self.common_picture_path)
        shutil.copy((self.id_picture_path+"/" +
                     self.get_id_list_name()[i]),
                    (self.common_picture_path+"/" +
                     self.get_id_list_name()[i].replace(".", "%d." % i)))

    def get_live_feature_str(self, i):
        """
        获取现场照片的feature值
        :param i: 现场照片和证件照返回的list索引
        :return:
        """
        if os.path.exists((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt")):

            with open((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt"), "r") as fp:
                data = fp.read().rstrip()
            os.unlink((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt"))
        else:
            time.sleep(2)
            with open((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt"), "r") as fp:
                data = fp.read().rstrip()
            os.unlink((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt"))
        return data

    def get_id_feature_str(self, i):
        """
        获取证件照的feature值
        :param i: 现场照片和证件照返回的list索引
        :return:
        """
        if os.path.exists((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt")):
            with open((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt"),
                      "r") as fp:
                data = fp.read().rstrip()
            os.unlink((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt"))
        else:
            time.sleep(2)
            with open((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt"),
                      "r") as fp:
                data = fp.read().rstrip()
            os.unlink((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt"))
        return data

    def get_live_picture_base64(self, i):
        """获取现场照的base64编码"""
        with open(file=(self.live_picture_path+"/"+self.get_live_list_name()[i]), mode="rb") as fp:
            image_data = fp.read()
            base64_data = base64.b64encode(image_data)
            return str(base64_data, encoding="utf-8")

    def get_id_picture_base64(self,i):
        """获取证件照的base64编码"""
        with open(file=(self.id_picture_path+"/"+self.get_id_list_name()[i]), mode="rb") as fp:
            image_data = fp.read()
            base64_data = base64.b64encode(image_data)
            return str(base64_data, encoding="utf-8")

    def copy_id_picture(self, i, newpath, k=0):
        """
        把证件照照片复制i-k+1张到另一个文件夹里,i,k都是索引
        :param i:
        :return:
        """
        id_list = self.get_id_list_name()
        for a in range(k, i):
            shutil.copy((self.id_picture_path + "/" + id_list[a]), newpath)

    def copy_live_picture(self, i, newpath, k=0):
        """
        把现场照片复制i-k+1张到另一个文件夹里,i,k都是索引
        :param i:
        :return:
        """
        id_list = self.get_id_list_name()
        for a in range(k, i):
            shutil.copy((self.live_picture_path + "/" + id_list[a]), newpath)


if __name__ == '__main__':
    live_p_path = "E:/picture"
    id_p_path = "E:/IDcard"
    common_p_path = r"D:\work file\project\zhihuipanshi\特征批量提取工具\work_folder"
    opera = ReadW(live_p_path, id_p_path, common_p_path)
    opera.copy_id_picture(10000,"E:/idphoto")
    opera.copy_live_picture(10000,"E:/livephoto")







