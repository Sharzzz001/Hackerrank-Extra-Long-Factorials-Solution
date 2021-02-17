#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = int(input())

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("1")
else:
   print(recur_factorial(num))
