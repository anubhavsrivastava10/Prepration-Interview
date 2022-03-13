t = int(input())
while t:
    t-=1
    n,x = map(int,input().split())
    if x%3==0:
        ans = x//3
        if ans<=n:
            print("Yes")
            print(ans,0,n-ans)
        else:
            print("No")
    else:
        ans = x//3
        ans += 1
        if ans >= n:
            print("No")
        else:
            check = (ans*3)-x
            # print(check, ans)
            if check <= n-ans:
                print("Yes")
                print(ans,check,n-ans-check)
            else:
                print("No")