grid=[
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def possible(x,y,n):
    for i in range(0,9):
        if grid[i][x]==n and i !=y:
            return False

    for i in range(0,9):
        if grid[i][y]==n and i!=x:
            return False

    x0 =(x // 3) * 3
    y0=(y //3)*3
    for x in range(x0,x0+3):
        for y in range(y0,y0+3):
            if grid[x][y]== n:
                return False
    return True

def solve():
    global grid
    for y in range(0,9):
        for x in range(0,9):
            if grid[x][y]==0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return
    print(grid)
    input("More?")

def print(matrix):
    for i in range(9):
        print(matrix[i])

