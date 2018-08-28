import random

class  DoubleColorBall(object):
	''' 双色球 
		
		生成投注
		校验中奖
	'''
	def __init__(self, arg):
		super( DoubleColorBall, self).__init__()
		self.arg = arg


	@classmethod
	def inputNote(cls,numbers):
		''' 
		rendNumbers格式:
		[[1,2,3,4,5,6,8],[1,2,3,4,5,6,9]] 

		前六位是红球,最后一位是篮球	

		'''
		return numbers


	@classmethod	
	def randomNotes(cls,count,same=False):
		''' 随机产生投注:
				count: 随机产生注数
				same:  是否重复
		'''
		notes = []
		for i in range(count):
			oneNote = cls.randomOneNote()
			if same:
				return [oneNote] * count
			notes.append(oneNote)
		return notes


	@classmethod
	def randomOneNote(cls):
		numbers = []
		while len(numbers) < 6:
			redNumber = random.randint(1,33)
			if redNumber not in numbers:
				numbers.append(redNumber)
		numbers.sort()
		blueNumber = random.randint(1,16)
		numbers.append(blueNumber)
		return numbers


	@classmethod
	def checkWin(cls,winNumbers,notes):
		''' 
		parameters:
			winNumbers: 中奖的号码
				[1,2,4,5,6,7,8] 
			notes: 下的注
				[[1,2,3,4,5,6,8],[1,2,3,4,5,6,9]] 

			⚠️ 前六位是红球,最后一位是篮球	⚠️
			

		return:
			[[0,<等级>],[1,<等级>],]
			等级
			1: 
			2: 
			3: 3000元
			4: 200元
			5: 10元
			6: 5元
		'''
		results = []
		for (index,note) in enumerate(notes):
			winBlueCount = 0
			winRedCount = 0
			level = 7
			for i in range(6):
				if note[i] in winNumbers[:6]:
					winBlueCount = winBlueCount + 1
			if note[6] == winNumbers[6]:
				winRedCount = 1

			if winBlueCount == 6 and winRedCount == 1:   # 6 + 1
				level = 1
			elif  winBlueCount == 6:					 # 6 + 0
				level = 2
			elif winBlueCount == 5 and winRedCount == 1: # 5 + 1
				level = 3
			elif winBlueCount == 5: 					 # 5 + 0
				level = 4
			elif winBlueCount == 4 and winRedCount == 0: # 4 + 0
				level = 5
			elif winBlueCount == 3 and winRedCount == 1: # 3 + 1
				level = 5
			elif winRedCount == 1:
				level = 6
			else:
				level = 7
			results.append([index,level])
		return results


	@classmethod
	def calucateTotalBonus(clv,notes):
		''' 
		计算总奖金 
		return 总奖金额
		'''
		total = 0
		levelBonus = [5_000_000,100_000,3000,200,10,5,0]
		for note in notes:
			total = total + levelBonus[note[1]-1]
		return total


totalCost = 0
totalBonus = 0
eachNoteNumber = 100
level1Times = 0

for i in range(1000):
	notes =  DoubleColorBall.randomNotes(eachNoteNumber,False)
	result = DoubleColorBall.randomNotes(count=1)[0]
	results = DoubleColorBall.checkWin(result, notes) 
	bouns =  DoubleColorBall.calucateTotalBonus(results)
	totalCost = eachNoteNumber * 2 + totalCost
	totalBonus = totalBonus + bouns

print("Total Cost: ",totalCost)
print("Total Bonus :",totalBonus)	
print("percent:%s " % str(totalBonus/totalCost))



