import os


# 第一种命名方法
def rename(path, name):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    images_path = os.path.join(path, "images")
    labels_path = os.path.join(path, "labels")
    images_name = os.listdir(images_path)
    labels_name = os.listdir(labels_path)
    for image in images_name:
        image_number = ''
        for string in image:
            if string in number:
                image_number += string
        print(image_number)
        old_image_path = os.path.join(images_path, image)
        new_image = name + str(int(image_number)) + '.'+image.split('.')[-1]
        new_image_path = os.path.join(images_path, new_image)
        # 重命名
        os.rename(old_image_path, new_image_path)
    for label in labels_name:
        label_number = ''
        for string in label:
            if string in number:
                label_number += string
        old_label_path = os.path.join(labels_path, label)
        new_label = name + str(int(label_number)) + '.'+label.split('.')[-1]
        new_label_path = os.path.join(labels_path, new_label)
        # 重命名
        os.rename(old_label_path, new_label_path)


# 第二种命名方式
def rename1(path, name):
    images_path = os.path.join(path, "images")
    labels_path = os.path.join(path, "labels")
    images_name = os.listdir(images_path)
    labels_name = os.listdir(labels_path)
    for image in images_name:
        old_image_path = os.path.join(images_path, image)
        new_image = name + image[-7:]
        new_image_path = os.path.join(images_path, new_image)
        # 重命名
        os.rename(old_image_path, new_image_path)
    for label in labels_name:
        old_label_path = os.path.join(labels_path, label)
        new_label = name + label[-7:]
        new_label_path = os.path.join(labels_path, new_label)
        # 重命名
        os.rename(old_label_path, new_label_path)


if __name__ == '__main__':
    dst_dir = r'C:\mython\projects\Devanagari-Character-Recognition\Sample Images\data'
    new_name = 'tb_'
    rename(dst_dir, new_name)
