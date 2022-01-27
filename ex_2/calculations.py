import csv


def read_csv_file(path_to_file):
    rows = []
    with open(path_to_file, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return headers, rows


def calculate_total_price_in_pln(currencies, data_rows):
    curr_for_calc = {}
    for curr in currencies:
        curr_for_calc.update({curr[0]: float(curr[1])})

    for row in data_rows:
        # count total price as price * quantity
        total_price = int(row[1]) * int(row[3])
        # count all prices in one currency (in PLN)
        multiplier = curr_for_calc[row[2]]
        total_price_in_pln = total_price * multiplier
        row[1] = str(total_price_in_pln)
        # change quantity to 1 and currency to PLN to reduce confusion
        row[2] = "PLN"
        row[3] = 1
    return data_rows


if __name__ == "__main__":
    data_header, data_rows = read_csv_file("data.csv")
    curr_header, curr_rows = read_csv_file("currencies.csv")
    match_header, match_rows = read_csv_file("matchings.csv")
    unified_data_rows = calculate_total_price_in_pln(curr_rows, data_rows)

