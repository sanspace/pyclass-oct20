# Day 2

## Reference

  - 

## Practice

  - Implement a function with *args and *kwargs to accept any number of args and kwargs from the caller
  - Create a list of lists using nested list comprehension.
  - Use sys module to get command line args and print them
  - Try out read, readline(s), and looping over file object
  - try json.dump and load for different data structures in python
  - dictionaries
    - given a list of numbers (`nums = [1, 2, 3]`) use dict comprehension to create a dict of squares `{ 1: 1, 2: 4, 3: 9}`
    - make a list of values alone from the above dictionary `[1, 4, 9]` using list comprehension
  - set comprehension
    - given a list `[1, 2, 5, 2, 3, 1, 4, 5]`, create squares of unique items using set comprehension. `{1, 4, 9, 16, 25}`
  - classes
    - create a class that provides the factorials for the list of numbers provided. Checkout `__repr__` and `__str__` methods and implement those for your class.
  - iterators
    - Create  an iterator using a class that behaves as below:
    ```python
        i = I(5) # I is the class you're gonna implement
        for num in i:
            print(i)
        # should output
        1
        2
        3
        4
        5
    ```
  - generators
    - Create a generator for the similar functionality
    ```python
      i = i(5) # i is the generator function that you need to implement
      for num in i:
          print(i)
      # should output
      1
      2
      3
      4
      5
    ```
  - put the generator and iterator in a file of their own and import both in a third file and test it out.
  - create custom exceptions and raise it when I pass non-numeric values to the iterator class.
    - if i call I('s'), raise InvalidInputTypeError
    - if i call I('-5'), raise InvalidNegativeInputError