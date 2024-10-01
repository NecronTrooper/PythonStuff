score = input("Enter Score: ")
val = 0
try:
    val = float(score)
except:
    print("enter number")
    quit()
if val >=0.9:
    print("A")
elif val >=0.8:
        print("B")
elif val >=0.7:
        print("C")
elif val >=0.6:
        print("D")
elif val <0.6:
        print("f")