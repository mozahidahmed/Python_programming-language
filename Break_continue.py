#break
numbers = [1, 5, 0, -4, 10, 9]
for val in numbers:
  if val < 0:     # condition to break
  break
  print(val) #1,5

#continue 
numbers = [1, 5, 0, -4, 10, 9]
for val in numbers:
  if val < 0:     # condition to break
  continue 
  print(val) #1,5,10,9

