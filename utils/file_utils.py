import os


def get_filename_list(dir):
    return os.listdir(dir)


def remove_files_by_dir(dir):
    file_name_list = get_filename_list(dir)
    for i in file_name_list:
        print("文件已存在，删除文件：" + i)
        os.remove(dir + i)


def check_and_create_dir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


def check_dirs(dir_list):
    for d in dir_list:
        check_and_create_dir(d)


def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


if __name__ == '__main__':
    print(get_desktop_path())