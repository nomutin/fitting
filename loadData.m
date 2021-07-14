function data = loadData(filename, load_index)
    data = importdata(filename);
    data = [(1:length(data)).' - 1, data(1:length(data),load_index)].';
end