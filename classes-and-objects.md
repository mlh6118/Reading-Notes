# Classes and Objects
* Classes are a template to create objects.
* Objects combine variables and functions into a single entity.
* Objects get their variables and functions from classes.
* Multiple objects may be created from the same class.
  * Variables within objects of the same class may be changed independently.


* To assign a class to an object, the generic syntax is:<br>
    `newobject = Class()`


* To access a variable inside of an object, the generic syntax is:<br>
    `newobject.variable`


* To access a function inside of an object, the generic syntax is:<br>
    `newobject.function()`

* `__init__()` is a special function called when the class is initiated.  It 
  is used for assigning values in a class.

##### Source: [Classes and Objects](https://www.learnpython.org/en/Classes_and_Objects)

# Recursion
A recursive function is one that calls itself via self-referential expressions.

* The function will continue to call itself until a condition to return a 
  result is met.
* All recursive functions have:
  * base case
  * recursive case

* Maintaining state can be done in two ways:
  * Threading through recursive call (i.e., passing the updated current 
    state to each recursive call as arguments)
  * Keep it in global scope.

* Recursive data structures are when something can be defined in smaller 
  versions of itself.
* Recursion is also seen as self-referential.
* Recursive data structures include: list, set, tree, dictionary, etc.

* Stack overflow can occur if doing deep recursion due to a limited call 
  stack depth.
* Python's mutable data structures don't support structural sharing, so acting 
  like they are immutable data structures is going to affect space and garbage 
  collection.

##### Things I'd like to know more about:<br>
Naive recursion and lru_cache

##### Source: [Thinking Recursively in Python](https://realpython.com/python-thinking-recursively/) 

# Fixtures and Coverage
* Fixtures are objects, like data, network, or filesystem that need to be 
  shared across tests.
  * Defined using the pytest.fixture decorator and a function definition.
  * The fixture is called by a specific test in the test's parameter list, 
    then referred to by name in the test.
  * Coverage refers to checking that tests have run all of the code.
    * pytest-cov will do this with the `pytest --cov[options]` command.
    * Turn the coverage report into html with the command `coverage html`.

##### Source: [Python Testing with pytest: Fixtures and Coverage](https://www.linuxjournal.com/content/python-testing-pytest-fixtures-and-coverage)
