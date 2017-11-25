
from enum import Enum
Month =  Enum("Month",("January","February","April","May"))

for name,member in Month.__members__.items():
	print(name,"=>",member,member.value) 

j = Month.January
print(j)
