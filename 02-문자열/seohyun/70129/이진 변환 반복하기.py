def solution(s):
    strs = s
    
    change = 0
    zerocount = 0
    
    while strs != '1':
        change += 1
        zerocount += strs.count('0')
        strs = strs.replace('0', '')

        strs = bin(len(strs))[2:]
            
    return [change, zerocount]