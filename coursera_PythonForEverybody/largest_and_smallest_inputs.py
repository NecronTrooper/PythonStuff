largest = -9999
smallest = 9999
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    else: 
        try:
            num = int(inp)
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
        except:
             print("Invalid input")
             
    
    

print("Maximum is", largest)
print("Minimum is", smallest)