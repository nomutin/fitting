clear variables;
clc;

global data;
data = loadData('data/example.csv', 2);

mode = {'linear', 'exponential', 'gompertz', 'exp_c', 'logistic'};

plotting(mode, 25);