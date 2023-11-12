import os

from matplotlib import pyplot as plt

# 类别统计
filedir = r'C:\mython\projects\Devanagari-Character-Recognition\Sample Images\data\labels'
count = [0] * 3
for filename in os.listdir(filedir):
    if filename.endswith(".txt"):
        with open('{}'.format(os.path.join(filedir, filename)), 'r+') as file:
            lines = file.readlines()
            file.seek(0, 0)
            for line in lines:
                row = line.strip().split(' ')
                # 两个类别
                if row[0]:
                    count[int(row[0])] += 1
                # if row[0] == '1':
                #     count[0] += 1
                # elif row[0] == '2':
                #     count[1] += 1
print(count)

# 准备数据
# 设置对应的类别
x_data = ['和尚', '狗', '猫']
# 设置对应类别的数量
y_data = count

# 正确显示中文和负号
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 画图，plt.bar()可以画柱状图
plt.pie(x=y_data, labels=x_data, autopct='%3.2f%%',
        shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.7)
plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0.1)
plt.title('类别统计饼状图')
plt.xlabel('类别')
plt.ylabel('占比')
plt.show()
