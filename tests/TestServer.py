import unittest
#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestServer(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    pass
  #Each test method starts with the keyword test_
  def test_add(self):
    pass
  def test_subtract(self):
    pass
  def test_multiply(self):
    pass
  def test_divide(self):
    pass
  def test_client(self):
    pass
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()