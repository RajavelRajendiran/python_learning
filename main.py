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