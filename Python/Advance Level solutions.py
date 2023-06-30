# 1. Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
# - *Input*: [("John", 25), ("Jane", 30)]
# - *Output*: "John is 25 years old. Jane is 30 years old."

data = [("John", 25), ("Jane", 30)]

for name, age in data:
  print(f"{name} is {age} years old.")

# 2.  Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.

person = {"name":"Krishna","age":25}