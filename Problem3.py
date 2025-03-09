#Problem3.py
#Name: Colton Janes
#Date: 03/09/2025
#Assignment: Lab 7 - Project Euler Problem 3

from NumberTests import isPrime
from NumberTests import getFactors

def main():
  number = 657513
  factors = getFactors(number)
  print(factors)

  for f in factors:
    if isPrime(f):
      print(f)

if __name__ == '__main__':
  main()
