import csv


def read_csv_file(path_to_file):
    rows = []
    with open(path_to_file, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return headers, rows


if __name__ == "__main__":
    data_header, data_rows = read_csv_file("data.csv")
    curr_header, curr_rows = read_csv_file("currencies.csv")
    match_header, match_rows = read_csv_file("matchings.csv")
