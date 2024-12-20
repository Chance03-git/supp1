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

def upsert(dictionary, key, value):
  """upserts a value into the dictionary

   The value must implement addition with itself 

    Args:
        dictionary: the dictionary to upsert to
        Key: The key to the dictionary for the upsert
        value: The value being upsert
    """
   
  if key in dictionary.keys():
      #dictionary contains key, update
      dictionary[key] = dictionary[key] + value
  else:
      #dictionary does not contain key, set
      dictionary[key] = value

def test_should_return_four_for_two_and_two():
    assert add(2, 2) == 4

def test_return_the_length_of_string_and_return():
   assert count("Hello") == 5 

def test_should_insert_new_key():
   dictionary = {}
   key = "test"
   upsert(dictionary, key, 5)
   assert dictionary[key] == 5 

def test_should_append_new_key():
   dictionary = {}
   key = "test"
   upsert(dictionary, key, 5)
   upsert(dictionary, key, 2)
   assert dictionary[key] == 7 