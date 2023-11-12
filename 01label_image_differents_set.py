import os

images_list = os.listdir(r'/Sample Images/data/images')
labels_list = os.listdir(r'C:\mython\projects\Devanagari-Character-Recognition\Sample Images\labels')
images_list = [i.split(".")[0] for i in images_list]
labels_list = [i.split(".")[0] for i in labels_list]
inter = set(images_list) & set(labels_list)
image_len = len(images_list)
labels_len = len(labels_list)
inter_len = len(inter)
if labels_len > inter_len:
    a = list(set(labels_list).difference(set(images_list)))
    a = [str(i) + ".txt" for i in a]
    print(f"\033[1;32;40m标签比图片多:{a}.jpg\033[0m")
if image_len > inter_len:
    a = list(set(images_list).difference(set(labels_list)))
    a = [str(i) + ".jpg" for i in a]
    print(f"\033[1;32;40m图片比标签多:{a}\033[0m")
if labels_len == inter_len and image_len == inter_len:
    print("\033[1;32;40m图片与标签匹配\033[0m")
else:
    print("\033[1;31;40m图片与标签不匹配\033[0m")
