import os
import shutil


def move_files(src_path, dst_path):
    files = os.listdir(src_path)
    for item in files:
        old_filepath = os.path.join(src_path, item)
        shutil.move(old_filepath, dst_path)


if __name__ == '__main__':
    src_path = r"C:\mython\projects\Devanagari-Character-Recognition\Sample Images\data"
    dst_path = r"C:\mython\projects\Devanagari-Character-Recognition\Sample Images"
    move_files(src_path + "/images", dst_path + "/images")
    move_files(src_path + "/labels", dst_path + "/labels")
