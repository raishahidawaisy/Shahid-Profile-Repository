#
# Example file for working with classes
# line6: self is the first argument of any method of a class and 
# refers to the object itslelf

class myClass():
  def method1(self):
    print("myClass method1")
  
  def method2(self, someString):
    print("myClass method2 " + someString)

#lets create another class which takes first class as its argument i.e it inherits first myClass
class anotherClass(myClass):
  def method1(self):
    #call the inherited method in the super class
    myClass.method1(self)
    print("anotherClass method1")
  
  def method2(self, someString):
    print("anotherClass method2 ")

def main():
  c = myClass()
  c.method1()
  c.method2("Test string")

  c2 = anotherClass()
  c2.method1()
  c2.method2("Test 2 string")

  
if __name__ == "__main__":
  main()
