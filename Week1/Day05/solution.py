N, K = map(int, input().split())
decimal_numbers = input().split()

binary_numbers = list(map(lambda x: bin(int(x))[2:], decimal_numbers))

array = []
for i in binary_numbers:
    count = i.count('1')
    array.append([count, int(i, 2)]) 

array.sort(reverse=True)

print(array[K-1][1])
