t = int(input())
while t:
    t-=1
    s = input()
    count = 0
    m  = -1
    for i in range(len(s)):
        if s[i]!=s[0]:
            if s[i]!=s[-1]:
                count+=1
        else:
            count = 0
        m = max(count,m)
    if m==0:
        print(-1)
    else:
        print(m)