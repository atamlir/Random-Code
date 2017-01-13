
"""
def find_near_letters(letter):
	if letter=="a": return ["a","z","q"]
	if letter=="s": return ["s","w","a","d"]
	if letter=="x": return ["s","z","d"]

def permutation(words,possible_letters):
	print words,possible_letters
	lis1=[]
	for i in words:
		for j in possible_letters:
			lis1.append(j+i)
	return lis1

def nearbywords(word,index):
	if index>=len(word): return ['']
	permutations_num=nearbywords(word,index+1)
	possible_letters=find_near_letters(word[index])

	return permutation(permutations_num,possible_letters)




print len(nearbywords("xsa",0))
"""
"""
def permutation(words,possible_letters):
	print words,possible_letters
	lis1=[]
	for i in words:
		for j in possible_letters:
			lis1.append(j+i)
	return lis1

def createP(n,num1,num2):
	print num1,num2,n
	if num1==n and num2==n: return [""]
	if num2==n: return [""]
	combi2=["("+e for e in createP(n,num1+1,num2) if num1>=num2 and num1+1<=n]
	combi1=[")"+e for e in createP(n,num1,num2+1) if num1-1>=num2 and num2+1<=n]

	print combi1,combi2
	return combi1+combi2


print createP(4,0,0)
"""

"""
def permutation(words,poss):
	print words,poss
	list1=[]
	for i in words:
		for j in poss:
			list1.append(j+i)
	return list1

def potential_letters(l):
	if l==2: return ["a","b","c"]
	if l==3: return ["d","e","f"]
	if l==4: return ["g","h","i"]
	if l==5: return ["j","k","l"]
	if l==6: return ["m","n","o"]
	if l==7: return ["p","q","r","s"]
	if l==8: return ["t","u","v"]
	if l==9: return ["w","x","y","z"]

def find_translated_words(word,num):
	if num>=len(word): return [""]
	combin=find_translated_words(word,num+1)
	possible=potential_letters(int(word[num]))
	return permutation(combin,possible)

print find_translated_words(str(23),0)
"""
"""
import queue 

def FindPath(Nodes,start,end):
	Q=Queue.Queue()
	for i in Nodes:
		i.visted=False
	start.visited=True
	Q.put(i)
	while not Q.empty():
		run=Q.get()
		#do something with it
		for i in run.adjacent:
			if i!=None and i.visted=False:
				if i==end: return True
				i.visited=True
				Q.put(i)

	return False

class Node:

	def __init__(self,ln=None,rn=None):
		self.Value=0
		self.leftNode=ln
		self.rightNode=rn

def MinimlaTree(Arr):
	if len(Arr)==0 return None
	mid=len(Arr)/2
	return Node(Arr[mid],MinimlaTree(Arr[0:mid]),MinimlaTree(Arr[mid+1:]))

import heapq
import os
f=file('input01.txt','r')
fw=file('output.txt','w')
n = int(f.readline().strip())
print n
#a = map(int, raw_input().strip().split(' '))h=[]
h=[]
for i in range(n):
    a = int(f.readline().strip())
    heapq.heappush(h,a)
    if (i+1)%2!=0:
        fw.write(str(round(h[int(len(h)/2)],2))+os.linesep)
    else:
        fw.write(str(round(float(h[int(len(h)/2)]+h[int((len(h)-1)/2.0)])/2,2))+os.linesep)



class LinkListN:
	def__init__(self,Node):
		self.Node =Node
		self.next=Node 

def AddToLinkedList(LNKL,N,depth):
	if len(LNKL)==depth:
		LNKL=LNKL.append(LinkListN(N))
	else:
		N.next=LNKL[depth]
		LNKL[depth]=N

def BDS(Node):
	q=Queue.Queue()
	Node.marked=True
	Node.depth=0
	q.put(Node)

	LinkedList=[Node]
	while not q.empty():
		vi=q.get()
		#do something
		for i in [vi.left,vi.right]:
			if i!=None and i.marked!=True:
				i.marked=True
				i.depth=vi.depth+1
				q.put(i)
				AddToLinkedList(LinkedList,i,i.depth)

a=1745
print "{0:b}".format(a)
list1=[]
tmp=a
i=0
count=int()
while a>>i:
	if a>>i & 1: 
		count+=1
	else:
		if count:
			list1.append(count)
		list1.append(0)
		count=0
	i+=1

if count:
	list1.append(count)


print max([list1[i]+list1[i+2] for i in xrange(0,len(list1)-2)])+1
print list1



def CalcSteps(n,ls):
	if n in [1,2,3]: return ls[n-1]
	if ls[n-1]!=0: 
		return ls[n-1]
	else:
		ls[n-1]+=CalcSteps(n-1,ls)+CalcSteps(n-2,ls)+CalcSteps(n-3,ls)
	return ls[n-1]

n=6
ls=[0]*n
ls[0:3]=[1,2,4]
print ls
print CalcSteps(n,ls)
print ls


Mat=[[0,0,-1,0,0]
	,[0,-1,-1,0,0]
	,[0,0,0,0,0]
	,[0,0,-1,0,0]
	,[0,0,0,0,0]]	

def FindPath(Mat,i,j,N):
	bad=True
	if i>=N or j>=N: return False
	if i==N-1 and j==N-1: return True
	if i+1<N and Mat[i+1][j]!=-1:
		bad=bad and FindPath(Mat,i+1,j,N)
	if j+1<N and Mat[i][j+1]!=-1:
		bad=bad and FindPath(Mat,i,j+1,N)
	if (Mat[i][j+1]==-1 and Mat[i+1][j]==-1) or (Mat[i][j+1]==-1 and i==N-1) or (Mat[i+1][j]==-1 and j==N-1):
		Mat[i][j]=-1
		return False

	print Mat
	return True

print Mat
N=4
FindPath(Mat,0,0,N)
#FindPath(Mat,0,0,4)
#FindPath(Mat,0,0,4)
print Mat

x,y=0,0
path=[]
while x+y<2*N-1:
	path.append([x,y])
	if x<=N-1 and Mat[x+1][y]!=-1:
		x+=1
		continue
	if y<=N-1 and Mat[x][y+1]!=-1:
		y+=1
		continue
print path

"""
"""
x=set([4,5,7,8])

def SetCombi(s):
	if len(s)==0 or s==None: return [[]]
	e=s.pop()
	without_x=SetCombi(s)
	el=[[e]+combi for combi in without_x]
	el.extend(without_x)
	return el 

print SetCombi(x)
"""
"""
def CreateP(n,x,y):
	print n,x,y
	if n==0: return [""]
	if x==n and y==n: return [""]
	left,right=[],[]
	if x>=y and x+1<=n:
		left =["(" + i for i in CreateP(n,x+1,y)]
	if x>=y+1 and y+1<=n:
		right=[")" + i for i in CreateP(n,x,y+1)]

	return left+right


print CreateP(4,0,0)
"""
"""
import itertools
def Recrusive(n1,n2):
	larger=lambda x,y: [x,y] if x>y else [y,x] 
	big,small=larger(n1,n2)
	if small==0 or big ==0: return 0
	if small==1: return big
	h_max=small>>1
	res=Recrusive(h_max,big)
	if h_max+h_max==small:
		return res+res
	else:
		return res+res+big


print Recrusive(11,7)

def permutations(string):
	if len(string)==0: return [""]
	lsp=[]
	for i in range(0,len(string)):
		lsp.extend([string[i]+j for j in permutations(string[0:i]+string[i+1:])])
	return lsp

name="Yazeee"

print len(permutations(name))
print len([i for i in itertools.permutations(name,6)])

def perm_with_dubs(string,edic):
	if len(string)==0: return [""]
	dic={}
	for i in range(0,len(string)):
		tmp=[]
		tmps=''.join(sorted(string[0:i]+string[i+1:]))
		if edic.get(tmps)==None:
			tmp=perm_with_dubs(string[0:i]+string[i+1:],edic)
			edic[tmps]=tmp
		else:
			print "OPT"
			tmp=edic[tmps]

		for j in tmp:
			if dic.get(string[i]+j)==None:
				dic[string[i]+j]=1
	return dic

edic={}
print len(perm_with_dubs(name,edic))
print edic
"""
"""
def MergeArrays(A,B,a,b):
	lenCombinedAB=a+b
	ABrun=a+b-1
	Arun=a-1
	Brun=b-1
	for i in range(a+b-1,-1,-1):
		print A,i,Arun,A[Arun],Brun,B[Brun],A[i]
		if Arun>=0 and Brun>=0:
			if A[Arun]>=B[Brun]:
				A[i]=A[Arun]	
				Arun-=1
			else:
				A[i]=B[Brun]
				Brun-=1
		else: 
			if Arun>=0 and Brun<0:
				A[i]=A[Arun]
				Arun-=1
			elif Arun<0 and Brun>=0:
				A[i]=B[Brun]
				Brun-=1
	return A

A=range(6,21)
A.extend([0 for x in range(30)])
B=range(20,28)
print A
print B

print MergeArrays(A,B,15,len(B))
"""
"""
def shift(l, n):
	return l[n:] + l[:n]

x=range(4,30)
print x
x.extend([y for y in range(6,10)])
x.extend([y for y in range(6,10)])
x.extend([y for y in range(6,10)])

x.sort()
print x
x=shift(x,26)

def BinS(A,start,end,e):

	while start<=end:
		mid=(start+end)/2
		if A[mid]>A[end]:
			if A[mid]>e>=A[start]:
				end=mid-1
			elif A[mid]==e:
				return mid
			else:
				start=mid+1
		else:
			if A[end]>=e>A[mid]:
				start=mid+1
			elif A[mid]==e:
				return mid
			else:
				end=mid-1
	return -1
print x	
e=14
print BinS(x,0,len(x)-1,e),x.index(e)


"""
"""
a=[1,2,3,7,5]
a=[1,100]
t=100
left=0
right=0
curr_sum=0
n=len(a)
while right<n and left<n:
    curr_sum=sum(a[left:right+1])
    if curr_sum<t:
        right+=1
    elif curr_sum>t:
        left+=1
    else:
        return left+1,right+1
        break
return -1
"""
"""

def CalcNonZero(A):
	left=0
	right=0
	n=len(A)
	while left<n and right<n:
		if A[left]!=0:
			left+=1
			right=left
		elif A[right]==0:
			right+=1
		else:
			A[left],A[right]=A[right],A[left]
	print left,A

CalcNonZero([1,0,2,3,0,0,4,0])
"""
"""
def FindS(A,t):
	if t>0 and len(A)>0:
		combi_without_x = FindS(A[0:len(A)-1],t)
		combi_with_x = [[A[-1]]+comb for comb in FindS(A,t-A[-1])]
		return combi_without_x + combi_with_x
	else:
		if t==0:
			return [[]]
		else:
			return []

A=[]
x=1
num=13
while x**2 < num:
	A.append(x**2)
	x+=1

print min(FindS(A,num),key=len)
"""

"""
def CountStart(n,num):
    pow_n=1
    counter=0
    while n>=(num+1)*pow_n:
        counter+=pow_n
        pow_n*=10
    if (num+1)*pow_n>n>=num*pow_n:
    	counter+=n-num*pow_n+1
    return counter

1,10,100,101...104,11,110,111,
count=0
i=1
n=160
k=70
while k>count and count<160:
	count+=CountStart(n,i)
	i+=1


print i,count
"""
n=6
for i in range(1,n+1):
	print " "*(n-i) +"#"*i

