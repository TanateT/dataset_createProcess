import os


def rename(path, name):
    images_path = os.path.join(path, "jishui")
    labels_path = os.path.join(path, "jishui_label")
    images_name = os.listdir(images_path)
    labels_name = os.listdir(labels_path)
    for image in images_name:
        old_image_path = os.path.join(images_path, image)
        new_image = name + image
        print(new_image)
        new_image_path = os.path.join(images_path, new_image)
        # 重命名
        os.rename(old_image_path, new_image_path)
    for label in labels_name:
        old_label_path = os.path.join(labels_path, label)
        new_label = name + label
        new_label_path = os.path.join(labels_path, new_label)
        # 重命名
        os.rename(old_label_path, new_label_path)


if __name__ == '__main__':
    dst_dir = r'C:\mython\projects\Devanagari-Character-Recognition'
    new_name = 'img_'
    rename(dst_dir, new_name)
