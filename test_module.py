# inbuilt modules are collections, datetime, logging, math, numpy, os, pip, sys, and time.

import random
from collections import Counter
import statistics as s
# runtime input output or error showing
import sys
import logging

import makemodule

print("randrange", random.randrange(3, 9))
print("getstate", random.getstate())
random.seed(10)
print("seed", random.random())
mylist = ["apple", "banana", "cherry"]
print("choice", random.choice(mylist))

# own module
print("*******************Create my own module**************************")
emp = makemodule.Employee("Niral", "Intern")
emp.show()


def count_in_list(l, word):
  c = Counter(l)
  return c[word]


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


