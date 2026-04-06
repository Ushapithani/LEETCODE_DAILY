class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple,obstacles))
        directions =['N','E','S','W']
        moves ={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
        x,y,d,ans = 0,0 ,0,0
        for c in commands:
            if c==-1:
                d=(d+1)%4
            elif c==-2:
                d=(d-1)%4
            else:
                dx,dy=moves[directions[d]]
                for i in range(c):
                    nx,ny=x+dx,y+dy
                    if (nx,ny) in obs:
                        break
                    x,y=nx,ny
                    ans = max(ans,x*x+y*y)
        return ans
