# coding:utf-8
import xml.etree.cElementTree as ET
import os
from collections import Counter
import shutil


# Counter({'towCounter({'tower': 3074, 'windpower': 2014, 'thermalpower': 689, 'hydropower': 261, 'transformer': 225})
# total_num: 6263

def count(pathdir, despath):
    category = []
    path = pathdir
    for index, xml in enumerate(os.listdir(path)):
        # print(str(index) + ' xml: '+ xml)
        root = ET.parse(os.path.join(path, xml))
        objects = root.findall('object')

        # ==================select images which has a special object=============
        for obj in objects:
            obj_label = obj.find('name').text
            if obj_label == 'transformer':
                print(xml)
                imgfile = pathdir + 'JPEG/' + xml.replace('xml', 'jpg')
                img_despath = despath + xml.replace('xml', 'jpg')
                # if not os.path.exists(img_despath):
                shutil.copyfile(imgfile, img_despath)

        # ==================select images which has a special object=============

        category += [ob.find('name').text for ob in objects]
    print(Counter(category))
    total_num = sum([value for key, value in Counter(category).items()])
    print('total_num:', total_num)


if __name__ == '__main__':
    # pathdirs = list(set(os.listdir('./')) ^ set(['tools','count.py']))
    # print(pathdirs)
    # for pathdir in pathdirs:
    pathdir = './VOC2007/Annotations/'
    despath = '/transformer/'
    count(pathdir, despath)