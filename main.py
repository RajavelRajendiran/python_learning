a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
c=2
d=5
if c>d:
    print("c if greater than d")
elif c==d:
    print("c=d")
else:
    print("d is greater than c")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
