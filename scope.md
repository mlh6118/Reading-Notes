# Scope
Teh concept of scope determines how variables and names are looked up in the 
code.  The scope of a name or variable is based on where it is placed in the 
code when created.

## LEGB: Local, Enclosing, Global, and Built-In scopes

### Understanding Scope
* The scope of a name defines the area of a program which can unambiguously 
  access that name.
  * A name is only visible to and accessible by the code in its scope
* Two types:
  * Global: names are available to all code, defined outside all functions
  * Local: names are only available to code within the scope, defined within 
    a function
* In scope: can access the value of a name from someplace in the code
* Out of scope: access to the name is not possible from the location in the code
* Enclosing scope: exists only for nested functions
* Built-in scope: contains names such as keywords, functions, exceptions, 
  and other attributes that are built into Python

### Python Specific
* Variables: exist when first assigned a value.
* Functions and Classes: available after defined
* Modules: available after importing



##### [Source: Python Scope & the LEGB Rule: Resolving Names in Your Code](https://realpython.com/python-scope-legb-rule/)