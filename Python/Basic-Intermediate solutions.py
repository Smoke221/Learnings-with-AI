# 1. Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
  for j in range(1, i + 1):
    print(j, end=" ")
  print()

# 2.Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions
# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
  if num > 500:
    break  # Stop the loop if the number is greater than 500
  if num > 150:
    continue  # Skip the number if it is greater than 150
  if num % 5 == 0:
    print(num)

#3. Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
s1 = "Ault"
s2 = "Kelly"
# AuKellylt (Expected output)


def appendStrings(s1, s2):
  concatIndex = len(s1) // 2
  s3 = s1[:concatIndex] + s2 + s1[concatIndex]
  return s3


s3 = appendStrings(s1, s2)
print(s3)

# 4. Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.


def arrangeLowerCase(input):
  lowercase = ""
  uppercase = ""
  for i in input:
    if i.islower():
      lowercase += i
    else:
      uppercase += i
  arranged = lowercase + uppercase
  return arranged


str1 = "PyNaTive"
toLowerCase = arrangeLowerCase(str1)
print(toLowerCase)

# 5. Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]


# ['My', 'name', 'is', 'Kelly'] - Expected output
def addLists(list1, list2):
  newList = []
  minLength = min(len(list1), len(list2))
  for i in range(minLength):
    newList.append(list1[i] + list2[i])

  if len(list1) > minLength:
    newList.extend(list1[minLength:])
  elif len(list2) > minLength:
    newList.extend(list2[minLength:])

  return newList


combined = addLists(list1, list2)
print(combined)

# 6. Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir'] - Expected output

result = [x + y for x in list1 for y in list2]
print(result)

# 7. Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
#  Expected Ouput
# 10 400
# 20 300
# 30 200
# 40 100

for i, j in zip(list1, reversed(list2)):
  print(i, j)
# We use the zip() function to iterate over both lists simultaneously. The zip() function pairs corresponding elements from each list together.

# 7.  Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# Expected output
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
output = {employee: defaults for employee in employees}
print(output)

# 9. Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

newDictionary = {key: sample_dict[key] for key in keys if key in sample_dict}

print(newDictionary)

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
# Expected output tuple1: (11, [222, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list
list1 = list(tuple1)

# Modify the first item of the list inside the tuple
list1[1][0] = 222

# Convert the list back to a tuple
modifiedTuple = tuple(list1)

print(modifiedTuple)
