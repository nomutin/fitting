from fitting import *

if __name__ == '__main__':
    data = CSVTreat.load_data('data/example.csv')
    mode = ['linear', 'exponential_constant', 'gompertz', 'logistic', 'gompertz_constant']
    param = Parameters.Param(data=data, mode=mode)
    Plotting.plot(data=data, param=param.estimated_params, mode=mode, graph_range=0, graph=True, initial=1985)

