def tri_recurtion(k):
  if(k>0):
    result = k + tri_recurtion(k-1)
    print(result)
  else:
    result=0
  return result
print("\n\nRecurtion Example Results")
tri_recurtion(6)
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
def my_func(n):
  return lambda a:a*n
my_doubler=my_func(2)
print(my_doubler(11))