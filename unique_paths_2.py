import collections 

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        obstacleGridPath = [[0 for j in i] for i in obstacleGrid]
        obstacleGridPath[0][0] = 1

        if len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
        	return 0

        m,n = len(obstacleGrid) , len(obstacleGrid[0])
        print obstacleGridPath

        def BFS(obstacleGrid,obstacleGridPath,x,y):
        	q = collections.deque()
        	q.append([x,y])

        	while len(q):
        		p = q.popleft()
        		if p[0] + 1 < m and obstacleGrid[p[0]+1][p[1]] == 0:
        			if obstacleGridPath[p[0] + 1][p[1]] == 0:
        				q.append([p[0] + 1,p[1]])
        			obstacleGridPath[p[0] + 1][p[1]] += obstacleGridPath[p[0]][p[1]]


        		if p[1] + 1 < n and  obstacleGrid[p[0]][p[1] + 1] == 0:
        			if obstacleGridPath[p[0]][p[1] + 1] == 0:
        				q.append([p[0],p[1] + 1])
        			obstacleGridPath[p[0]][p[1] + 1] += obstacleGridPath[p[0]][p[1]]


        BFS(obstacleGrid,obstacleGridPath,0,0)
        print obstacleGridPath[-1][-1]

M = [
  [0,1,0],
  [0,0,0],
  [0,0,0]
]

x = Solution()
x.uniquePathsWithObstacles(M)

