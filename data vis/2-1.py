import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

np.random.seed(0)

x_data = np.array(range(1,13,1))
y_data_max = [39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25]
y_data_min = [21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18]


def test_func(x, a, b,c):
    return (a*np.sin(b * x))+c

params_max,_ = optimize.curve_fit(test_func, x_data, y_data_max,
                                               p0=[30, 0.3, 52])
a_max,b_max,c_max = params_max[0], params_max[1],params_max[2]


params_min,_ = optimize.curve_fit(test_func, x_data, y_data_min,
                                               p0=[30, 0.3, 52])
a_min,b_min,c_min = params_min[0], params_min[1],params_min[2]

plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data_max, color='r')
plt.scatter(x_data, y_data_min, color='b')

x_axis = np.linspace(1,12,num=100)
plt.plot(x_axis,test_func(x_axis, a_max, b_max,c_max),color='r')
plt.plot(x_axis,test_func(x_axis, a_min, b_min,c_min),color='b')
plt.ylabel('Temprature(*C)')
plt.xlabel('Month')

plt.show()
