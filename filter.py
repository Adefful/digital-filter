"""
            Digital Filter
github: https://github.com/Adefful/digital-filter

функция: Acos(a*2pi*x) + Bcos(b*2pi*x) ++ ....

где amplitude: A,B, ...
    frequency: a,b, ...
    n: частота дискретизации
[a,b] отрезок на котором отображается функция

v1.0.0 - используется метод прямоугольников

"""
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
import math

options = {
    'n': 64,
    'amplitude':  [6, 6, 1, 2],
    'frequency': [2, 3,23,28]
}
 
def __main__():
    n = options['n']
    ampl_lst = np.array(options['amplitude'])
    freq_lst = np.array(options['frequency'])
    a = 0 
    b = 1
    nT = np.linspace(a,b,n)
    print("nT")
    print(nT)
    Xn = np.array([ampl_lst[x]*np.cos(2 * math.pi * freq_lst[x] * nT) for x in range(len(ampl_lst))])
    func = np.array(reduce(lambda a,b: np.add(a,b), Xn))
    print("func")
    print(func)
    plt.plot(nT, func, label="Function One", color="g")
    Yn = [reduce(lambda i,j: i+j, func[x:x+5])/5 for x in range(len(func - 5))]  #bug fixed
    print("Yn")
    print(Yn)
    plt.plot(nT[2:], Yn[:-2], label="filter", color="b")
    ak = np.array([(2/n)*np.sum(Yn*Xn[x]/ampl_lst[x]) for x in range(len(Xn))])
    print("ak")
    print(ak[0])
    Yt = np.array([(Xn[x]/ampl_lst[x])*ak[x] for x in range(len(ampl_lst))])
    func2 = np.array(reduce(lambda a,b: np.add(a,b), Yt))
    plt.plot(nT, func2, label="Function Two", color="r")
    plt.legend()
    plt.show()

__main__()