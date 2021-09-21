
def add_one(number):
  # 0) Function: add_one 
  #
  # Takes one int and returns that int plus one.
  #
  # e.g. add_one(5) == 6
  #      add_one(-1) == 0
  return number + 1


def is_even(number):
  # 1) Function: is_even 
  #
  # Takes one int and returns True if it's even, False otherwise.
  #
  # e.g. is_even(-2) == True
  #      is_even(61) == False
  if number % 2 == 0:
    return True
  else:
    return False


def halve(number):
  # 2) Function: halve 
  #
  # Takes one int and returns an int with half the value.
  #
  # e.g. is_even(50) == 25
  #      halve(21) == 10
  return number // 2

def triple(x):
  # 3) Function: triple 
  #
  # Takes one int and returns an int with triple the value.
  #
  # e.g. is_even(5) == 15
  #      add_one(-2) == -6
  return 3*x


def collatz(x):
  # 4) Function: collatz 
  #
  # Takes one parameter, a positive integer, and returns either:
  # - If the number is even, half the value
  # - If the number is odd, triple the value and add one
  #
  # e.g. collatz(6) == 3
  #      collatz(5) == 16
  #      collatz(2) == 1
  if is_even(x) == True:
    return halve(x)
  else:
    return triple(x) + 1

def collatz_loop(x):
  # 5) Function: collatz_loop
  #
  # Takes one parameter, a positive integer. It should
  # repeatedly call the collatz function you wrote
  # in (8) in a loop, until the return value is 1.
  # Then it should return the number of loops it took
  # to reach 1.
  #
  # e.g. collatz_loop(1) == 0
  #      collatz_loop(8) == 3
  #      collatz_loop(5) == 5
  count = 0
  while x != 1:
    x = collatz(x)
    count += 1
  return count

def collatz_conjecture(x):
  # 6) Function: collatz_conjecture
  #
  # Takes one parameter, a positive integer. It should
  # loop through every positive integer up through the
  # parameter and call collatz_loop with each of
  # those integers. It should save and return the manumberimum
  # number of loops it took to reach 1 among those numbers.
  #
  # e.g. collatz_conjecture(2) == 1
  #      collatz_loop(1) == 0 and collatz_loop(2) == 1, and the
  #      manumber is 2, so the return is 2.
  #
  #      collatz_conjecture(5) == 7 
  #      Of the numbers 1-5, it takes 3 the longest to reach 1:
  #      3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 which is 7 steps,
  #      so the return is 7.
  #
  #      collatz_conjecture(10) == 19
  #      Of the numbers 1-10, it takes 9 the longest and it takes
  #      19 steps, so the return is 19.
  #     
  # More about this here:
  # https://en.wikipedia.org/wiki/Collatz_conjecture
  max_loop = 0
  number = 1
  while number <= x:
    count = collatz_loop(number)
    if count > max_loop:
      max_loop = count
    number += 1
  return max_loop