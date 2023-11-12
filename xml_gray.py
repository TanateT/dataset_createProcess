import os
import shutil
import xml.etree.ElementTree as ET
import cv2
import imutils
import numpy as np


def img_AUG(path, img_dir, label_dir):
    images_path = os.path.join(path, "jishui")
    labels_path = os.path.join(path, "jishui_label")
    images_name = os.listdir(images_path)
    labels_name = os.listdir(labels_path)
    for i in range(len(images_name)):
        old_image_path = os.path.join(images_path, images_name[i])
        old_label_path = os.path.join(labels_path, labels_name[i])
        if i % 4 == 3:
            img = cv2.imread(old_image_path, 0)
            dir_image = img_dir + '/' + images_name[i]
            cv2.imwrite(dir_image, img)
            dir_label = label_dir
            shutil.copy(old_label_path, dir_label)
        elif i % 4 == 0:
            # 打开xml文档
            img = cv2.imread(old_image_path)
            # 翻转
            img = np.flipud(img)
            dir_image = img_dir + '/' + images_name[i]
            cv2.imwrite(dir_image, img)
            tree = ET.parse(old_label_path)
            root = tree.getroot()
            height = root.iter('height')
            y_min = root.iter('ymin')
            y_max = root.iter('ymax')
            for h, y1, y2 in zip(height, y_min, y_max):
                tmp_y1 = str(abs(int(h.text) - int(y2.text)))
                tmp_y2 = str(abs(int(h.text) - int(y1.text)))
                y1.text, y2.text = tmp_y1, tmp_y2
            dir_label = label_dir + '/' + labels_name[i]
            tree.write(dir_label)
        elif i % 4 == 1:
            img = cv2.imread(old_image_path)
            # 平移
            img = imutils.translate(img, 50, 50)
            dir_image = img_dir + '/' + images_name[i]
            cv2.imwrite(dir_image, img)
            tree = ET.parse(old_label_path)
            root = tree.getroot()
            width, height = root.iter('width'), root.iter('height')
            x_min, y_min, = root.iter('xmin'), root.iter('ymin')
            x_max, y_max = root.iter('xmax'), root.iter('ymax')
            for w, h, x1, y1, x2, y2 in zip(width, height, x_min, y_min, x_max, y_max):
                x1.text, y1.text = str(int(x1.text) + 10), str(int(y1.text) + 10)
                if int(x2.text) + 10 > int(w.text):
                    x2.text = w.text
                else:
                    x2.text = str(int(x2.text) + 10)
                if int(y2.text) + 10 > int(h.text):
                    y2.text = h.text
                else:
                    y2.text = str(int(y2.text) + 10)
            dir_label = label_dir + '/' + labels_name[i]
            tree.write(dir_label)
        elif i % 4 == 2:
            img = cv2.imread(old_image_path)
            # 缩放
            imginfo = img.shape
            h = imginfo[0]
            w = imginfo[1]
            M = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
            img = cv2.warpAffine(img, M, (w, h))
            dir_image = img_dir + '/' + images_name[i]
            cv2.imwrite(dir_image, img)
            tree = ET.parse(old_label_path)
            root = tree.getroot()
            x_min, y_min, = root.iter('xmin'), root.iter('ymin')
            x_max, y_max = root.iter('xmax'), root.iter('ymax')
            for x1, y1, x2, y2 in zip(x_min, y_min, x_max, y_max):
                print(x1.text)
                x1.text, y1.text = str(int(x1.text) // 2), str(int(y1.text) // 2)
                x2.text, y2.text = str(int(x2.text) // 2), str(int(y2.text) // 2)
                print(x1.text)
            dir_label = label_dir + '/' + labels_name[i]
            tree.write(dir_label)


if __name__ == '__main__':
    # 原始路径
    dst_dir = r'C:\mython\projects\Devanagari-Character-Recognition'
    # 图片目标路径
    img_dir = 'data/积水'
    # 标签目标路径
    label_dir = 'data/积水标注'
    img_AUG(dst_dir, img_dir, label_dir)
