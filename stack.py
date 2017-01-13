class StackOfPlates:
	NumOfPlates=0
	setofstacks=[0]
	def __init__(self,th):
		self.treshold=th
		print "Create A class"

	def push(self):
		if self.setofstacks[-1]<self.treshold:
			self.setofstacks[-1]+=1
		else:
			self.setofstacks.append(1)

	def pop(self):
		if self.setofstacks[-1]==1:
			self.setofstacks[-1]-=1
			if len(self.setofstacks)>1:
				self.setofstacks.remove(self.setofstacks[-1])
		elif self.setofstacks[-1]>1:
			self.setofstacks[-1]-=1

	def popAt(self,index):
		counter=0
		if index<len(self.setofstacks):
			while len(self.setofstacks)-1!=index:
				self.pop()
				counter+=1

			self.pop()

			while counter>0:
				counter-=1
				self.push()


#smaple run
x=StackOfPlates(4)
for i in range(0,30):
	x.push()

print x.setofstacks
for i in range(0,5):
	x.pop()


print x.setofstacks

x.popAt(2)
x.popAt(5)
print x.setofstacks
