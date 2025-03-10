#Problem7.py
#Name: Colton Janes
#Date: 03/09/2025
#Assignment: Lab 7 - Project Euler Problem 7

### Problem 7 - 10001st prime
### By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
######  we can see that the 6th prime is 13.

### What is the 10001st prime number?

from NumberTests import isPrime
from NumberTests import findNthPrime

def main():
  num = 10001
  nth_prime = findNthPrime(num)

  print("The " + str(num) + "th prime number is: " + str(nth_prime))

if __name__ == '__main__':
  main()
