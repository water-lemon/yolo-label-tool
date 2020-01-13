# -*- coding: utf-8 -*-
import os
import xml.dom.minidom
import shutil
g = os.walk("label")
for path, dir_list, file_list in g:
    for file_name in file_list:
        # print(file_name)
        a = file_name
        result = file_name.split('\n')
        # print(result)
        for i in result:
            dom = xml.dom.minidom.parse("/home/thu/Downloads/7-/label/"+i)
            print(dom.toprettyxml())
            if "bndbox" in dom.toprettyxml():
                print (i)
                shutil.move("/home/thu/Downloads/7-/label/"+i, "/home/thu/Downloads/7-/VOC2007/Annotations")
