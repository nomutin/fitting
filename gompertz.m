function phi = gompertz(x)
    global data;
    phi = 0;
    gamma = x(1);
    b = x(2);
    
    for i = 1:length(data)-1
        t = data(1, i);
        pt = data(2, i);
        delta = (data(2, i+1) - data(2, i));
        
        phi = phi + (gamma - b*t - log(delta/pt))^2;
    end
end