
def get_n_value():
    try:
        n = int(input("Please enter the first number (N): "))
    except ValueError:
        print("Entered sign is not an integer. Try again")
    return n


def get_m_value():
    try:
        m = int(input("Please enter the second number (M) which is > than first one: "))
    except ValueError:
        print("Entered sign is not an integer. Try again")
    return m


def validate_input_numbers(n, m):
    "Input numbers must follow condition: 1 <= n < m <=10000"
    flag = True
    if n > m:
        flag = False
        print("Provided numbers did not follow condition: n < m ")

    if n < 1:
        flag = False
        print("Provided N number is lower than 1 ")

    if m > 10000:
        flag = False
        print("Provided M number is greater than 10000 ")

    if flag == False:
        raise ValueError("Provided data did not follow expected condition")


if __name__ == "__main__":
    n = get_n_value()
    m = get_m_value()
    validate_input_numbers(n, m)
