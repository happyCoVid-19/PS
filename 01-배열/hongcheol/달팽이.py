def solution(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]#2차원배열
    y, x = -1, 0
    count = 1
    
    for i in range(n):
        for j in range(i, n):
            if(i % 3 == 0):   #아래로
                y += 1
            elif(i % 3 == 1):  #오른쪽으로
                x += 1
            else:  
                y -= 1 #대각선으로 올렷
                x -= 1
            matrix[y][x] = count
            count += 1

    answer = []
    for i in range(n):
        for j in range(n):
            if(matrix[i][j]!=0):
                answer.append(matrix[i][j])
    
    return answer
