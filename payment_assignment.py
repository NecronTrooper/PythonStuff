hrs = input("Enter hours:")
try:
   flt_hrs = float(hrs)
except:
   print("Hey, I said hours, NUMBER")

grp = input("Enter gross pay:")
try:
   flt_grp = float(hrs)
except:
   print("Hey, I said hours, NUMBER")
try:   
   print("Payment:",flt_hrs*flt_grp)
except:
   print("kill yourself")