import csv


def load_data(_path: str, data_column: int = -1) -> list:
    """ data_column行目を0から始まる時系列データとする """
    with open(_path, 'r') as _f:
        return [float(c[data_column]) for c in csv.reader(_f)]
