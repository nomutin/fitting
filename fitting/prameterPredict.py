import numpy as np
from scipy.optimize import minimize


class ObjectiveFunction:
    @staticmethod
    def linear_objective(params, data):
        a, c = params
        return sum([(a * t + c - pt) ** 2 for t, pt in enumerate(data)])

    @staticmethod
    def exponential_objective(params, data):
        a, c = params
        phi = sum([(a * t + np.log(c) - np.log(pt)) ** 2 for t, pt in enumerate(data)])
        return phi

    @staticmethod
    def exponential_constant_objective(params, data):
        a, gamma = params
        return sum([(gamma - a * data[t] - (data[t+1] - data[t])) ** 2 for t in range(0, len(data)-1)])

    @staticmethod
    def gompertz1_objective(params, data):
        gamma, b = params
        return sum([(gamma - b * t - np.log((data[t+1] - data[t]) / data[t])) ** 2 for t in range(0, len(data)-1)])

    @staticmethod
    def gompertz2_objective(params, data):
        alpha, b, c = params
        for t, pt in enumerate(data):
            phi += pt - c * np.exp()


class Param:
    def __init__(self, data: list, mode: list):
        self.data = data
        self.estimated_params = {}

        if 'linear' in mode:
            self.linear()
        if 'exponential' in mode:
            self.exponential()
        if 'exponential_constant' in mode:
            self.exponential_constant()

    def linear(self):
        popt = minimize(fun=ObjectiveFunction.linear_objective, args=(self.data, ),
                        x0=np.array([1.0, 1.0]), method='Nelder-Mead', options={'maxiter': 100000})
        self.estimated_params.update({'linear': {'full': popt, 'a': popt['x'][0], 'c': popt["x"][1],
                                                 'success': popt["success"],
                                                 'equ': f'y = {popt["x"][0]} + {popt["x"][1]}'}})

    def exponential(self):
        popt = minimize(fun=ObjectiveFunction.exponential_objective, args=(self.data,),
                        x0=np.array([1.0, 1.0]), method='Nelder-Mead', options={'maxiter': 100000})
        a = popt['x'][0]
        c = popt['x'][1]
        self.estimated_params.update({'exponential': {'full': popt, 'a': a, 'c': c,
                                      'success': popt["success"], 'equ': f'y = {c} * exp({a} * t)'}})

    def exponential_constant(self):
        popt = minimize(fun=ObjectiveFunction.exponential_constant_objective, args=(self.data, ),
                        x0=np.array([1.0, 1.0]), method='Nelder-Mead', options={'maxiter': 100000})
        a = popt['x'][0]
        gamma = popt['x'][1]
        s = gamma / a
        c = sum([(s - pt) * np.exp(a*t) for t, pt in enumerate(self.data)]) / len(self.data)
        self.estimated_params.update({'exponential_constant': {'full': popt, 'a': a, 'c': c, 'gamma': gamma, 's': s,
                                      'success': popt["success"], 'equ': f'y = {s} - {c} * exp(-{a} * t)'}})

    def gompertz(self):
        popt = minimize(fun=ObjectiveFunction.gompertz1_objective, args=(self.data,),
                        x0=np.array([1.0, 1.0]), method='Nelder-Mead', options={'maxiter': 100000})
        gamma = popt['x'][0]
        b = popt['x'][1]
        a = np.exp(gamma)
        alpha = a / b
        c = sum([pt * np.exp(alpha * np.exp((-1) * b * t)) for t, pt in enumerate(self.data)]) / len(self.data)
