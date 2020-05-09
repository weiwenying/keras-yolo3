import os
import random


# 文件xml的目录，这些文件描述了图片中，被标记的物体的位置。
xml_file_path = "./VOCdevkit/VOC2007/Annotations/"
# 文件txt的父目录，这些txt文件，说明哪些图片用于训练集、哪些用于验证集，以及哪些用于测试集。
txt_base_path = "./VOCdevkit/VOC2007/ImageSets/Main/"


# 这三个值加起来，要等于1
train_percent = 0.8  # 训练集图片，相对于所有图片的占比
val_percent = 0.1  # 验证集图片，相对于所有图片的占比
test_percent = 0.1  # 测试集图片，相对于所有图片的占比


# 读取所有xml文件
total_xml = os.listdir(xml_file_path)
# 根据占比，计算训练集、验证集、测试集的图片的数量
total_num = len(total_xml)
train_num = int(total_num * train_percent)
val_num = int(total_num * val_percent)
test_num = int(total_num * test_percent)
# 划分前，随机打乱，然后再划分。
random.shuffle(total_xml)
train_xml = total_xml[0:train_num]
val_xml = total_xml[train_num:train_num+val_num]
test_xml = total_xml[train_num+val_num:train_num+val_num+test_num]


# 将xml文件名写入train.txt中，说明这么xml对应的图片，将作为train训练集。
with open(os.path.join(txt_base_path, "train.txt"), 'w') as f:
    for name in sorted(train_xml):  # 排序，只是让生成的txt更易于理解
        name = name[:-4] + "\n"
        f.write(name)

# 将xml文件名写入val.txt中，说明这么xml对应的图片，将作为val验证集。
with open(os.path.join(txt_base_path, "val.txt"), 'w') as f:
    for name in sorted(val_xml):
        name = name[:-4] + "\n"
        f.write(name)

# 将xml文件名写入test.txt中，说明这么xml对应的图片，将作为test测试集。
with open(os.path.join(txt_base_path, "test.txt"), 'w') as f:
    for name in sorted(test_xml):
        name = name[:-4] + "\n"
        f.write(name)
