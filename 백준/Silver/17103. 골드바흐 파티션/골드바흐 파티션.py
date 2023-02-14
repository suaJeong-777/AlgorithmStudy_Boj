array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

tc = int(input())
for i in range(tc):
    n = int(input())
    count = 0
    
    for i in range(2, n//2+1):
        if array[i] and array[n-i]:
            count+=1

    print(count)