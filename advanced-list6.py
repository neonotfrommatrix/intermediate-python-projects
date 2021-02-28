"""
In this lesson we will continue with expanding our understanding of lists. We will focus in this session to target certain items in a list by using indexes. 

Lesson Plan:
Go Over python library functions for lists
Game to implement using library functions

"""

myList = [2,4,6,8,10,15,20]
print(myList[0:2])
print(myList[3:5])
myList[3] = "word"
print(myList)
print(myList.index("word"))
print(myList.index(15))

unordered = [9,4,82,751,962,3,10]
print(unordered)
unordered.sort()
print(unordered)
unordered.sort(reverse = True)
print(unordered)

myList = [2,4,6,8,10,15,20]
myList.append(60)
print(myList)
myList.insert(3,2) #(index, value)
print(myList)
myList.remove(4)
print(myList)
myList.pop(4)   #this is the index
print(myList)

# This is a game in which the students can practice their python list library functions.

print("Welcome to Math List Games")
print("Make list B be the same as List A")
print( )
aList = [2,4,6,8,10,15,20]
print("List A:")
print(aList)
print("List B:")
bList = [4,5,6,8,798,15]
print(bList)

def Menu():
  print("1. Append")
  print("2. Remove")
  print("3. Insert")
  print("4. Pop")
  print("5. Print")
  print("6. DONE: Check Score")

while True:
  Menu()
  choice = input("Which Choice?")
  if choice == "1":
    print("Append")
    num = int(input("What Num?"))
    bList.append(num)
  elif choice == "2":
    print("Remove")
    num = int(input("What Num?"))
    bList.remove(num)
  elif choice == "3":
    print("Insert")
    index = int(input("What Index?"))
    num = int(input("What Num?"))
    bList.insert(index,num)
  elif choice == "4":
    print("Pop")
    index = int(input("What Index?"))
    bList.pop(index)
  elif choice == "5":
    print("Print")
    print(bList)
  elif choice == "6":
    print("Check")
    if aList==bList:
      print("All Matched! You win")
    else:
      print("No Match, You lose")
    break
  else:
    print("Error, Try Diff Choice")

