function plotting(mode, datarange, xl, yl, ini, interval)
    global data
    plot(data(1,:), data(2,:),'k*', 'DisplayName', 'データ');
    xlabel(xl);
    ylabel(yl);
    xlim([0 datarange]);
    xticks(1:2:datarange)
    xticklabels({1970:8:2100})
    av = mean(data(2,:));
    hold on;
    
    options = optimset('MaxFunEvals', 1000000000, 'MaxIter', 10000000);
    if strmatch('linear', mode)
        linear_params = fminsearch(@linear, 1:2, options);
        linear_eq = "線形: y = " + linear_params(1) + " * (t -"+ini+")/4+ " + linear_params(2);
        fplot(@(x) linear_params(1) * x + linear_params(2), 'DisplayName', linear_eq);
        
        
    end
    
    if strmatch('exponential', mode)
        exponential_params = fminsearch(@exponential, 1:2, options);
        exponential_eq = "指数: y=" + exponential_params(2) + "exp(" + exponential_params(1) + " (t-"+ini+")/4)";
        fplot(@(x) exponential_params(2) * exp(exponential_params(1)*x), 'DisplayName', exponential_eq);
      
        
    
    end
    
    if strmatch('gompertz', mode)
        gompertz_params = fminsearch(@gompertz, 1:2, options);
        gamma = gompertz_params(1);
        b = gompertz_params(2);
        a = exp(gamma);
        c = 0;
        for i = data
            c = c + i(2) * exp(a/b * exp(-b * i(1)));
        end
        c = c/length(data);
        
        
        gompertz_eq = "ゴンペルツ: y=" + c + "exp(-" + a/b + "exp(-" + b + " (t-"+ini+")/4))";
        fplot(@(x) c * exp(-a/b * exp(-b*x)), 'DisplayName', gompertz_eq);
        
        d = 0;
        m = 0;
        for i=data
            d = d + (i(2)-  c * exp(-a/b * exp(-b*i(1))))^2;
            m = m + (i(2) - av)^2;
        end
        r = 1 - d/m
        
       
    end
    
    if strmatch('exp_c', mode)
        exp_c_params = fminsearch(@exp_c, [-2, -2], options);
        a = exp_c_params(1);
        gamma = exp_c_params(2);
        s = gamma / a;
        c = 0;
        for i = data
            c = c + (s-i(2)) * exp(a*i(1));
        end
        c = c/length(data);
        exp_c_eq = "定数項付き指数: y=" + s + "-" + c + "exp(-" + a + " (t-"+ini+")/4)";
        fplot(@(x) s-c*exp(-a*x), 'DisplayName', exp_c_eq);
    end
    
    if strmatch('logistic', mode)
        logistic_params = fminsearch(@logistic, 1:2, options);
        a = logistic_params(1);
        gamma = logistic_params(2);
        s = gamma / a;
        c = 0;
        for i = data
            c = c + (s - i(2)) * exp(gamma * i(1)) / i(2);
        end
        c = c/length(data);
 
        logistic_eq = "ロジスティック: y=" + s + "/(1+" + c + "exp(-" + gamma +" (t-"+ini+")/4))";
        fplot(@(x) s/(1+c*exp(-gamma*x)),'DisplayName', logistic_eq);
        
    end
    
    if strmatch('gomp_c', mode)
        gompertz_c_params = fminsearch(@gomp_c, [-1 1 1000000], options);
        a = gompertz_c_params(1);
        b = gompertz_c_params(2);
        s = gompertz_c_params(3);
        c = 0;
        for i = data
            c = c + (s - i(2)) * exp(-a/b * exp(-b * i(1)));
        end
        c = c/length(data);
        
        gompertz_c_eq = "gomp-const: y=" + s + "-" + c + "exp(" + a/b + "exp(-" + b + " (t-"+ini+")/4))";
        fplot(@(x) s+c*exp(a * exp(-b*x) / b),'DisplayName', gompertz_c_eq);
    end
    
    hold off;
   
end