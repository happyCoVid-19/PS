# 코드의 전체 흐름
# 1. 집합의 원소들을 길이순으로 정렬한다.
# 2. 차집합으로 어떤 원소가 새롭게 추가됐는지 확인한다. (튜플 원소의 순서 확인)
# 3. 원래 표현하는 튜플을 배열에 담아 return


def solution(s):
    
    # 가장 바깥쪽의 중괄호 제거
    s = s[2:-2]
    
    # s의 각 원소(문자열)을 집합(set)으로 변환
    s = s.split("},{")
    new_s = []
    
    for i in s:
        bundle = set(map(int, i.split(',')))
        new_s.append(bundle)
    
    # 집합들 길이순 정렬
    new_s.sort(key=len)
    
    # 차집합 연산으로 어떤 원소가 순서대로 추가됐는지 확인
    answer = []
    
    ## 첫 번째 집합의 첫 번째 원소 추가
    answer.append(list(new_s[0])[0])
    
    for j in range(len(new_s)-1):
        new = list((new_s[j+1] - new_s[j]))[0]
        answer.append(new)
    
    return answer