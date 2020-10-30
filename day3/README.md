# Day 3

## Reference

  - Virtuals envs and packages https://docs.python.org/3/tutorial/venv.html
  - REST API https://www.restapitutorial.com
  - Decorators
    - I am providing a lot of materials here. Go with what works for you. If you could get some basic understanding, I can fill the gaps for you.
        - little older http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/#section_10
        - https://realpython.com/primer-on-python-decorators/
        - https://www.youtube.com/watch?v=FsAPt_9Bf3U (Video with real life examples as well) 

## Practice

  - Given a list of tuples with current and min balances: `[("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]` use comprehensions to get the below:
    - dict of those with proper balances (above or equal min bal)
        `{"Guido": 2000, "Brandon": 2000}`
    - set of all balances
        `{2000, -52, 900}`
    - list of account holders
        `["Guido", "Raymond", "Jack", "Brandon"]`
    - dict of user and money each need to fulfill the min balance requirement (those who already have enough bal should not be in the dict)
        `{"Raymond": 1052, "Jack": 100}`
    - list of tuples with name and current balance if the balance is above 0
        `[("Guide", 2000), ("Jack", 900), ("Brandon", 2000)]`
    - create a new repo
    - create and activate a new virtual environment
    - use gitignore to skip version control for this venv
    - pip install pytest
    - write tests for your program above (cover at least a few cases)
    - when you are done, someone should be able to clone your repo, pip install from your requirments.txt in a venv and able to run pytest and get a report of your tests
  - Create REST API endpoints for your use case. No code. Just the endpoints alone. e.g. /accounts or /accounts/123
  - If you're adventurous, attempt a decorator after going through the materials above. Or at least try writing an outer inner function
    - Write an outer function that will print a msg before and after callin a function passed to it.

    ```python
    def hello():
        print("hello")
    outer_func(hello)
    ```
    
    should output below

    ```
    calling a function # coming from outer
    hello # coming from print
    called a function # coming from outer
    ```
