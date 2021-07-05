from fitting import *

if __name__ == '__main__':
    data = csvTreat.load_data('data/export.csv')
    # p = Param(data, ['logistic'])
    # print(p.estimated_params['logistic']['full'])
    # print(p.estimated_params['logistic']['equ'])
    mode = ['linear', 'exponential', 'exponential_constant', 'gompertz', 'logistic']
    param = prameterPredict.Param(data=data, mode=mode)
    plotting.plot(data=data, param=param.estimated_params, mode=mode)
