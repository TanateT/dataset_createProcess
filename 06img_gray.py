import os
import shutil
import cv2
import numpy as np


def rename(path):
    images_path = os.path.join(path, "images")
    labels_path = os.path.join(path, "labels")
    images_name = os.listdir(images_path)
    labels_name = os.listdir(labels_path)
    for (image, label) in zip(images_name, labels_name):
        old_image_path = os.path.join(images_path, image)
        new_image = "gray_" + image
        new_image_path = os.path.join(images_path, new_image)
        # 重命名
        os.rename(old_image_path, new_image_path)

        old_label_path = os.path.join(labels_path, label)
        new_label = "gray_" + label
        new_label_path = os.path.join(labels_path, new_label)
        # 重命名
        os.rename(old_label_path, new_label_path)


def copy_file(src_dir, dst_dir, images_dir):
    class_labels = ["1"]
    for filename in os.listdir(src_dir):
        if filename.endswith(".txt"):
            path = os.path.join(src_dir, filename)
            with open(path, 'r+') as file:
                lines = file.readlines()
                file.seek(0, 0)
                flag = False
                for line in lines:
                    row = line.strip().split(' ')
                    # 多类别灰度化标签序列号
                    if row[0] in class_labels:
                        flag = True
                    if flag:
                        dst_dir_labels = os.path.join(dst_dir, "labels")
                        shutil.copy(path, dst_dir_labels)
                        print("标签{}复制".format(filename))
                        dst_dir_images = os.path.join(dst_dir, "images")
                        new_filename = filename.split(".")[0] + ".jpg"
                        src_path = os.path.join(images_dir, new_filename)
                        shutil.copy(src_path, dst_dir_images)
                        print("图片{}复制".format(new_filename))
                        break


def img_gray(path, mode):
    img_list = os.listdir(path)
    for img in img_list:
        img_path = os.path.join(path, img)
        img = cv2.imread(img_path)
        if mode == 0:
            # 修改参数
            img = cv2.cvtColor(img, 6)
            cv2.imwrite(img_path, img)
        elif mode == 1:
            # 图片尺寸修改
            img_zero = np.zeros_like(img)
            # 修改颜色
            (b, g, r) = (255, 0, 0)
            img_zero[:] = [b, g, r]
            cvt_img = cv2.addWeighted(img_zero, 0.5, img, 0.5, 0)
            cv2.imwrite(img_path, cvt_img)


if __name__ == '__main__':
    # 源地址标签路径
    src_dir = r'/Sample Images/data/labels'
    # 目标地址路径
    dst_dir = r'C:\mython\projects\Devanagari-Character-Recognition\Sample Images\data'
    # 源地址图片路径
    images_dir = r'/Sample Images/data/images'

    if not os.listdir(dst_dir):
        os.mkdir(dst_dir + "/images")
        os.mkdir(dst_dir + "/labels")
    else:
        print('文件夹已存在')

    if os.path.getsize(dst_dir + '/images') == 0:
        copy_file(src_dir, dst_dir, images_dir)
        img_gray(os.path.join(dst_dir, "images"), mode=0)
        rename(dst_dir)
    else:
        print('图片已存在')
