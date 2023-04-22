N = int(input("enter number: "))
k = (2*N)-1
low = 0
high = k-1
value = N
matrix = [[0 for i in range(k)] for j in range(k)]
for i in range(N):
    for j in range(low, high+1):
        matrix[i][j] = value
    for j in range(low+1, high+1):
        matrix[j][i] = value
    for j in range(low+1, high+1):
        matrix[high][j] = value
    for j in range(low+1, high):
        matrix[j][high] = value
    low += 1
    high -= 1
    value -= 1

for i in range(k):
    for j in range(k):
        print(matrix[i][j], end=" ")
    print()

# output 
# enter number: 3
# 3 3 3 3 3 
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3
# 3 3 3 3 3
