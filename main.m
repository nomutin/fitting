clear variables;
clc;

global data;
data = loadData('data/Book1.csv', 5);

mode = {'logistic'};
xlabel = '西暦(年)';
ylabel = '1mm^{-2}あたりのlog_{10}(トランジスタ数)';
ini = 1970;
interval = 1;
plotting(mode, 35, xlabel, ylabel, ini, interval);