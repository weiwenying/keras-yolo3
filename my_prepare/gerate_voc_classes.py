import os
import pathlib


voc_classes_txt_path = "./model_data/voc_classes.txt"
label_xmls_path = "./my_dataset/label_xmls/"  # 你的数据集xml文件所在目录的父目录

label_xmls_path = pathlib.Path(label_xmls_path)
# 图片分类的名称，各个分类的图片，在各自的文件夹内
label_names = sorted(
    item.name for item in label_xmls_path.glob('*/') if item.is_dir())


with open(voc_classes_txt_path, 'w') as f:
    for name in sorted(label_names):
        name = name + "\n"
        f.write(name)
