# 시간 복잡도: 길이가 최대 5인 모든 단어 조합 5^5 -> O(5^5) -> O(3125) -> O(1) 상수 시간.
# 공간 복잡도: recursionError 피하기 위해서 sys.setrecursionlimit(10000)로 일단 늘리고 시작하기


# 접근법
# 1. 재귀니까 점화식으로 나타낼 수 있을 것
# (접근법 못 찾아서 해설지 봄)

import sys
sys.setrecursionlimit(10000)

# find 함수 -> 재귀적으로 모든 가능한 단어를 생성하여, dict 리스트에 추가
def find(dict, now, idx):    # 생성된 단어들을 저장하는 리스트, 현재 생성된 문자열, 현재 문자열의 길이
    vowels = ['A', 'E', 'I', 'O', 'U']  # 사용할 알파벳 모음
    
    if idx == 6: return     # 종료 조건 명시: 최대 5글자만 가능하므로, 6이 되면 탐색 종료
    if now != '': dict.append(now)   # 현재 생성된 문자열이 비어있지 않다면 리스트에 추가 (빈 문자열은 사전에 포함되지 않기 때문에 제외)
    for i in vowels:    # 모음 순서대로 새로운 문자 추가
        find(dict, ''.join([now, i]), idx+1)    # idx는 현재 문자열의 길이를 나타내기 때문에, 새로운 문자열이 생성될 때마다 1씩 길이 증가시킴
    
    
# solution 함수 -> 주어진 단어가 몇 번째인지 찾는 함수    
def solution(word):
    answer = 0  # 단어의 위치를 저장할 변수
    dict = []   # 모든 가능한 단어 조합을 저장할 리스트
    find(dict, '', 0)   # 재귀적으로 모든 단어 조합을 생성 # 빈 문자열부터 시작하여 길이가 0인 상태로 모든 조합을 생성
    for j in range(len(dict)):  # 생성된 모든 단어를 순회하며
        if dict[j] == word:     # 주어진 단어와 일치하는 단어를 찾으면
            answer = j + 1      # 단어의 위치를 기록 (인덱스는 0부터 시작하므로 1을 더해야 실제 몇 번째 단어인지 알 수 있음)
            break               # 단어 찾았으면 탐색 종료
    
    return answer