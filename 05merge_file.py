import os
import shutil


# 将测试的数据集与训练的数据集合并

def mergeFiles(path):
    files_document = os.listdir(path)
    print(files_document)
    for i in range(len(files_document)):
        if not os.path.isdir(files_document[i]):
            train = os.path.join(path, files_document[i])
            document_train = os.listdir(train)
            print(document_train)
            if document_train is not None:
                for train_i in document_train:
                    print(train + '/' + train_i, path)
                    shutil.move(train + '/' + train_i, path)
                os.rmdir(train)
    print()
    print('\033[1;32;40m processing done\033[0m')


if __name__ == '__main__':
    path_images = r'/Sample Images/data/images'
    mergeFiles(path_images)
    path_labels = r'C:\mython\projects\Devanagari-Character-Recognition\Sample Images\labels'
    mergeFiles(path_labels)
