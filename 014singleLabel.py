import os, shutil
# 原始标签文件夹
dir = r"C:\mython\projects\Devanagari-Character-Recognition\Sample Images\data\labels"
# 原始图片文件夹
dir_image = r"C:\mython\projects\Devanagari-Character-Recognition\Sample Images\data\images"
# 目标文件夹
dir_new = r"C:\mython\projects\Devanagari-Character-Recognition\data"
label_list = os.listdir(dir)
classes_index = ['1', '2']
if not os.listdir(dir_new):
    os.mkdir(dir_new + '/labels')
    os.mkdir(dir_new + '/images')
else:
    print("已创建，请删除文件夹data目录下文件夹images和labels")
label_txt = os.path.join(dir_new, 'labels')
if not os.listdir(label_txt):
    for i in label_list:
        image_name = i.split('.')[0] + '.jpg'
        with open('{}'.format(os.path.join(dir, i)), 'r') as file:
            lines = file.readlines()
            file.seek(0, 0)
            for line in lines:
                line_ = line[:5].split(' ')[0]
                if line_ in classes_index:
                    with open(label_txt + '/' + i, 'a+') as f:
                        f.write(line)
                    shutil.copy(dir_image + '/' + image_name, dir_new + '/' + 'images')
    print('加载完毕')
else:
    print('已存在数据请删除！！')
