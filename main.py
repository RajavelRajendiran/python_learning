a=["hi",1,2,3,]#list
for x in a:
 print(x)
b=[4,5,6]
for x in range(len(b)):#looping
 print(b[x])
c=a
c.append("hello")#adding list
print(c)
c[1:4]=["lol","lot","hat"]#changing list
print(c)
i=0
while i <len(c):
 print(c[i])
 i=i+1
c.remove("hi")
print(c)
c.pop((2))
print(c)
[print(x) for x in c]#comprehention
d=[x for x in c if "ol" in x]
print(d)
