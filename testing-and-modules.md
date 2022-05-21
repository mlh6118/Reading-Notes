# Testing and Modules

TDD, which stands for Test-Driven Development, means writing the tests 
before writing the code.

In TDD, the smallest test that can be done against a to-be-written function 
should be.  Based on that test, the function is then written.

Test file names should be the same as the module file name with "test_" 
pre-pended.

A convention that is widely used is AAA (Arrange, Act, and Assert).
* Arrange: Organize data needed to execute code (input).
* Act: Execute code being tested.
* Assert: Check if result (output) is the same as expected.

The Cycle is three steps:
* Write a unit test and make it fail.
* Write the feature and make the test pass.
* Refactor the code.

##### Reference: [In Tests We Trust - TDD with Python](https://code.likeagirl.io/in-tests-we-trust-tdd-with-python-af69f47e6932)

# `if __name__ == "__main__"`
* Every Python module has it's __name__ defined.  If the module is being run 
  as a standalone, then \_\_name__ is "\_\_main__".
* If the module is imported into another script, then \_\_name__ is the name 
  of the module being imported.
* `if __name__ == "__main__"` is only used if the module is run as a 
  standalone and not imported.

##### Reference: [What does the if __name__ == "\_\_main__" do?](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

# Recursion
Recursion is when a function calls itself directly or indirectly.

* Base case: Provided to the program.
* Other case: Small function that calls itself.
* Stack Overflow error: Occurs when the base case is not reached or defined.
* Direct recursion: Function calls itself.
* Indirect recursion: A function calls another function which then calls the 
  original function.  (Essentially a circular process.)

##### Reference: [Recursion](https://www.geeksforgeeks.org/recursion/)

### Things I want to know more about:
* Stacks and memory