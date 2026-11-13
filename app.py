import unittest
def add(a,b):
  return a+b
def subtract (a,b):
  return a-b
def multiply(a,b):
  return a * b
class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(20,20),40)
  def test_subtract(self):
    self.assertEqual(subtract(20,10),10)
  def test_multiply(self):
    self.assertEqual(multiply(5,5),25)
if __name__=="__main__":
  print("student calculator application")
  print("addition:",add(20,20))
  print("subtraction:",subtract(20,10))
  print("multiplication:",multiply(5,5))
  print("\nExecuting Automated Tests..\n")
  unittest.main(argv=['first-arg-is-ignored'],exit=False)

  
  
  
  
  
