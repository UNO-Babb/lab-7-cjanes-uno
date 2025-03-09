#NumberTests.py

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def getFactors(num):
  """Returns a list of all factors of a given integer"""
  factors = []
  for f in range(1, num // 2 + 1):
    if num % f == 0:
      factors.append(f)

  return factors

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""

  if p == 2:
    return True
  if isEven(p):
    return False

  for div in range(3, p // 2, 2):
    if p % div == 0:
      return False
    
  return True

def findNthPrime(n):
  """Finds the nth prime number."""
  count = 0 #sets the starting primes found
  num = 1

  while count < n: #our nth count of primes
    num = num + 1
    if isPrime(num):
      count = count + 1

  return num #when the count reaches our nth value, return the prime number

def sumPrime(sp):
  """Finds the summation of all prime numbers in a predermined range."""
  total = 0 #set total value to zero

  for num in range(2, sp):
    if isPrime(num):
      total = total + num

  return total

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

def isPalindrome(num):
  """Returns True if pal is a palindrome."""
  if num < 10: #figured out that leaving this out could be a problem :'(
    return False
  orig = num
  rev = 0

  while num > 0:
    pos1 = num % 10 #last digit position, (ie 321 "1" is in pos1, then in 32 it's "2", 3 is "3")
    rev = rev * 10 + pos1
    num = num // 10

  return orig == rev

def findLargestPalindrome():
  """Find the largest palindrome value based on calculation of two numbers."""
  largest = 0 #set base largest value

  for i in range(100, 1000): #first number in test range (i.e. range(10, 100) = 10 through 99, including 99))
    for j in range(100, 1000): #second number in test range
      product = i * j
      if isPalindrome(product) and product > largest:
        largest = product
        num1 = i
        num2 = j
    
  return largest, num1, num2 

#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]

  num1 = int(input("Enter a number (num1): "))
  num2 = int(input("Enter another number (num2): "))

  if isPrime(num1):
    print("%d is a prime number" %(num1))
  if isPrime(num2):
    print("%d is a prime number" %(num2))

  if isEven(num1):
    print("%d is an even number" %(num1))
  if isEven(num2):
    print("%d is an even number" %(num2))

  if isPalindrome(num1):
    print("%d is a palindrome" %(num1))
  if isPalindrome(num2):
    print("%d is a palindrome" %(num2))

if __name__ == '__main__':
    main()
