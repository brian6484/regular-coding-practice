n=int(input())
k=int(input())
data = [[0]* (n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a,b=map(int,input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def turn(direction,c):
    if c=='L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def simulate():
    x,y=1,1
    daata[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x,y)]
    while True:
        nx = x+dx[direction]
        ny = y +dy[direction]
        if 1<=nx and nx <=