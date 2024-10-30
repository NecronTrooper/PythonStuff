counts = dict()
scounts= dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
   if name not in counts:
      counts[name] = 1
   else:
      counts[name] = counts[name] + 1
print(counts.get("csev"))
print(counts)

#simplified count by using .get() method
for name in names:
   scounts[name] = scounts.get(name,0) + 1
print(scounts)