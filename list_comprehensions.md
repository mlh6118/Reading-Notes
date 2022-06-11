# List Comprehensions

List comprehension can replace the need for `for` loops in Python.  
* elegant way to create and manage lists
* more compact way of creating lists
* more flexible than `for` loops, typically faster than other methods

### Syntax
my_new_list = [_expression_ for _item_ in _list_]
where<br>
expression = what is to be carried out  
item = what expression is to work on  
list = list of objects to build new list from

### Examples
Each of the examples below show the versatility of how list comprehension 
can be used to create increasingly complex code with a single line or two.
* Create a list with range()  
`digits = [x for x in range(10)]`  


* Create a list using loops and list comprehension  
`squares = [x**2 for x in range(10)`  


* Multiplying parts of a list  
`multiples_of_three = [x*3 for x in range(10)`  


* Show the first letter of each word  
`letters = [name[0] for name in authors`


* Lower/upper case converter  
`lower_case = [letter.lower() for letter in ['A', 'B', 'C']]`


* Print numbers only from a given string  
`phone_number = [x for x in user_data if x.isdigit()]`


* Parsing a file  
`file = open("dreams.txt", 'r')
 poem = [line for line in file]`


* Using functions  
`nums = [double(x) for x in range(1,10)]`

#### [Source: List Comprehensions in Python](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)