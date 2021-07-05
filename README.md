# 都市工学のやつ

## Usage
日本人口(1986〜2000)

```
data = CSVTreat.load_data('data/example.csv')
mode = ['linear', 'exponential', 'exponential_constant', 'gompertz', 'logistic', 'gompertz_constant']
param = Parameters.Param(data=data, mode=mode)
Plotting.plot(data=data, param=param.estimated_params, mode=mode, graph_range=40, graph=True, initial=1986)
```