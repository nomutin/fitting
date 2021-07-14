function phi = exp_c(x)
    global data;
    phi = 0;
    a = x(1);
    gamma = x(2);
    for i = 1:length(data)-1
        pt = data(2, i);
        delta = data(2, i+1) - data(2, i);
        phi = phi + (gamma - a * pt - delta)^2;
    end
end