

## 福利彩票3D玩法:

# “单选”、“组选”、“1D”、“2D”、“通选”、“和数”、“包选”、“猜大小”、“猜1D”、“猜2D”、“猜三同”、“拖拉机”、“猜奇偶”等投注方式，具体规定如下：

# （一）单选投注：是指对三个号码以唯一的排列方式进行投注。

# （二）组选投注：是指将三个号码的所有排列方式作为一注投注号码进行投注。如果一注组选的三个号码中有两个号码相同，则包括三种不同的排列方式，称为“组选3”；如果一注组选的三个号码各不相同，则包括六种不同的排列方式，称为“组选6”。

# （三）1D投注：是指对百位、十位或个位中某一特定位置上的号码进行投注。

# （四）猜1D投注：是指对百位、十位或个位中任意一个位置上的号码进行投注。

# （五）2D投注：是指对百位和十位、十位和个位或百位和个位号码，以唯一的排列方式进行投注。

# （六）猜2D投注：是指对百位、十位或个位中任意两个位置上的号码进行投注。

# （七）通选投注：是指对三个号码以唯一的排列方式进行投注。

# （八）和数投注：是指对三个号码相加之和进行投注。

# （九）包选投注：是指同时用单选和组选的方式对三个号码进行投注。如果三个号码中有两个号码相同，则包括三种不同的排列方式，称为“包选3”；如果三个号码各不相同，则包括六种不同的排列方式，称为“包选6”。

# （十）猜大小投注：是指对三个号码相加之和的大、小性质进行投注。其中，三个号码相加之和在19（含）至27（含）之间时为大，在0（含）至8（含）之间时为小。

# （十一）猜三同投注：是指对全部三个相同的号码进行投注。

# （十二）拖拉机投注：是指对全部以升序或降序连续排列的号码进行投注（890、098、901、109除外）。

# （十三）猜奇偶投注：是指对全部三个号码的奇数、偶数性质进行投注。其中，1、3、5、7、9为奇，0、2、4、6、8为偶。


from enum import Enum

class GameType(Enum):
	''' 投注的类型 '''
	single 			= 0
	group3  		= 1

	oneD 			= 2	
	betOne  		= 21
	twoD 			= 3
	betTwoDSame		= 31

	singleSelect 	= 4
	sumNumber		= 5
	allSelect 		= 6
	betBigSmall		= 7
	
	bet3Same		= 10
	tractors		= 11
	betEvenOdd 		= 12

class GameBonus(Enum):
	''' 奖金的类型 '''

	single 		= 'single' 
	group3 		= 'group3'
	group6 		= 'group6'
	oneD 		= 'oneD'
	betOneD1	= 'betOneD1'
	betOneD2 	= 'betOneD2'
	betOneD3 	= 'betOneD3'
	twoD 		= 'twoD'
	betTwoDSame = 'betTwoDSame'
	betTwoDDiff = 'betTwoDDiff'
	singleSelect1 = 'singleSelect1'
	singleSelect2 = 'singleSelect2'

	sum0_27  =  'sum0_27'
	sum1_26  =  'sum1_26'
	sum2_25  =  'sum2_25'
	sum3_24  =  'sum3_24'
	sum4_23  =  'sum4_23'
	sum5_22  =  'sum5_22'
	sum6_21  =  'sum5_22'
	sum7_20  =  'sum7_20'
	sum8_19  =  'sum8_19'
	sum9_18  =  'sum9_18'
	sum10_17 =  'sum10_17'
	sum11_16 =  'sum11_16'
	sum12_15 =  'sum12_15'
	sum13_14 =  'sum13_14'
	allSelectAll    =  'allSelectAll'
	allSelectGroup  =  'allSelectGroup'
	betBigSmall 	=  'betBigSmall'
	bet3Same 		=  'bet3Same'
	tractors 		=  'tractors'
	betEvenOdd 		=  'betEvenOdd'

	pass

dic = {
		'single':1040,
		'group3':346,
		'group6':173,
		'oneD':10,
		'betOneD1':2,
		'betOneD2':12,
		'betOneD3':230,
		'twoD':104,
		'betTwoDSame':37,
		'betTwoDDiff':19,
		'singleSelect1': 470,
		'singleSelect2': 21,
		'sum0_27': 1040,
		'sum1_26': 345,
		'sum2_25': 172,
		'sum3_24': 104,
		'sum4_23': 69,
		'sum5_22': 49,
		'sum6_21': 37,
		'sum7_20': 29,
		'sum8_19': 23,
		'sum9_18': 23,
		'sum10_17': 16,
		'sum11_16': 15,
		'sum12_15': 15,
		'sum13_14': 14,
		'allSelectAll': 693,
		'allSelectGroup': 173,
		'betBigSmall': 6,
		'bet3Same':	104,
		'tractors':	65,
		'betEvenOdd': 8
	  }



class ThreeD(object):
	''' 3D '''

	@classmethod
	def randomNotes(type):
		pass


print(dic)










