def hanoi(n, answer, start, end):
    mid = 0
    if start+end == 3:
        mid = 3
    elif start+end == 4:
        mid = 2
    elif start+end == 5:
        mid = 1
        
    if n == 2:
        answer.append([start,mid])
        answer.append([start,end])
        answer.append([mid,end])
        return
    else:
        hanoi(n-1, answer, start, mid)
        answer.append([start,end])
        hanoi(n-1, answer, mid, end)
        return

def solution(n):
    answer = []
    hanoi(n, answer, 1, 3)
    return answer