import csv


def load_data(_path: str) -> list:
    with open(_path, 'r') as _f:
        reader = csv.reader(_f)
        value = [float(i[-1]) for i in reader]
        index = [int(i) for i in range(len(value))]
        return [index, value]
