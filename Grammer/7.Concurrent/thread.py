

# 1.每个独立的线程 有自己入口、执行序列、程序出口
# 2.线程的运行可以被抢占（中断）、暂时被挂起了（休眠）、让其他线程运行（让步）
# 3.一个进程的各个线程间可以共享同一片数据空间


# 全局解释器锁 GIL
# GIL不是python的特性，是实现python解释器（CPython）时引入的概念
# GIL是一把全局排他锁，同一时间只有一个线程在运行
# multiprocessing 使用了多进程，每个进程有自己的独立GIL，不会出现进程之间的GIL争抢


from threading import Thread
import time 


''' 单线程 '''

def my_counter():
	i = 0
	for _ in range(100000000):
		i = i + 1
	return True

def main():
	thread_array = {}
	start_time = time.time()
	for tid in range(2):
		t = Thread(target=my_counter)
		t.start()
		t.join() # 阻塞进程，直到线程执行完成
	end_time = time.time()
	print("total time: {}".format(end_time - start_time))

if __name__ == "__main__":
	main()



# ''' 两个并发线程 '''
# def main1():
# 	thread_array = {}
# 	start_time = time.time()
# 	for tid  in range(2):
# 		t = Thread(target=my_counter)
# 		t = start()
# 		thread_array[tid] = t

# 	for i in range(2):
# 		thread_array[i].join()
# 	end_time = time.time()
# 	print("Total time: ".format(end_time-start_time))

# if __name__ == "__main__":
# 	main1()

