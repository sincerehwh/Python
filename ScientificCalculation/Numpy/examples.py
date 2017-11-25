


import matplotlib.pyplot as plt
import numpy as np
import numpy.random as np_random
import pylab

print('模拟随机游走')
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

# 画图
plt.title('Random Walk')
limit = max(abs(min(walk)), abs(max(walk)))
plt.axis([0, 1000, -limit, limit])
x = np.linspace(0, 1000, 1000)
plt.plot(x, walk, 'g-')
plt.show()

''' 

points = np.arange(-5,5,0.01)
print(points)

xs,ys = np.meshgrid(points,points)  #xs,ys互为转置矩阵
print(xs)
print(ys)

z = np.sqrt(xs ** 2,ys ** 2 )
print(z)

plt.imshow(z,cmap = plt.cm.gray)
plt.colorbar()
plt.title("HHH")
pylab.show()

'''