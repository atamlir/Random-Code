
#problem 10.1
"""
import math
def find_index(num,lis):
	L=0
	R=len(lis)-1
	while L<=R:
		mid=((L+R)/2)
		print mid
		if lis[mid]==num:
			return -1
		elif lis[mid]>num:
			R=mid-1
		else:
			L=mid+1
	return mid
A=[1,3,4,5,7,9,11]
B=[-1,0,2,6,12,14]

for i in B:
	index=find_index(i,A)
	if index!=-1:
		if A[index]>i:
			A.insert(index,i)
		else:
			A.insert(index+1,i)
	print A
"""

"""
A=[1,3,4,5,7,9,11,0,0,0,0,0,0,0,0,0]
B=[-1,0,2,6,12,14]
def merge(A,B,lastA,lastB):
	lenA=lastA
	lenB=lastB
	lenAB=lastA+lastB+1

	while lenB>=0:
		max1=max(A[lastA],B[lastB])
		print lenA,lenB,A
		if A[lenA]>B[lenB] and lenA>=0:
			A[lenAB]=A[lenA]
			lenA-=1
		else:
			A[lenAB]=B[lenB]
			lenB-=1
		lenAB-=1

merge(A,B,6,5)
print A

import time
import math
import itertools
start_time = time.time()
def permut(str1):
	if len(str1)==0: return ""
	if len(str1)==1: return str1
	res=permut(str1[0:len(str1)-1])
	tmp_list=[]
	for i in res:
		print res
		for j in range(0,len(str1)):
			tmp=i[0:j]+str1[-1]+i[j:]
			print tmp
			tmp_list.append(tmp)
	return tmp_list

print set(permut("Granny"))
print("--- %s seconds ---" % (time.time() - start_time))
"""
"""
import math
dic={}
string="Tact Ca".lower()
for i in string:
	if dic.get(i)==None:
		dic[i]=1
	else: 
		dic[i]+=1

allowed_1=(len(string)-string.count(' '))%2==1
for i in dic:
	if i==' ' and dic[i]!=string.count(' '):
		print string,dic[i],"1False",string.count(' ')
		break
	elif i!=' ' and dic[i]%2==1 and dic[i]!=1:
		print string,dic[i],"2False"
		break
	elif i!=' ' and dic[i]==1:
		if not allowed_1: 
			print string,dic[i],"3False"
			break

print dic
"""
"""
def OneWay(str1,str2):
	if str1==str2: return True
	if abs(len(str1)-len(str2))>1: return False
	num_matches=max(len(str1),len(str2))-1
	dic={}
	for s in str1:
		if dic.get(s)==None:
			dic[s]=1
		else:
			dic[s]+=1

	for s in str2:
		if dic.get(s)!=None:
			num_matches-=1
			dic[s]-=1
			if dic[s]<0: return False

	if num_matches==0:
		return True
	return False
print OneWay("aaa","aaaa")
"""
"""
def compression(str1):
	if len(str1)==0: return ''
	i=0
	while i+1<len(str1) and str1[i]==str1[i+1]:
		i+=1
	return str1[i]+str(i+1)+ compression(str1[i+1:])

print len(compression("aabcccccaaa")),len("aabcccccaaa"),compression("aabcccccaaa")
"""
import operator
N=3
matrix=[[1,2,0],[4,3,6],[7,8,9]]
#print [[matrix[N-i-1][j] for i in range(0,N)] for j in range(0,N)]

def ElemInMat(mat,i,j):
	if j>=N or i>=N: return -1
	return reduce(operator.mul,[matrix[i][l] for l in range(0,N)])*reduce(operator.mul,[matrix[l][j] for l in range(0,N)])

print ElemInMat(matrix,2,0)
