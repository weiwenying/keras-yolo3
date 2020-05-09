# 如果目录存在，则删除目录
if [ ! -d "./VOCdevkit" ]; then
     echo "将要创建目录"
else
     rm -r ./VOCdevkit
     echo "VOCdevkit已经存在，将先该目录删除，再创建。"
fi

# 创建 目录
mkdir -p ./VOCdevkit/VOC2007/ && cd  ./VOCdevkit/VOC2007/
mkdir Annotations  ImageSets  JPEGImages  SegmentationClass  SegmentationObject
cd ./ImageSets && mkdir Layout  Main  Segmentation

