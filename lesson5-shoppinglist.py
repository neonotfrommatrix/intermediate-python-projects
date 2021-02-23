"""
Lesson 5: Shopping Lists
This lesson introduces the concept of lists. The objective of this lesson is to provide students with an understanding of the basic functionality of lists, their purpose, general usages, and attributes. The program will follow a particular story.
Lesson plan:
Introduce the concept of lists and use real world examples to demonstrate how it works. I began by asking people how they got dressed in the morning. And where they got their clothes from. The answer you’re looking for here is, dresser. 
Draw a picture of a dresser and explain how each drawer represents an item in the list. What separates the top drawer from the others is a division; however, in lists what separates one item from the next is a comma.
Introduce the prompt -- your mom comes into your room and asks you to go shopping for her. 
Create a shopping list with items that you need to purchase from the store. 
Create an empty list, this represents the shopping bag. 
Spend some time helping the students understand the fundamentals of lists (such as indexes)
Review inputs and how to store the response in a variable 
Review if-elif-else conditions and how to make certain statements lead to different conclusions

"""











# Your mom asks you to go to the local market and get some groceries. She gives you a shopping list. 

# Add as many items in the shopping list as you want
mom_list = ["eggs", "milk", "butter", "bread", "flour"]
grocery_bag = []
print("STORE CLERK: Welcome to my grocery store.")
 
while True:
   answer = input("What item would you like to purchase? ")
   if answer == "check":
# display the shopping list
      print(mom_list)
   elif answer == "done":
      break
   else:
#  add the item to your shopping cart.
   grocery_bag.append(answer)

#You return home and approach your mom, and she asks you if you bought everything she requested 

# Add the following code after the WHILE loop to verify that you purchased all of the items that were on mom’s shopping list::

answer = input("MOM: Did you get everything on my list? ")
if len(grocery_bag) == len(mom_list):
   print("MOM: Thank you -- you got everything I wanted!!")
else:
   print("MOM: No - please try again...")
# Now let’s add some more code to see if the item you requested exists in your shopping list, and also to ensure that you are not requesting something you already purchased.  Add the code highlighted in yellow to the WHILE loop, but be careful about the indentation:

while True:
   answer = input("What item would you like to purchase? ")
   if answer == "check":
# show mom's shopping list
      print(mom_list)
   elif answer == "done":
      break
   else:
      if answer in mom_list:
         if answer in grocery_bag:
            print("CLERK: Sorry, you already purchased that time -- please try again")
         else:
#  add the item to your shopping cart.
            grocery_bag.append(answer)
      else:
         print("CLERK: I don't think that item is on your list -- please try again")

