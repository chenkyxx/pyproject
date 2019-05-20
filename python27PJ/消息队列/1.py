# coding:utf-8
from xml.etree import ElementTree as ET

ET.register_namespace("", "http://schemas.datacontract.org/2004/07/Xasd.FASC.SECM.Entity")
ET.register_namespace("i", "http://www.w3.org/2001/XMLSchema-instance")
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
           xml_declaration=True)

with open("lkxx.xml","rb") as fp:
    data = fp.read().decode("utf-8")
    print(data)
