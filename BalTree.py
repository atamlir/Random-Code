

class Node:

	def __init__(self,val):
		Value=val
		Left=None
		Right=None


def InorderPass(Node,Arr):
	if Node!=None:
		InorderPass(Node.Left,Arr)
		Arr.append(Node)
		InorderPass(Node.Right,Arr)
	return Arr

def ArrayToTree(Arr,start,end):
	if len(Arr)==0 or start>=end:
		return None

	mid=(start+end)/2
	No=Node(Arr[mid])
	No.Left= ArrayToTree(Arr, start, mid)
	No.Right=ArrayToTree(Arr, mid + 1, end)
	return No

ls1=InorderPass(T1,[])
ls2=InorderPass(T2,[])
ls3=[]
ptr1=0
ptr2=0

while ptr1<len(ls1) or ptr2<len(ls2):
	if ls1[ptr1]<ls2[ptr2]:
		ptr1+=1
	elif ls1[ptr1]>ls2[ptr2]:
		ptr2+=1
	else:
		ls3.append(ls1[ptr1])
		ptr1+=1
		ptr2+=1


print ArrayToTree(ls3,0,len(ls3))



ArrayToTree(range(5),2)
1,2,3,4,5]

