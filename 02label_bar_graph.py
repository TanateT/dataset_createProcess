import os

from matplotlib import pyplot as plt

# 正确显示中文和负号
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 准备数据
# 设置对应的类别
x_data = ['和尚', '狗', '猫']
count = [0] * len(x_data)
# 设置对应类别的数量
y_data = count
print(y_data)
# 类别统计
filedir = r'C:\mython\projects\Devanagari-Character-Recognition\Sample Images\data\labels'

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

# 画图，plt.bar()可以画柱状图
for i in range(len(x_data)):
    plt.bar(x_data[i], y_data[i])
# plt.bar(x_data, y_data)
# 设置图片名称
plt.title("训练图像数据类别数量对比")
plt.xticks(rotation=45)
# 设置x轴标签名
plt.xlabel("类别")
# 设置y轴标签名
plt.ylabel("数量")
# 显示
for x, y in zip(range(len(count)), count):
    plt.text(x, y, s=y, size=12, family="Times new roman", color="black", style='italic', weight="light",
             bbox=dict(facecolor="dimgray", alpha=0.7, boxstyle="round"))
plt.show()
