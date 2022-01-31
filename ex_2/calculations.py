import csv


def read_csv_file(path_to_file):
    rows = []
    with open(path_to_file, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return headers, rows


def write_csv_file(path_to_file, headers: list, row_list: list):
    with open(path_to_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(row_list)


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


def get_rows_with_proper_matching_id(data_rows, matching_id):
    output = []
    for row in data_rows:
        if int(row[4]) == matching_id:
            output.append(row)
    return output


def sort_rows_by_price_desc(data_rows):
    sorted_data = sorted(data_rows, key=lambda x: float(x[1]), reverse=True)
    return sorted_data


def get_top_priced_rows(data_rows: list, rows_amount: int):
    return data_rows[:rows_amount]


if __name__ == "__main__":
    # read files
    data_header, data_rows = read_csv_file("data.csv")
    curr_header, curr_rows = read_csv_file("currencies.csv")
    match_header, match_rows = read_csv_file("matchings.csv")
    # unify data
    unified_data_rows = calculate_total_price_in_pln(curr_rows, data_rows)

    # define what to get
    output = []
    for idx, pair in enumerate(match_rows):
        match_id = pair[0]
        top_count = pair[1]

        # get proper data
        matched_rows = get_rows_with_proper_matching_id(unified_data_rows, int(match_id))
        sorted_rows = sort_rows_by_price_desc(matched_rows)
        top_rows = get_top_priced_rows(sorted_rows, int(top_count))
        for row in top_rows:
            output.append(row)
        print(top_rows)

    write_csv_file("top_products.csv", data_header, output)

#TODO: missing: avg and ignored prod count in output csv file
#TODO: change way of saving initial currency