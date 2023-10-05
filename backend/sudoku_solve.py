board = [[7, 5, 0, 8, 0, 6, 0, 0, 3], 
          [1, 0, 0, 2, 0, 0, 0, 7, 0], 
          [6, 0, 0, 0, 0, 7, 0, 0, 5], 
          [0, 0, 0, 0, 6, 0, 0, 8, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 1], 
          [0, 9, 0, 0, 0, 0, 0, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 7], 
          [5, 0, 0, 0, 0, 0, 0, 0, 2], 
          [0, 0, 0, 0, 0, 0, 0, 1, 4]]

# --- 程序入口 --- #
def main(board):
    sudoku = board
    indexList = []
    # print(board)
    #寻找首个空元素
    firstEmpty(sudoku, indexList)
    #寻找末尾空元素
    last = lastEmpty(sudoku)
    m,n = last
    #当末尾空元素合法且不等于0时停止循环
    while oneIsLegal(m,n,sudoku) != True or sudoku[m][n] == 0:
        #获取栈顶元素
        x,y = indexList[-1]
        #判断当前位置是否合法
        if isLegal(sudoku, indexList) == True and sudoku[x][y] <= 9 and 0 < sudoku[x][y]:
            #寻找下一个空元素
            isEmpty(sudoku, indexList)
        else:
            #不合法 - 回退
            if sudoku[x][y] >= 9:
                myReturn(sudoku, indexList)
                myAdd(sudoku, indexList)
            else: #不合法 - 自增
                myAdd(sudoku, indexList)
    # myOutput(sudoku)
    return sudoku
    

# --- 寻找第一个空元素位置 --- #
def firstEmpty(sudoku, indexList):
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0: #'0'
                myPush([i,j], indexList)
                return

# --- 寻找最后一个空元素位置 --- #
def lastEmpty(sudoku):
    for i in range(8,-1,-1):
        for j in range(8,-1,-1):
            if sudoku[i][j] == 0: #'0'
                return [i,j]

# --- 位置判空加入栈中 --- #
def isEmpty(sudoku, indexList):
    #获取栈顶元素
    a,b = indexList[-1]
    #从下一元素开始找起
    b += 1
    for i in range(a,9):
        if i != a:
            b = 0
        for j in range(b,9):
            if sudoku[i][j] == 0: #'0'
                myPush([i,j], indexList)
                return

# --- 入栈 --- #
def myPush(coordinate, indexList):
    indexList.append(coordinate)

# --- 出栈 --- #
def myPop(indexList):
    indexList.pop()

# --- 当前位置自增 ---#
def myAdd(sudoku, indexList):
    #获取栈顶元素
    x,y = indexList[-1]
    sudoku[x][y] += 1

# --- 判断当前位置是否合法 --- #
def isLegal(sudoku, indexList):
    #获取栈顶元素
    x,y = indexList[-1]
    temp = sudoku[x][y]
    #判断该行是否重复
    for i in range(9):
        if sudoku[x][i] == temp and i != y:
            return False; #当前位置不合法
    #判断该列是否重复
    for i in range(9): 
        if sudoku[i][y] == temp and i != x:
            return False; #当前位置不合法
    #判断该宫是否重复
    xx = int(x / 3)
    yy = int(y / 3)
    for i in range(3):
        for j in range(3):
            if sudoku[xx * 3 + i][yy * 3 + j] == temp and (xx * 3 + i) != x and (yy * 3 + j) != y:
                return False; #当前位置不合法
    return True #当前位置合法
    
# --- 判断某一位置是否合法 --- #
def oneIsLegal(x,y,sudoku):
    temp = sudoku[x][y]
    #判断该行是否重复
    for i in range(9):
        if sudoku[x][i] == temp and i != y:
            return False; #当前位置不合法
    #判断该列是否重复
    for i in range(9): 
        if sudoku[i][y] == temp and i != x:
            return False; #当前位置不合法
    #判断该宫是否重复
    xx = int(x / 3)
    yy = int(y / 3)
    for i in range(3):
        for j in range(3):
            if sudoku[xx * 3 + i][yy * 3 + j] == temp and (xx * 3 + i) != x and (yy * 3 + j) != y:
                return False; #当前位置不合法
    return True #当前位置合法

# --- 回退函数 --- #
def myReturn(sudoku, indexList):
    #获取栈顶元素
    x,y = indexList[-1]
    sudoku[x][y] = 0
    myPop(indexList)

# --- 输出数独 --- #
def myOutput(sudoku):
    print("答案为：")
    for i in range(9):
        print(sudoku[i])

if __name__ == "__main__":
    main(board)