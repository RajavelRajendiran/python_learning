class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1=person("rahul",22)
p2=person("vijay",25)
p3=person("hari",26)
print(p1.name,p1.age)
print(p2.name,p2.age)
print(p3.name,p3.age)
class students:
  def __init__(self,name,rollno):
    self.name=name
    self.rollno=rollno
  def __str__(self):
    return f"{self.name} {self.rollno}"
a1=students("raja",4)
print(a1)