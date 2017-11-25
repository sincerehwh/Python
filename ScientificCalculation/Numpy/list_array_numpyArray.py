import timeit

''' 
效率对比
    • 三种数据结构:list / array / numpy.array 
    • 三种方法求和:for / sum / numpy.sum
'''


common_for = """
for d in data:
    s += d
"""

common_sum = """
sum(data)
"""

common_numpy_sum = """
numpy.sum(data)
"""

def timeit_list(n, loops):
    list_setup = """
import numpy
data = [1] * {}
s = 0
""".format(n)
    print('\nlist:')
    print(timeit.timeit(common_for, list_setup, number = loops))
    print(timeit.timeit(common_sum, list_setup, number = loops))
    print(timeit.timeit(common_numpy_sum, list_setup, number = loops))

def timeit_array(n, loops):
    array_setup = """
import numpy
import array
data = array.array('L', [1] * {})
s = 0
""".format(n)
    print('\narray:')
    print(timeit.timeit(common_for, array_setup, number = loops))
    print(timeit.timeit(common_sum, array_setup, number = loops))
    print(timeit.timeit(common_numpy_sum, array_setup, number = loops))

def timeit_numpy(n, loops):
    numpy_setup = """
import numpy
data = numpy.array([1] * {})
s = 0
""".format(n)
    print('\nnumpy:')
    print("for: ",timeit.timeit(common_for, numpy_setup, number = loops))
    print("sum: ",timeit.timeit(common_sum, numpy_setup, number = loops))
    print("numpy_sum:",timeit.timeit(common_numpy_sum, numpy_setup, number = loops))

if __name__ == '__main__':
    timeit_list(500000, 500)
    timeit_array(500000, 500)
    timeit_numpy(500000, 500)



