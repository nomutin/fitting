function phi = linear(x)
    global data;
    phi = 0;
    for i = data
        phi = phi + (i(1) * x(1) + x(2) - i(2))^2;
    end
end