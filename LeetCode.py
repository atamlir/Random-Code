#76. Minimum Window Substring

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        min_length=[0, 2 * len(s)]
        
        if len(t) == 0 or len(s) == 0 or len(t) > len(s): 
            return ""
            
        l ,r ,d ,df = 0 , 0, {}, {}
        se={}
        for i in t:
            d[i] = 0
            df[i] = (1 if i not in df else df[i]+1)
            se[i] = (1 if i not in se else se[i]+1)
            
        while l<len(s) and (s[l] not in d):
            l+=1
            r=l
            
        while r<len(s):
            if s[r] not in d:
                r+=1
            else:
                if s[r] in se:
                    se[s[r]] -= 1
                    if se[s[r]] == 0:
                        del se[s[r]]
                    
                d[s[r]]+=1
                r+=1
                while d[s[l]] > df[s[l]]:
                    d[s[l]]-=1
                    l+=1
                    while s[l] not in d:
                        l+=1
                if len(se) == 0 and r-l < min_length[1]-min_length[0] :
                    min_length=[l,r]
                    
        if len(se) != 0:
            return ""
        else:
            return s[min_length[0]:min_length[1]]
                    

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i=0
    s=[]
    res=0
    while (i<len(height)):
        if len(s)==0 or height[s[-1]]> height[i]:
            s.append(i)
            i+=1
        else:
            r=0
            e=0
            print(s,i,height[s[-1]],height[i])
            while len(s)>0 and height[s[-1]]<=height[i]:
                e=s.pop()
                r=max(r,height[e])
            v=(height[e] if len(s)==0 else height[s[-1]])
            res+=(min(v,height[i])-r)*(i-e+1)
    
    return res

print trap([0,1,0,2,1,0,1,3,2,1,2,1])