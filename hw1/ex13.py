# an experiment with ex 1.3 #
import matplotlib.pyplot as plt;
import random;
import math;

grids = 2000;
x_init = 0.0;
x_end = 2.0;
dx = (x_end - x_init)/grids;

f = lambda x: -x**2 + 2*x;
x = [x_init+j*dx for j in range(grids+1)];
y = [f(s) for s in x];

N = 10000;
samples = [[random.uniform(0,2), random.uniform(0,1)] for j in range(N)];
count = 0;

for sample in samples:
    if f(sample[0]) > sample[1]:
        count += 1;
    

def cal_area():
    ratio = float(count)/N;
    area = 2*ratio;
    return area, (area-(4.0/3))/(4.0/3);
print "the simulated area is", cal_area()[0];
print "the theoretical area is", float(4.0/3);
print "the relative error with respect to the theretical result is", cal_area()[1]


plt.figure(1)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Exercise 1.3")
plt.savefig("ex13.eps")
