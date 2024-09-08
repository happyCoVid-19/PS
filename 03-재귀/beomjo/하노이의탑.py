def hanoi(start, mid, end, answer, n):
    if n == 1:
        answer.append([start, end])
        return
    hanoi(start, end, mid, answer, n-1)
    answer.append([start, end])
    hanoi(mid, start, end, answer, n-1)
def solution(n):
    answer = []
    hanoi(1, 2, 3, answer, n)
    return answer