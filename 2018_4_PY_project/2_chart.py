

# 注册账号：https://www.reportlab.com/accounts

# 安装：pip3 install rlextra -i https://www.reportlab.com/pypi

# 获取数据: https://www.swpc.noaa.gov/


from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF
from reportlab.lib import colors

data = [
#   UTC,Radio Flux   Planetary   Largest
#  Date, 10.7 cm,A Index    Kp Index
(1,72,5,2),
(2,72,5,2),
(3,72,5,2),
(4,72,12,4),
(5,72,10,4),
(6,72,5,2),
(7,72,5,2),
(8,69,5,2),
(9,69,5,2),
(10,69,5,2),
(11,69,5,2),
(12,69,5,2),
(13,69,5,2),
(14,69,5,2),
(15,69,5,2),
(16,69,5,2),
(17,69,5,2),
(18,69,5,2),
(19,69,5,2),
(20,69,5,2),
(21,70,10,4),
(22,70,15,4),
(23,70,15,4),
(24,70,10,4),
(25,70,10,4),
(26,70,5,2),
(27,70,5,2)
]

# Date
date = []

# Radio Flux 
radio_flux  = []

# Planetary
planetary = []

# Largest Kp
largest_kp = []


for row in data:
	print(row)
	date.append(row[0]*10)
	radio_flux.append(row[1]+100)
	planetary.append(row[2]+100)
	largest_kp.append(row[3]+100)

# d = Drawing(500,300)
# d.add(PolyLine(list(zip(date,radio_flux)),strokeColor=colors.blue))
# d.add(PolyLine(list(zip(date,planetary)),strokeColor=colors.red))
# d.add(PolyLine(list(zip(date,largest_kp)),strokeColor=colors.green))
# d.add(String(50,200," Space Weather Outlook Table ",fontSize=14,fillColor=colors.black))
# renderPDF.drawToFile(d,"hello.pdf","")

d = Drawing(500,300)

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 200
lp.width = 300
lp.data = [list(zip(date,radio_flux)),list(zip(date,planetary)),list(zip(date,largest_kp))]
lp.lines[0].strokeColor =  colors.blue
lp.lines[1].strokeColor =  colors.red
lp.lines[2].strokeColor =  colors.green
d.add(lp)
d.add(String(50,200," Space Weather Outlook Table ",fontSize=14,fillColor=colors.black))
renderPDF.drawToFile(d,"hello.pdf","")













