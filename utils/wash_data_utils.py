import csv
import os

from utils import csv_utils
from utils.file_utils import get_filename_list


# 清洗csv文件，转义转义字符
def wash_data(csvdir):
    csv_file_list = get_filename_list(csvdir)
    print("清洗数据开始")
    for i in csv_file_list:
        csv_path = csvdir + i
        print("当前清洗的数据：" + csv_path)
        headers = csv_utils.read_header(csv_path)
        headers.pop(0)
        lines = csv_utils.read_line(csv_path)
        # 删除当前csv文件
        os.remove(csv_path)
        with open(csv_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for l in lines:
                l.pop(0)
                writer.writerow(l)
        print("清洗完成")


def escape_data(data):
    res = []
    res += data
    for i in range(0, len(res)):
        item = res[i]
        if type(item) is str:
            res[i] = item.replace("\n", "\\n").replace("\r", "\\r")
    return res
