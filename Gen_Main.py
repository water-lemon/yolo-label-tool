import os
import random

trainval_percent = 0.8
train_percent = 0.8
xmlfilepath = './VOC2007/Annotations'
txtsavepath = './VOC2007/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)
# print(total_xml)
num = len(total_xml)
# print(num)
list = range(num)
# print(list)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
# print(len(trainval))
train = random.sample(trainval, tr)
# print(len(train))

ftrainval = open('VOC2007/ImageSets/Main/trainval.txt', 'w')
ftest = open('VOC2007/ImageSets/Main/test.txt', 'w')
ftrain = open('VOC2007/ImageSets/Main/train.txt', 'w')
fval = open('VOC2007/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
