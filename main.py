"""
Usage:
    data = CSVTreat.load_data('data/export.csv')
    mode = ['linear', 'exponential', 'exponential_constant', 'gompertz', 'logistic', 'gompertz_constant']
    param = Parameters.Param(data=data, mode=mode)
    Plotting.plot(data=data, param=param.estimated_params, mode=mode, graph_range=40, graph=True, initial=1986)

"""
from fitting import *

if __name__ == '__main__':
    pass
