

# 进程 ： 有自己的空间和数据栈，不能直接共享信息，需要进程间通信

# import os 

# print("Process (%s) start ... " % os.getpid())

# pid = os.fork() # 调用一次，在子进程返回0，在父进程返回子进程ID，子进程中getppid()可以拿到父进程的ID

# if pid==0:
# 	print("I am child process (%s) and my parent is %s" % (os.getpid(),os.getppid()))
# else:
# 	print("I %s jsut created a child process (%s)" % (os.getpid(),pid))



# from multiprocessing import Process
# ''' multiprocessing 是跨平台的多进程模块 提供一个Process类代表一个进程对象 '''

# import time

# def f(n):
# 	time.sleep(1)
# 	print(n**n)

# if __name__ == "__main__":
# 	for i in range(10):
# 		p = Process(target=f,args=[i,])
# 		p.start()
# 		# p.join() 上一个进程执行完成后，其他的进程再执行

''' 进程间通信 '''

from multiprocessing import Process,Queue 
import time

# queue 多进程的安全队列 ，实现多进程之间的数据传递

def write(q):
	for i in ['A','B','C','D','E']:
		q.put(i)
		time.sleep(1)

def read(q):
	while  True:
		v = q.get(True)

if __name__ == "__main__":
	q = Queue()
	pw = Process(target=write,args=[q,])
	pr = Process(target=read,args=[q,])
	pw.start()
	pr.start()
	pr.join()
	pr.terminate() 












