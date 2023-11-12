import os
import random
import shutil


def mk_files(path_file: str):
    if os.path.exists(path_file):
        shutil.rmtree(path_file)
    os.mkdir(path_file)


def without_class_dir(images_path):
    train_root = os.path.join(images_path, "train")
    mk_files(train_root)
    #  验证集
    val_root = os.path.join(images_path, 'val')
    mk_files(val_root)
    #  测试集
    # test_root = os.path.join(data_root, 'test')
    # mk_files(test_root)
    return train_root, val_root


def with_class_dir(data_root, n_classes):
    train_root = os.path.join(data_root, "train")
    mk_files(train_root)
    for cls in n_classes:
        mk_files(os.path.join(train_root, cls))
    #  验证集
    val_root = os.path.join(data_root, 'val')
    mk_files(val_root)
    for cls in n_classes:
        mk_files(os.path.join(val_root, cls))
    #  测试集
    # test_root = os.path.join(data_root, 'test')
    # mk_files(test_root)
    # for cls in n_classes:
    #     mk_files(os.path.join(test_root, cls))
    return train_root, val_root


def splitFiles(data_root, images_path, split_rate):
    # 保证随机可重复
    random.seed(42)
    assert os.path.exists(images_path)
    n_classes = [cls for cls in os.listdir(images_path)]
    # 有标签文件的数据集分类
    if os.path.isdir(os.path.join(images_path, n_classes[-1])):
        # 创建训练与验证的类别文件夹
        train_root, val_root = with_class_dir(data_root, n_classes)
        for cls in n_classes:
            cls_path = os.path.join(images_path, cls)
            images = os.listdir(cls_path)
            num = len(images)
            eval_index = random.sample(images, k=int(num * split_rate))
            for index, image in enumerate(images):
                if image in eval_index:
                    image_path = os.path.join(cls_path, image)
                    val_path = os.path.join(val_root, cls)
                    shutil.move(image_path, val_path)
                else:
                    image_path = os.path.join(cls_path, image)
                    train_path = os.path.join(train_root, cls)
                    shutil.move(image_path, train_path)
                print("\r[{}] processing [{}/{}]".format(cls, index + 1, num), end="")
        print()
    # 无标签文件的数据集分类
    else:
        train_root, val_root = without_class_dir(images_path)
        dir_train_val = ['train', 'val']
        images = [jpg for jpg in os.listdir(images_path) if jpg not in dir_train_val]
        print(images)
        num = len(images)
        eval_index = random.sample(images, k=int(num * split_rate))

        for index, image in enumerate(images):
            if image in eval_index:
                image_path = os.path.join(images_path, image)
                val_path = val_root
                shutil.move(image_path, val_path)
            else:
                image_path = os.path.join(images_path, image)
                train_path = train_root
                shutil.move(image_path, train_path)
            print("\033[1;32;40m\r[{}] processing [{}/{}]\033[0m".format(images, index + 1, num), end="")
        print()
    print('\033[1;32;40m processing done\033[0m')


if __name__ == '__main__':
    # 获取当前的目录
    cwd = os.getcwd()
    # 将数据集的50%划分到验证集
    split_rate = 0.3
    # 获取图片和文本的总目录
    data_root = os.path.join(cwd, 'sample Images')
    images_path = os.path.join(data_root, 'images')
    splitFiles(data_root, images_path, split_rate)
    labels_path = os.path.join(data_root, 'labels')
    splitFiles(data_root, labels_path, split_rate)
