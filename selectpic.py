# -*- coding: utf-8 -*-
import os
import shutil
pic_path = "./VOC2007/JPEGImage"
g = os.walk("./VOC2007/Annotations")
for path, dir_list, file_list in g:
    for file_name in file_list:
        file_name_num = file_name.split('.')[-2]
        print(file_name_num)
        pic_name = "/home/thu/Downloads/7-/RawImage/"+file_name_num+".jpg"
        shutil.copy(pic_name, pic_path)