import os
import shutil


# 文件移动
def file_move(src_path, dst_path):
    for root, dirname, filename in os.walk(src_path):
        print("当前地址:", root)
        for name in dirname:
            print("当前目录名:", name)
        for name in filename:
            print("当前文件名:", name)
            file_path = os.path.join(root, name)
            shutil.move(file_path, dst_path)


def special_file_move(src_path, dst_path):
    for root, dirname, filename in os.walk(src_path):
        for name in filename:
            if name.endswith(".jpg"):
                file_path = os.path.join(root, name)
                shutil.move(file_path, dst_path)


if __name__ == "__main__":
    src_path = r"C:\mython\projects\Devanagari-Character-Recognition\Sample Images\labels"
    dst_path = r"/Sample Images/data/images"
    special_file_move(src_path, dst_path)
    # file_move(src_path, dst_path)
