#args means I can use as many arguments
#as possible 

def sum(*args):
  total = 0
  for arg in args:
    total += arg
  return total

print(sum(2,3,4,5))

#kwargs means using key values(limitless)