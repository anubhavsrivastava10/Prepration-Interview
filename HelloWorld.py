# n = int(input())
# for i in range(n):
#     if i<n-1:
#         for j in range(n-i-1):
#             print(" ",end="")
#         print("*",end="")
#         for j in range((n-(n-i))*2):
#             print(" ",end="")
#         if i>0:
#             print("*")
#         else:
#             print()
#     else:
#         print("*"*(n*2))
    
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# row = 0
# col = 0
# dist_row = len(matrix)
# dist_col = len(matrix)
# while(row<dist_row and col<dist_col):
#     for i in range(col,dist_col):
#         print(matrix[row][i],end=" ")
#     row += 1
#     for i in range(row,dist_row):
#         print(matrix[i][dist_col-1],end=" ")
#     dist_col -= 1
#     if row<dist_row:
#         for i in range(dist_col-1,col-1,-1):
#             print(matrix[dist_row-1][i],end=" ")
#         dist_row -=1
#     if col<dist_col:
#         for i in range(dist_row-1,row-1,-1):
#             print(matrix[i][col],end=" ")
#         col+=1


lst =   [1,0,0,0,0,1,0,1,0,1,1]
one = 0
zero = 0
for item in lst:
    if item==1:
        one+=1
    else:
        zero+=1
if one == zero:
    print(len(lst))
else:
    stock = {}
    stock[0] = -1
    length = 0
    index = -1
    total = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            total += -1
        else:
            total += 1
        if total in stock:
            if length< i-stock.get(total):
                length = i-stock.get(total)
                index = i
        else:
            stock[total] = i
    if index != -1:
        print(length)