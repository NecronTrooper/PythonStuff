fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
#lst_faced = []
for line in fh:
    if line.startswith("From "):
        line = line.split()
        #if line[1] not in lst_faced:
        print(line[1])
        count += 1
            #lst_faced.append(line[1])
print("There were", count, "lines in the file with From as the first word")
