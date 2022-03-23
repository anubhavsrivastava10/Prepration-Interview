
# 1 2 3 4 5 5 4 3 2 1
# 1 2 3 4 * * 4 3 2 1
# 1 2 3 * * * * 3 2 1
# 1 2 * * * * * * 2 1
# 1 * * * * * * * * 1
n = int(input())
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print(j+1,end=" ")
        else:
            print('*',end=" ")
    for j in range(n):
        if i+j>(2*i)-1:
            print(n-j,end=" ")
        else:
            print('*',end=' ')
    print()