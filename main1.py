def add(num1, num2):
  """ Adds two numbers and returns the results
    
    Args:
     num1: the first summand
     num2: the second summand 

     returns:
      The sum of the two numbers
     """ 
  return num1 + num2

def count(string):
   """Counts the number of characters in a string and returns the result.

    Args:
        string: The string whose characters are to be counted.

    Returns:
        The number of characters in the given string.
    """
   
   return len(string)


def test_should_return_four_for_two_and_two():
    assert add(2, 2) == 4

def test_return_the_length_of_string_and_return():
   assert count("Hello") == 5 

def test_should_insert_new_key():
   dictionary = {}
   key = "test"
   upsert(dictionary, key, 5)
   assert dictionary[key] == 5 