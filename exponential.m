function phi = exponential(x)
    global data;
    a = x(1);
    c = x(2);
    phi = 0;
    for i = data
        t = i(1);
        pt = i(2);
        phi = phi + (t * a + log(c) - log(pt))^2;
    end
end