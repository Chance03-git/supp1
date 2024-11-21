def add(num1, num2):
  """ Adds two numbers and returns the results
    
    Args:
     num1: the first summand
     num2: the second summand 

     returns:
      The sum of the two numbers
     """ 
  return num1 + num2

def test_should_return_four_for_two_and_two():
    assert add(2, 2) == 4

def test_return_the_length_of_string_and_return():
   assert count("Hello") == 5 