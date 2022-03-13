t = int(input())
while t:
    t-=1
    a = input()
    b = input()
    ans = ""
    for i in range(len(a)):
        if a[i]==b[i]:
            ans += "G"
        else:
            ans += "B"
    print(ans)