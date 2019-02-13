N = 9
numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
print(numbers)

i = 1
while i < N:
    j = 0    
    while j <= N-2:
        if numbers[j] > numbers[j+1]:
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
            j+=1
        else:
            j+=1
    else:
        i+=1

print(numbers)

