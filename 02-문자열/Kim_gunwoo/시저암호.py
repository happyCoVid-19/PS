def solution(s, n):
    answer = []

    for i in s:
        if i == ' ':
            answer.append(' ')
            continue
        
        oi = ord(i)
        if 65 <= oi <= 90:
            oi += n
            if oi > 90: oi = 65 + (oi - 90 - 1)
        
        if 97 <= oi <= 122:
            oi += n
            if oi > 122: oi = 97 + (oi - 122 - 1)
        
        answer.append(chr(oi))
        
    return ''.join(answer)