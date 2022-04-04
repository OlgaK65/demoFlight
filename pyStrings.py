import pandas as pd

def lambda_row(row):

    dep = row['Departure']
    arv = row['Arrival']
    return str_to_num(dep) - str_to_num(arv) >= 3

def get_success():
    str_fl = pd.read_csv("flights.csv", skipinitialspace=True)

    str_fl['success'] = str_fl.apply(lambda row: lambda_row(row), axis=1)

    print(str_fl["success"])


def str_to_num(p_str):

    str_str = ""

    for x in range(0, 2):
        a = p_str[x]
        if (a != '0') | (x > 0):
            str_str += p_str[x]

    str_str += "."
    for x in range(3, 5):
        a = p_str[x]
        if (a != '0') | (x > 3):
            str_str += p_str[x]

    return pd.to_numeric(str_str)


if __name__ == '__main__':
    get_success()
