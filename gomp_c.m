function phi = gomp_c(x)
    global data;
    phi = 0;
    a = x(1);
    b = x(2);
    s = x(3);
    for i = 1:length(data)-1
        t = data(1, i);
        pt = data(2, i);
        delta = data(2, i+1) - data(2, i);
        phi = phi + (log(s-pt) - b * t -log(delta) + log(a))^2;
    end
     
end