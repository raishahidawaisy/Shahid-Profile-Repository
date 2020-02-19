#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop, it will execute the set of code till the condition is true
  # while (x<5):
  #   print(x)
  #   x = x+1


  # define a for loop, in Python, its the iterators using the range function
  # here x starts from lower value and upper value is
  # for x in range(5,10):
  #   print(x)

  # use a for loop over a collection
  # days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  # for d in days:
  #   print(d)
    
 
  # use the break condtion to break a loop for a certain condition and continue statements
  # for x in range(5,10):
  #   #if (x==7): break
  #   if (x %2 == 0): continue
  #   #when line 28 is true, it will skip line 30
  #   print(x)


  #using the enumerate() function to get index 
  days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  # in line 36, enumerate function will return the index + value of the looked item
  for i,d in enumerate(days):
    print(i,d)


if __name__ == "__main__":
  main()
