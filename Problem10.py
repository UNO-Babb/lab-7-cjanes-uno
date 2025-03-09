#Problem10.py
#Name: Colton Janes
#Date: 03/09/2025
#Assignment: Lab 7 - Project Euler Problem 10

### Problem 10 - Summation of primes
### The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

### Find the sum of all the primes below two million. (< 2000000)

from NumberTests import isPrime
from NumberTests import sumPrime

def main():
  sp = 2000000 #sample number is 10; 2000000 could take A LONG TIME, so I tested it for 5000 instead
  prime_sum = sumPrime(sp)
  print("The sum of all prime numbers below " + str(sp) + " is: " + str(prime_sum))

if __name__ == '__main__':
  main()
