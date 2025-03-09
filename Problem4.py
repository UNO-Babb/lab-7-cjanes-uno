#Problem4.py
#Name: Colton Janes
#Date: 03/09/2025
#Assignment: Lab 7 - Project Euler Problem 4

### Problem 4 - Largest palindrome product
### A palindromic number reads the same both ways. The largest palindrome made,
###### from the product of two 2-digit numbers is 9009 = 91 × 99.

### Find the largest palindrome made from the product of two 3-digit numbers.

from NumberTests import isPalindrome
from NumberTests import findLargestPalindrome

def main():
  largest_palindrome, num1, num2 = findLargestPalindrome()
  print("The largest palindrome from two 3-digit numbers is:", largest_palindrome)
  print("This occurs when " + str(num1) + " is multiplied by " + str(num2) + ".")
    
if __name__ == '__main__':
  main()
