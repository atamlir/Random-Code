class Node:
	def __init__(self,val,right,left):
		self.v=val
		self.right=right
		self.left=left

class Node1:
	def __init__(self,val):
		self.v=val
		self.right=None
		self.left=None

def ConsructTree(A,index):
	if len(A)==0:
		return None
	root=Node1(A[index].v)
	ind=index+1
	if A[index].left==1:
		root.left,ind=ConsructTree(A,ind)
	if A[index].right==1:
		root.right,ind=ConsructTree(A,ind)
	print root.v,ind
	return root,ind

def postorder(T):
	Arr=[]
	if T!=None:
		Arr.extend(postorder(T.left))
		Arr.extend(postorder(T.right))
		print T.v
		Arr.append(T.v)
		return Arr
	return []


ls=[Node(3,1,1),Node(1,1,1),Node(0,0,0),Node(2,0,0),Node(5,1,0),Node(4,0,0)]
T,ind=ConsructTree(ls,0)
postorder(T)

ls =[1,2,3,4,5,6,7]
ls1=[3,5,3]
least=324232323
dis=0
s_index=0
for i in range(0,len(ls)-len(ls1)+1):
	dis=0
	for j in range(0,len(ls1)):
		dis+=abs(ls1[j]-ls[i+j])
	if dis<least:
		least=dis
		s_index =i

print least,s_index


def combinations(ls,num,pos=0):
	if pos>=len(ls) and num>0: return []
	if num!=0:
		with_x =[[ls[pos]] + combi for combi in combinations(ls,num-1,pos+1)]
		without_x =combinations(ls,num,pos+1)
	else:
		return [[]]
	return with_x+without_x

ls=["yaz","ma7","ena","pep","bunn","sed","sa7","wal"]
print combinations(ls,4)


		