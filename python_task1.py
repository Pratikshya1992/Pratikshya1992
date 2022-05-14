Task 1

1. Check if to is present in the below statement

str1 = "Welcome to python"
print("present", str1.find("to"))

OR

str1 = "Welcome to python"
if "to" in str1:
    print("Yes, 'to' is present")

Task 2 
1. #Add item 70 after 60 in the following Python List
#input
l1 = [10, 20, [30, 40, [50, 60], 80], 90, 100]
#output
[10, 20, [30, 40, [50, 60, 70], 80], 90, 100]

Code - 
l1 = [10, 20, [30, 40, [50, 60], 80], 90, 100]
l1[2][2].insert(2,70)
print(l1)

2. #add sublist [7,8] after 6
#input
l2 = [1,2,[3,4,5,6],9]
#output
[1,2,[3,4,5,6,[7,8]],9]

code - 
l2 = [1,2,[3,4,5,6],9]
l2[2].append([7,8])
print(l2)

Completed till list 10 may 2022

Task 3.
From the above dictionary, do the following tasks

a.access "Mike"
code -
 dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}
output = dict1['april_batch']['student']['name']
print(output)


b.access 80

code - 
dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}
output = dict1['april_batch']['student']['marks']['python']
print(output)

c.change "Mike" to "Your name"
dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}
dict1["april_batch"]["student"]["name"] = "Supriya"
print(dict1)


d.add ML = 80 and DL = 80 inside marks

code - 
dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}
dict1["april_batch"]["student"]["marks"] = {"python":80,"maths":70,"ML":80,"DL":80}
print(dict1)

Task 4
Add and remove the elements from a tuple

a. add
code-
tup1 = (1,2,3,4,5)
output = list(tup1)
output.append(6)
tup1 = tuple(output)
print(tup1)

b. remove
code - 
tup1 = (1,2,3,4,5)
output = list(tup1)
output.remove(5)
tup1 = tuple(output)
print(tup1)

done till tuple

Task 5
Make a table of all the In-built data structures and Point out the differences one by one
LISTS:

Lists are created using square brackets:

Lists are used to store multiple items in a single variable.

Lists are Mutable that is items in it are changeable.

e.g 
test_list = ["India","Nepal", ""]
Tuples are used to store multiple items in a single variable.

Tuples are written with round brackets

Tuple items are ordered, unchangeable, and allow duplicate values. ("IMMUTABLE")

yset = {"apple", "banana", "cherry"}

Sets are used to store multiple items in a single variable.

Set items are unordered, unchangeable, and do not allow duplicate values.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Set items are unchangeable, meaning that we cannot change the items after the set has been created"

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values

The dictionaries are ordered, it means that the items have a defined order, and that order will not change.


Task 6

Ask 2 numbers from users and store it in num1 and num2
Ask user to press 1 for addition,2 for subtraction,3 for multiplication and 4 for division
based on number given by user do the math operation

a.Addition

num1 = 2
num2 = 4
num3 = num1 + num2 
if num3 == 0:
    print("incorrect answer",num3)
else:
    print("correct answer",num3)

b.subtraction

num1 = 2
num2 = 2
num3 = num1 - num2 
if num3 == 0:
    print("correct answer is",num3)
else:
    print("incorrect answer",num3)

c.multiplication
num1 = 2
num2 = 2
num3 = num1 * num2 
if num3 == 0:
    print("incorrect answer is",num3)
else:
    print("correct answer is",num3)

d.division
num1 = 2
num2 = 2
num3 = num1/num2 
if num3 == 0:
    print("incorrect answer is",num3)
else:
    print("correct answer is",num3)

