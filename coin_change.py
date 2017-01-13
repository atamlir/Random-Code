import collections

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def BFS(coins,amount):
            range_set = set()
            
            q = collections.deque()
            for i in coins:
                q.append(i)
            while q:
                print range_set,len(q),len(range_set)
                p = q.popleft()
                range_set.add(p)
                for i in coins: 
                    if i + p <= amount and i+p not in range_set:
                        q.append(i+p)
            return range_set
        
        m_coins = min(coins)
        d = {}
        for i in coins:
            d[i] = 1
        
        coins_dic = collections.OrderedDict({m_coins : 1})
        ls = BFS(coins,amount)
        print ls
        
        for i in ls:
            if i in d:
                coins_dic[i] = d[i]
            else:
                for x in coins_dic:
                    if x > i/2:
                        break
                    if x in coins_dic and i-x in coins_dic:
                        if i in coins_dic:
                            coins_dic[i] = min(coins_dic[i],coins_dic[x] + coins_dic[i-x])
                        else:
                            coins_dic[i] = coins_dic[x] + coins_dic[i-x]
        #print coins_dic
        return coins_dic.get(amount,-1)


x = Solution()
print x.coinChange([186,419,83,408],6249)