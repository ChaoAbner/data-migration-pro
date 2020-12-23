import csv

from utils import csv_utils, json_utils
from config.csv_config import *
from config.poem_config import *
from config.word_config import *
from data_transform import remove_files_by_dir
from utils.file_utils import check_dirs, get_desktop_path

resource_path = get_desktop_path() + '/resource.csv'

json_file_root_path = get_desktop_path() + '/resourceJsonList/'

new_csv_root_path = get_desktop_path() + '/oldCsvFile/'


def output_csv(lines):
    for l in lines:
        json_path = json_file_root_path + l[PATH_INDEX]
        # 读取json
        json_dict = json_utils.read_json(json_path)
        # 生成csv头
        header = generate_header(l)
        resource_name = get_resource_name(l)
        # 写入路径
        output_path = new_csv_root_path + get_resource_name(l) + ".csv"
        l.append(resource_name)
        with open(output_path, 'w') as f:
            print("正在写入csv文件：" + output_path + "...")
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            write_rows(l, json_dict, csv_writer)
            print("写入完成！")


def write_rows(l, json_dict, csv_writer):
    if is_word_type(l):
        for r in json_dict:
            csv_writer.writerow(get_word_data_list(l, r))
    elif is_poem_type(l):
        for r in json_dict:
            csv_writer.writerow(get_poem_data_list(l, r))


def get_word_data_list(line, row):
    res = []
    res += line
    for i in WORD_HEADER:
        res.append(get_or_default_blank(row, i))
    return res


def get_poem_data_list(line, row):
    res = []
    res += line
    for i in POEM_HEADER:
        res.append(get_or_default_blank(row, i))
    return res


def get_or_default_blank(row, keyword):
    data = row.get(keyword)
    if data is True or data is False:
        return str(data)
    if data is None:
        return ""
    if type(data) is str:
        return wash_data(data)
    return data


def wash_data(data):
    return data.replace(",", "，")


def get_resource_name(resource_line):
    return resource_line[VERSION_INDEX] + "-" + \
           resource_line[STAGE_INDEX] + resource_line[GRADE_INDEX]


def generate_header(resource_line):
    header = []
    if is_word_type(resource_line):
        header = RESOURCE_HEADER + WORD_HEADER
    elif is_poem_type(resource_line):
        header = RESOURCE_HEADER + POEM_HEADER
    return header


def is_word_type(resource_line):
    return resource_line[TYPE_INDEX] == WORD_TYPE


def is_poem_type(resource_line):
    return resource_line[TYPE_INDEX] == POEM_TYPE


def run():
    check_dirs([new_csv_root_path])
    lines = csv_utils.read_line(resource_path)
    remove_files_by_dir(new_csv_root_path)
    output_csv(lines)


if __name__ == '__main__':
    # 1、读取resource csv文件，获取资源包列表lines
    # 2、遍历资源包列表lines，
    # 2.1 拼接文件名 "versionName-stageName+versionName"
    # 2.2 拼接json文件的path，读取json文件
    # 2.3 拼接资源包信息和json数据信息
    # 2.4 根据类型写入头信息，合并数据写入新的csv文件并输出
    run()