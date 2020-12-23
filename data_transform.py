import pandas as pd

from utils.file_utils import remove_files_by_dir, get_filename_list, check_dirs, get_desktop_path
from utils.wash_data_utils import wash_data

# excel生成csv，并且清洗

excel_file_root_path = get_desktop_path() + '/newDataExcelList/'

new_csvFile_root_path = get_desktop_path() + '/csvFile/'


def output_csv(df, path):
    csv_path = new_csvFile_root_path + path.split(".")[0] + ".csv"
    print("正在写入：" + csv_path)
    df.to_csv(csv_path)
    print("写入完成")


def get_headers(path):
    headers = []
    file = pd.ExcelFile(path)
    sheet = file.parse("Sheet1")
    for i in sheet:
        headers.append(i)
    return headers


def run():
    check_dirs([new_csvFile_root_path])
    remove_files_by_dir(new_csvFile_root_path)
    file_list = get_filename_list(excel_file_root_path)
    for f in file_list:
        output_csv(read_excel(f), f)
    wash_data(new_csvFile_root_path)


def read_excel(path):
    print("当前excel文件：" + path)
    df = pd.read_excel(excel_file_root_path + path)
    return df


if __name__ == '__main__':
    run()

