import os

filedir = r'C:\mython\projects\Devanagari-Character-Recognition\Sample Images\labels'
for filename in os.listdir(filedir):
    if filename.endswith(".txt"):
        with open('{}'.format(os.path.join(filedir, filename)), 'r+') as file:
            lines = file.readlines()
            file.seek(0, 0)
            for line in lines:
                row = line.strip().split(' ')
                # 要修改的第一个数字
                if row[0] == '15':
                    row[0] = '1'
                elif row[0] == '16':
                    row[0] = '2'
                row = ' '.join(i for i in row)
                print(row)
                file.write(''.join(str(row)) + "\n")
