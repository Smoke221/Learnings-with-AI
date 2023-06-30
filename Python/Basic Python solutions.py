#1. Write a Python program that prints "Hello, World!" to the console.
print("Hello World!")

#2.  Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
integer = 4
floatNumber = 4.6
string = "Masai"
boolenValue = True
listValue = [1, 2, 3, 4, 5]
tupleVariable = (1, 2, 3, 4, 5)
dictonary = {"city": "Banglore", "state": "Karnataka"}
setValues = {1, 2, 3, 4, 5}

print("Type of integer:", type(integer), "value:", integer)
print("Type of floatNumber:", type(floatNumber), "value:", floatNumber)
print("Type of string:", type(string), "value:", string)
print("Type of boolenValue:", type(boolenValue), "value:", boolenValue)
print("Type of listValue:", type(listValue), "value:", listValue)
print("Type of tupleVariable:", type(tupleVariable), "value:", tupleVariable)
print("Type of dictonary:", type(dictonary), "value:", dictonary)
print("Type of setValues:", type(setValues), "value:", setValues)

#3. Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
numbers = list(range(1, 11))
print("Original List:", numbers)
# adding a number
numbers.append(11)
print("After adding 11:", numbers)
#removing a number
numbers.remove(2)
print("After removing 2:", numbers)
#sorting the list
numbers.sort()
print("After sorting:", numbers)
# If we want to sort the list in descending order we can pass reverse=True paramater to sort()

# 4.  Write a Python program that calculates and prints the sum and average of a list of numbers.
Sum = sum(numbers)
print("Sum of numbers list:", Sum)
n = len(numbers)
Average = Sum / n
print("Average of numbers list:", Average)


# 5. Write a Python function that takes a string and returns the string in reverse order.
def reverse_string(input):
  reversed = ""
  for char in input:
    reversed = char + reversed
  return reversed


# Example usage
string = "Hello, World!"
reversed_string = reverse_string(string)
print(reversed_string)


# 6. Write a Python program that counts the number of vowels in a given string.
def countVowels(input):
  vowels = 'aeiouAEIOU'
  count = 0
  for char in input:
    if char in vowels:
      count += 1
  return count


string = "Hello"
numOfVowels = countVowels(string)
print("Number of vowels in", string, "is", numOfVowels)


#7. Write a Python function that checks whether a given number is a prime number.
def checkPrime(input):
  if input <= 1:
    return False
  for i in range(2, int(input**0.5) + 1):
    if input % i == 0:
      return False
  return True


num = 37
isPrime = checkPrime(num)
if isPrime:
  print(num, "is a prime number")
else:
  print(num, "is not a prime number")


#8. Write a Python function that calculates the factorial of a number.
def factorial(input):
  if input < 0:
    return None
  elif input == 0:
    return 1
  else:
    return input * factorial(input - 1)


num = 5
factorialOfNum = factorial(num)
print("factorial of", num, "is:", factorialOfNum)


#9. Write a Python function that generates the first n numbers in the Fibonacci sequence.
def fibonacci(input):
  sequence = []
  if input <= 0:
    return sequence
  elif input == 1:
    sequence.append(0)
    return sequence
  else:
    sequence = [0, 1]
    while len(sequence) < input:
      next_number = sequence[-1] + sequence[-2]
      sequence.append(next_number)
    return sequence


num = 10
fib = fibonacci(num)
print("Fibonacci sequence of", num, "numbers:", fib)

#10. Use list comprehension to create a list of the squares of the numbers from 1 to 10.
squares = []
for i in range(1, 11):
  squares.append(i**2)

print(squares)
