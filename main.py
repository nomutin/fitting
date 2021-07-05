import csv
from fitting.prameterPredict import Param
from fitting.plotting import Plot


def load_data(_path: str, data_column: int = -1) -> list:
    """ data_column行目を0から始まる時系列データとする """
    with open(_path, 'r') as _f:
        return [float(c[data_column]) for c in csv.reader(_f)]


if __name__ == '__main__':
    data = load_data('data/export.csv')
    # p = Param(data, ['gompertz'])
    # print(p.estimated_params['gompertz']['full'])
    # print(p.estimated_params['gompertz']['equ'])
    mode = ['linear']
    Plot(data=data, mode=mode)





