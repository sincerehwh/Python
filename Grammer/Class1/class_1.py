# sdmfl'ksmdlkfmlsak
# sdfsadfa
# String splice 
# 字符串拼接
def string_splice():
    name = input("Input name :")
    where = input("Input where :")
    work = input("Input work :")
    total = "{} work as {} in {} !".format(name,work,where)
    print(total)


# Sum of integer sequences
# 整数序列求和
def sum_N():
    n = input("Input number N :")
    sum = 0
    for i in range(int(n)):
        sum += i + 1
    print("1到{}的和是：{}".format(n,sum))


# Output Multiplication table
# 输出九九乘法表
def print_9X9_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print("{} X {} = {} ".format(j,i,i*j))
        print("------")


# Factorial calculation
# 阶乘计算
def get_calculation():
    num = input("Input number N :")
    sumString = ""
    sum = 0
    for i in range(0,int(num)):
        sumString += "{}!+".format(i)
        sumNumber = 0
        for j in range(0,i):
            j = j+1
            sumNumber = j*(j+1)    
    print(sumString[len(sumString)-1],"={}".format(sumNumber))


print_9X9_table()

