user_input = int(input())

result = 0
for i in range(user_input):
    inputValue = input()
    result += int(eval(inputValue))
    
print(result)

