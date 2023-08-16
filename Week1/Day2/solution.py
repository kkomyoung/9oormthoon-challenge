N = int(input())
T, M = map(int, input().split())
totalWorkTime = 0

for i in range(N):
    totalWorkTime += int(input())

totalM = (M + totalWorkTime % 60)
T = (T + int(totalWorkTime / 60) + int(totalM / 60)) % 24
M = totalM % 60
print(T, M)
