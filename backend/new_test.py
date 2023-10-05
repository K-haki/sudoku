#全局变量记录空位置（使用回溯法）
indexList = []

#储存数独元素
sudoku = [[7, 5, 0, 8, 0, 6, 0, 0, 3], 
          [1, 0, 0, 2, 0, 0, 0, 7, 0], 
          [6, 0, 0, 0, 0, 7, 0, 0, 5], 
          [0, 0, 0, 0, 6, 0, 0, 8, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 1], 
          [0, 9, 0, 0, 0, 0, 0, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 7], 
          [5, 0, 0, 0, 0, 0, 0, 0, 2], 
          [0, 0, 0, 0, 0, 0, 0, 1, 4]]

# --- 程序入口 --- #
def main():
    #寻找首个空元素
    firstEmpty()
    #寻找末尾空元素
    last = lastEmpty()
    m,n = last
    #当末尾空元素合法且不等于0时停止循环
    while oneIsLegal(m,n) != True or sudoku[m][n] == 0:
        #获取栈顶元素
        x,y = indexList[-1]
        #判断当前位置是否合法
        if isLegal() == True and sudoku[x][y] <= 9 and 0 < sudoku[x][y]:
            #寻找下一个空元素
            isEmpty()
        else:
            #不合法 - 回退
            if sudoku[x][y] >= 9:
                myReturn()
                myAdd()
            else: #不合法 - 自增
                myAdd()
    myOutput()

# --- 寻找第一个空元素位置 --- #
def firstEmpty():
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0: #'0'
                myPush([i,j])
                return

# --- 寻找最后一个空元素位置 --- #
def lastEmpty():
    for i in range(8,-1,-1):
        for j in range(8,-1,-1):
            if sudoku[i][j] == 0: #'0'
                return [i,j]

# --- 位置判空加入栈中 --- #
def isEmpty():
    #获取栈顶元素
    a,b = indexList[-1]
    #从下一元素开始找起
    b += 1
    for i in range(a,9):
        if i != a:
            b = 0
        for j in range(b,9):
            if sudoku[i][j] == 0: #'0'
                myPush([i,j])
                return

# --- 入栈 --- #
def myPush(coordinate):
    indexList.append(coordinate)

# --- 出栈 --- #
def myPop():
    indexList.pop()

# --- 当前位置自增 ---#
def myAdd():
    #获取栈顶元素
    x,y = indexList[-1]
    sudoku[x][y] += 1

# --- 判断当前位置是否合法 --- #
def isLegal():
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
def oneIsLegal(x,y):
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
def myReturn():
    #获取栈顶元素
    x,y = indexList[-1]
    sudoku[x][y] = 0
    myPop()

# --- 输出数独 --- #
def myOutput():
    print("答案为：")
    for i in range(9):
        print(sudoku[i])

if __name__ == "__main__":
    main()
