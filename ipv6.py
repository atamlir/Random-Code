import re

def from_shot_to_long_ipv6(s):

	if "::" in s:
		s = s.replace("::",(9 - s.count(':')) * ':')

	t = s.split(':')

	t = ':'.join(['0' * (4 - len(i)) + i for i in t])

	print(t)


def DecodeString(s):
	while '[' in s:
		s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2),s)
		print(s)

s = ["1080::8:800:200C:417A", "1454:45::4140:141:55:ABBB", "2340::0455:0000:AAAB:1121", "::1:AAAA:BBBC:A222:BBBA:1"]

for i in s:
	from_shot_to_long_ipv6(i)

DecodeString("3[a2[c2[f]as4[df]]]")
import functools

@functools.lru_cache(maxsize=None)
def lexicalOrder(n):
    """
    :type n: int
    :rtype: List[int]
    """
    
    ls = []
    
    def DFS(i,n,ls):
        #print(i)
        if i > n:
            return 
        ls.append(i)
        for j in range(10*i,min(10*i+10,n+1)):
            DFS(j,n,ls)
            
    for i in range(1,10):
        DFS(i,n,ls)
    return ls

lexicalOrder(4999)
