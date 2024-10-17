fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0.0
allv = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        position = line.find(":")
        number_str = line[position+1:].strip()
        number = float(number_str)
        count += 1
        allv += number
average = allv/count

print("Average spam confidence:", average)