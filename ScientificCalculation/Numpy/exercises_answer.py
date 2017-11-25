
''' 方法1:标准方法计算Dij
• D[i, j] = numpy.linalg.norm(X[:, i], X[:, j) ** 2
'''




''' 方法2:利用dot计算Dij
• d=X[:,i]-X[:,j]
• D[i, j] = numpy.dot(d, d)
'''



''' 方法3:减少dot调用次数
• Dij = (xi - xj)T(xi - xj) = xiTxi - 2xiTxj + xjTxj
• G = numpy.dot(X.T, X) • Dij =Gii -2Gij +Gjj
'''



''' 方法4:利用重复操作替代外部循环
• 在方法3的基础上，将D表达为H + K - 2G
• Hij =Gii,Kij =Gjj
• H = numpy.title(np.diag(G), (n, 1))
• K=HT
• D=H+HT-2G
'''


import numpy as np
import numpy.linalg as la
import time

X = np.array([range(0, 500), range(500, 1000)])
m, n = X.shape

t = time.time()
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        D[i, j] = la.norm(X[:, i] - X[:, j]) ** 2
        D[j, i] = D[i, j]
print(time.time() - t)

t = time.time()
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        d = X[:, i] - X[:, j]
        D[i, j] = np.dot(d, d)
        D[j, i] = D[i, j]
print(time.time() - t)

t = time.time()
G = np.dot(X.T, X)
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        D[i, j] = G[i, i] - G[i, j] * 2 + G[j,j]
        D[j, i] = D[i, j]
print(time.time() - t)

t = time.time()
G = np.dot(X.T, X)
H = np.tile(np.diag(G), (n, 1))
D = H + H.T - G * 2
print(time.time() - t)