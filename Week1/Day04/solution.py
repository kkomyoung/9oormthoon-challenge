# 1. 값을 입력받는다.
N = int(input())
K = [*map(int, input().split())]

# 2. 가장 큰 값의 인덱스를 찾는다.
biggestIndex = K.index(max(K))

# 3. 가장 큰 값의 인덱스를 기준으로 왼쪽, 오른쪽으로 나누어 배열에 저장한다.
leftPart = []
rightPart = []

for idx, val in enumerate(K):
    if idx < biggestIndex:
        leftPart.append(val)
    elif idx > biggestIndex:
        rightPart.append(val)

# 4. 오른쪽 요소의 배열은 반전해준다.
rightPart.reverse()

# 5. 배열과 오름차순으로 정렬한 배열의 값이 동일할 경우에만 K 배열의 값을 더해준다.
# 동일하지 않을 경우 0을 출력한다.
if leftPart == sorted(leftPart) and rightPart == sorted(rightPart):
    print(sum(K))
else:
    print(0)
