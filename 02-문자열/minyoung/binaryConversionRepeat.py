def solution(s):
    zero_count = 0
    bin_count = 0
    
    while s != '1':
        # 0 개수를 세고, 문자열의 0을 전부 제거
        zero_count += s.count('0')
        s = s.replace('0', '')
    
        # 문자열의 길이를 구하고, 2진법으로 변환
        s = bin(len(s))[2:] #0b100 
        bin_count += 1
        
    
    return [bin_count, zero_count]