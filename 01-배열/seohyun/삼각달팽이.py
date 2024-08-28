n = int(input())

answerdic = []
for i in range(n):
    answerdic.append([])

sum = int(n*(n+1)/2)
row = 0
y = 0
i = 1
while i <= sum:
    if row == 0:
        if len(answerdic)>y and len(answerdic[y])<y+1:
            answerdic[y].append(i)
            y += 1
            i += 1
        else:
            row = 1
            y -= 1
    
    elif row == 1:
        if len(answerdic[y])<y+1:
            answerdic[y].append(i)
            i += 1
        else:
            row = 2
            y -= 1
    
    elif row == 2:
        if len(answerdic[y])<y+1:
            answerdic[y].append(i)
            y -= 1
            i += 1
        else:
            row = 0
            y += 2
    
print(answerdic)
# answer = []