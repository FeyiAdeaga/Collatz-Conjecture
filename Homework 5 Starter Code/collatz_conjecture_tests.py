from collatz_conjecture import add_one, is_even, halve, triple, collatz, collatz_loop, collatz_conjecture
import unittest

class TestCollatzConjecture(unittest.TestCase):
  """
  Class for testing Collatz Conjecture.
  """

  def test_add_one(self):
    """
    Example of testing for add_one function

    You do not need to further test add_one
    """
    self.assertEqual(add_one(5), 6)
    self.assertEqual(add_one(1), 2)
    self.assertEqual(add_one(20), 21)
    self.assertEqual(add_one(0), 1)

  # WRITE YOUR TESTS BELOW.
  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  def test_is_even(self):
    self.assertEqual(is_even(20),True)
    self.assertEqual(is_even(2),True) 
    self.assertEqual(is_even(15),False)
    self.assertEqual(is_even(7),False)   
  
  def test_halve(self):
    self.assertEqual(halve(20),10)
    self.assertEqual(halve(2),1) 
    self.assertEqual(halve(10),5)
    self.assertEqual(halve(14),7)   

  def test_triple(self):
    self.assertEqual(triple(7),21)
    self.assertEqual(triple(5),15) 
    self.assertEqual(triple(20),60)
    self.assertEqual(triple(4),12)   

  def test_collatz(self):
    self.assertEqual(collatz(20),10)
    self.assertEqual(collatz(2),1) 
    self.assertEqual(collatz(15),46)
    self.assertEqual(collatz(7),22)   

  def test_collatz_loop(self):
    self.assertEqual(collatz_loop(1),0)
    self.assertEqual(collatz_loop(2),1) 
    self.assertEqual(collatz_loop(8),3)
    self.assertEqual(collatz_loop(5),5)   

  def test_collatz_conjecture(self):
    self.assertEqual(collatz_conjecture(10),19)
    self.assertEqual(collatz_conjecture(2),1) 
    self.assertEqual(collatz_conjecture(5),7)  


if __name__ == '__main__':
    unittest.main()
