
from multiprocessing import Pool
import time


# pool 批量创建子线程，灵活控制子线程的数量

# 同步执行：
# 异步执行：

def X_x_X(n):
	print(n*n)
	time.sleep(1)
	return n*n

if __name__ == "__main__":
	pool = Pool(processes=5)
	res_list = []

	for i in range(10):
		# 异步的方式启动进程
		# 如果要同步等待，在每次启动线程后调用res.get(),也可以使用Pool.apply()
		res = pool.apply_async(X_x_X,[i,])
		 # res.get()

		print('---------:',i)
		res_list.append(res)

	pool.close()
	pool.join()
	for r in res_list:
		print("result",(r.get(timeout=5)))

