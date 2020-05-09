import os
import pathlib
import shutil


src_dataset_path = "./my_dataset/src_images/"  # 源文件目录
dst_dataset_path = "./my_dataset/dst_images/"  # 修改文件名后，存放的目录

src_dataset_path = pathlib.Path(src_dataset_path)
dst_dataset_path = pathlib.Path(dst_dataset_path)
# 图片分类的名称，各个分类的图片，在各自的文件夹内
label_names = sorted(
    item.name for item in src_dataset_path.glob('*/') if item.is_dir())


# 生成存放目录
if os.path.exists(dst_dataset_path):
   shutil.rmtree(dst_dataset_path)
os.makedirs(dst_dataset_path)
for path in label_names:
   os.makedirs(dst_dataset_path / path)


for label_name in label_names:
   # 某个类别的目录
   src_image_paths = src_dataset_path / label_name
   # 某个类别的所有图片
   src_image_paths = src_image_paths.glob("*/")
   # 转换为字符串类型
   src_image_paths = sorted([str(path) for path in src_image_paths])

   for i, src_image_path in enumerate(src_image_paths):
       # 新名称
       path_splits = src_image_path.split("/")
       class_name = path_splits[-2]
       new_name = "{}_{:0>5d}.jpg".format(class_name, i)
       shutil.copy(src_image_path, dst_dataset_path / label_name / new_name)
       print(src_image_path)
       print(dst_dataset_path / label_name / new_name)
