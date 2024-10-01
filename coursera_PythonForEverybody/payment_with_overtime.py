hrs = input("Enter Hours:") #if greater than 40, payment 1.5 
grs = input("Enter Gross pay:")
try:
    h = float(hrs)
    gp = float(grs)
except:
    print("Please type numerical values")
    quit()
salary = 0

print("Hours:", hrs)
print("Gross pay:", grs)

if h >= 40:
    overtime = h - 40
    time = h - overtime
    salary = overtime*1.5*gp + time*gp
else:
    salary = h*gp
print(salary)