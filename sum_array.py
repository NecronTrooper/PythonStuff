def sum_array(a: list) -> int:
   sum = 0
   for i in a:
      sum = sum + i
   return sum

scan_var = input()
parsed_var = list(map(int, scan_var.split()))
print(sum_array(parsed_var))