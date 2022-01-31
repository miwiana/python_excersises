import csv


def read_csv_file(path_to_file):
    rows = []
    with open(path_to_file, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return headers, rows


def get_headers(path_to_file):
    headers, rows = read_csv_file(path_to_file)
    return headers


def get_rows(path_to_file):
    headers, rows = read_csv_file(path_to_file)
    return rows

