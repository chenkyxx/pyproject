# coding:utf-8

# from xml.etree.ElementTree import ElementTree,Element
from xml.etree import ElementTree as ET
#
#
#
# def read_xml(in_path):
#     """
#     读取并解析xml文件
#     :param in_path:xml路径
#     :return:ElementTree
#     """
#     tree = ElementTree()
#     tree.parse(in_path)
#     return tree
#
#
# def write_xml(tree,out_path):
#     """
#     将xml文件写出
#     :param tree: xml树
#     :param out_path: 写出路径
#     :return:
#     """
#     tree.write(out_path,encoding="utf-8", xml_declaration=True)
#
# def find_nodes(tree,path):
#     """
#     查找某个路径匹配的所有节点
#     :param tree: xml树
#     :param path: 节点路径
#     :return:
#     """
#     return tree.findall(path)
#
# def change_node_text(nodelist,text,is_add=False,is_delete=False):
#     """
#     改变增加删除一个节点的文本
#     :param nodelist: 节点列表
#     :param text: 更新后的文本
#     :param is_add:
#     :param is_delete:
#     :return:
#     """
#     for node in nodelist:
#         if is_add:
#             node.text += text
#         elif is_delete:
#             node.text = ""
#         else:
#             node.text = text
#
# def get_node_by_keyvalue(nodelist, kv_map):
#     """
#     根据属性及属性值定位符合的节点，返回节点
#     nodelist: 节点列表
#     kv_map: 匹配属性及属性值map
#     """
#     result_nodes = []
#     for node in nodelist:
#         if if_match(node, kv_map):
#             result_nodes.append(node)
#             return result_nodes
#
# def if_match(node, kv_map):
#     '''判断某个节点是否包含所有传入参数属性
#        node: 节点
#        kv_map: 属性及属性值组成的map
#        '''
#     for key in kv_map:
#         if node.get(key) != kv_map.get(key):
#             return False
#         return True
# ET.register_namespace("", "http://schemas.datacontract.org/2004/07/Xasd.FASC.SECM.Entity")
ET.register_namespace(prefix="i", uri="http://www.w3.org/2001/XMLSchema-instance")
tree = ET.parse(r"C:\Users\Administrator\Desktop\lkxx.xml")
root = tree.getroot()

lk_id = root[3][0]
for i in lk_id:
    print(i.text)
print(root[3][0][15].text)
lk_id_ele = root[3][0][15]
lk_id_ele.text = "0001"

tree.write(file_or_filename="lkxx.xml",
           encoding="utf-8",
           #default_namespace="http://schemas.datacontract.org/2004/07/Xasd.FASC. SECM.Entity",
           xml_declaration=True)

with open("lkxx.xml","rb") as fp:
    data = fp.read().decode("utf-8")
    print(data)




















