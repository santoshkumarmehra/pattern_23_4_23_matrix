n = int(input("enter number of rows? : "))
for i in range(n):
    k = i+1
    for j in range(n-i-1):
        print(" ", end="  ")
    for j in range(i+1):
        print(k, end=" ")
        k -= 1
    if i>0:
        for j in range(i-1):
            print(" ", end=" ")
        for j in range(i+1):
            k += 1
            print(k, end=" ")
    print()

for i in range(1, n):
    k = n-i
    for j in range(i):
        print(" ", end="  ")
    for j in range(n-i):
        print(k, end=" ")
        k -= 1
    if i<(n-1):
        for j in range(n-i-2):
            print(" ", end=" ")
        for j in range(n-i):
            k += 1
            print(k, end=" ")
    print()
    
# output
# enter number of rows? : 5
#             1
#          2 1 1 2
#       3 2 1   1 2 3
#    4 3 2 1     1 2 3 4
# 5 4 3 2 1       1 2 3 4 5
#    4 3 2 1     1 2 3 4
#       3 2 1   1 2 3
#          2 1 1 2
#             1

