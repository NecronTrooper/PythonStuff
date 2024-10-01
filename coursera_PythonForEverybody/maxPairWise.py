def MaxPairWise(numbers):
    n = len(numbers)

    if n < 2:
        return 0  
    
    it = 0
    for i in range(1, n):
        if numbers[i] > numbers[it]:
            it = i
    
    it2 = -1  
    for i in range(0, n):
        if i != it:
            if it2 == -1 or numbers[i] > numbers[it2]:
                it2 = i

    return numbers[it] * numbers[it2]


n = int(input())  
user_input = input()  

num_list = list(map(int, user_input.split()))

print(MaxPairWise(num_list))
