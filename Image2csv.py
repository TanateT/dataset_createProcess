import csv
import cv2
import os


def img2csv(img_dir, csv_file):
    with open(csv_file, 'w', newline="") as file:
        # 设置csv列名
        col_name = ['pixel_%04d' % i for i in range(32 * 32)]
        col_name.extend(['character'])
        # 将列名写入csv
        csv_writer = csv.writer(file)
        csv_writer.writerow(col_name)
        # 该目录下的目录名,46个类别
        file_name = os.listdir(img_dir)
        for i in file_name:
            img_tmp_dir = os.path.join(img_dir, i)
            print(f'\033[1;32;40m当前处理的{i}\033[0m')
            # 判断是否为目录
            if os.path.isdir(img_tmp_dir):
                # 获取目录的路径
                img_list = os.listdir(img_tmp_dir)
                for img_name in img_list:
                    img_path = os.path.join(img_tmp_dir, img_name)
                    print(f'\033[1;32;40m当前处理的文件目录{i} 图片的名称{img_name}\033[0m')
                    # 判断是否为文件
                    if os.path.isfile(img_path):
                        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                        # 获取图片像素
                        row_data = [i for i in img.flatten()]
                        # 获取文件的名字即标签
                        row_data.extend([i])
                        # 将数据存储到csv文件中
                        csv_writer.writerow(row_data)
    print('\033[1;31;40m运行完成\033[0m')


if __name__ == '__main__':
    csv_file = r"C:\mython\projects\Devanagari-Character-Recognition\DevanagariHandwrittenCharacterDataset\Train\data.csv"
    path = r'C:\mython\projects\Devanagari-Character-Recognition\DevanagariHandwrittenCharacterDataset\Train'
    img2csv(path, csv_file)
