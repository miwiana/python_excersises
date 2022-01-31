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


def get_rows_with_matching_id_1(output_file_path):
    rows_with_matching_id_1 = []

    rows = get_rows(output_file_path)
    for row in rows:
        if int(row[4]) == 1:
            rows_with_matching_id_1.append(row)
    return rows_with_matching_id_1


def get_rows_with_matching_id_2(output_file_path):
    rows_with_matching_id_2 = []

    rows = get_rows(output_file_path)
    for row in rows:
        if int(row[4]) == 2:
            rows_with_matching_id_2.append(row)
    return rows_with_matching_id_2


def get_rows_with_matching_id_3(output_file_path):
    rows_with_matching_id_3 = []

    rows = get_rows(output_file_path)
    for row in rows:
        if int(row[4]) == 3:
            rows_with_matching_id_3.append(row)
    return rows_with_matching_id_3
