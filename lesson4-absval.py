# Absolute values as well as taking the sum of the absolute values of all elements in a list

def abs_val(x):                  #takes in an integer
 if x >= 0:                     #if x is positive we return x
   return x
 else:                          #return the absolute value of x if negative
   return x * -1              # alternatively, you could just type “return -x”

print("The absolute value of 6: " + str(abs_val(6)))                #testing our absolute value helper method
print("The absolute value of -4: " + str(abs_val(-4)))
print("The absolute value of 20: " + str(abs_val(20)))
print("The absolute value of -61: " + str(abs_val(-61)))

def abs_sum(list1):              #takes in a list of integers
 total = 0                      #initializes the sum with a value of 0
 for i in range(len(list1)):    #we iterate through the elements in the list
   total += abs_val(list1[i])   #we increase the sum by the absolute value of each element
 return total                   #we return the final sum

print("---------------------------------------------------------------------")
print("The sum of the absolute values of the elements in various lists:")
print(abs_sum([1,2,3,-4]))       #testing our absolute value sum function
print(abs_sum([-9,1,-2]))
print(abs_sum([1,7,6,5]))
print(abs_sum([-3,-2]))


"""
Lesson plan:
Introduce the concept of absolute value and use a number line to demonstrate how it works
Have them write a program that returns the absolute value of a given number
Make the absolute value program into a helper method (We know the method exists within python libraries, but we want the students to understand how it works)
Have them test out the function and print different examples
Introduce the list data type and explain how it can store elements of primitive data types (like str and int)
Explain how lists have indexes that start at 0 and go to the length of the list minus 1 (similar to strings)
Explain how each index corresponds to a specific element within the list
Explain how we can go through each element in a list using a for loop in the range of the length of the list
Have them call the absolute value method from earlier as a helper method that can be used to find the absolute value of each element, which can then be added into the sum variable that was initialized earlier
Reinforce how to return that sum and have the students print out examples of lists inputted into the method
Time permitting, allow the students to create their own additional functions to perform some simple arithmetic stuff; note that a function can be called from within a function 

def diff (num1, num2):          # find the difference between two numbers
  return abs_val(num1 - num2)    # return the absolute value of the difference

def squared (num):          # find the square of a number
  return num * num   

def max_value (num1, num2):    # find the maximum of two numbers
  if num1 >= num2:
     return num1               # why “>=” and not just “>” ?
  else:
     return num2


"""
