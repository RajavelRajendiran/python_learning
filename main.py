txt = " The best things in life are free! "
print(txt[:5])
print("free" in txt)
print(txt.replace("best","worst"))
print(txt.strip())
print(txt.upper())
print(txt.split(","))
for x in txt:
    print(x)
if "free" in txt:
    print("Yes, 'free' is present.")
a = "Hello"
b = "World"
c = a + b
print(c)
age=25
month=2
year=5
d="iam raja and my age is {0}\n with{2}years,{1}months of exp"
print(d.format(age,month,year))
    
