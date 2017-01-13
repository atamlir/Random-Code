import re
s = "++-++++-++---+"
x = map(len,re.split('-+',s))

def FMN(ls):
	ls_set = set(ls)
	for i in xrange(len(ls)):
		if i not in ls_set: return i
	return len(ls)

g = [0] * (max(x) + 1)
for i in xrange(2,max(x)+1):
	list_of_xors = set([g[a]^g[i - a - 2] for a in range(i/2)])
	g[i] = FMN(list(list_of_xors))
	print g[i],i
print g,x
print bool(reduce(lambda a,b: a^b,[g[k] for k in x]))