import csv


def read_csv_file(path):
    with open(path, 'r') as f:
        file = csv.reader(f)
    return file


def read_header(path):
    with open(path, 'r') as f:
        file = csv.reader(f)
        row = 0
        header = []
        for i in file:
            if row >= 1:
                return header
            header = i
            row += 1
        return header


def read_line(path):
    lines = []
    with open(path, 'r') as f:
        file = csv.reader(f)
        row = 0
        for i in file:
            if row == 0:
                row += 1
                pass
            else:
                lines.append(i)
    return lines

