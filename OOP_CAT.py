#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
mycat1 = Cat('bili',2)
mycat2 = Cat('mili',3)
mycat3 = Cat('vili',1)
# 2 Create a function that finds the oldest cat
def oldest_cat(cat1,cat2,cat3):
  if cat1.age > cat2.age and cat3.age:
    oldest = "the oldest cat ",cat1.name," is ",cat1.age," year old"
  elif cat2.age > cat1.age and cat3.age:
    oldest = "the oldest cat ",cat2.name," is ",cat2.age," year old"
  else:
    oldest = "the oldest cat ",cat3.name," is ",cat3.age," year old"

  return oldest
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(oldest_cat(mycat1,mycat2,mycat3))