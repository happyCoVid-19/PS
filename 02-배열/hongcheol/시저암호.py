def solution(s, n):
    #answer = ''
    answer=[]
    for i in range (0,len(s)):
        temp=ord(s[i])
        if(s[i]!=' '):
            if('a'<=chr(temp)<='z') and (chr(temp+n)>'z'):
                #print(chr(temp+n-1-ord('z')+ord('a')))
                answer.append(chr(temp+n-1-ord('z')+ord('a')))
            elif('a'<=chr(temp)<='z') and (chr(temp+n)<='z'):
                #print(chr(temp+n))
                answer.append(chr(temp+n))
            elif('A'<=chr(temp)<='Z') and (chr(temp+n)>'Z'):
                #print(chr(temp+n-1-ord('Z')+ord('A')))
                answer.append(chr(temp+n-1-ord('Z')+ord('A')))
            else:
                #print(chr(temp+n))
                answer.append(chr(temp+n))
        else:
            answer.append(s[i])
        #print(ord(s[i]))
    answer="".join(answer)
    return answer
