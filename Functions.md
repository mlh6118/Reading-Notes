## Expressions and Operators in JavaScript

Types of operators:
- Assignment operators: =, +=, -=, *=, /=, %=, **= (exponential), and more
- Comparison operators: ==, !=, === (strict equal), !== (strict not equal), >, >=, \<, \<=
- Arithmetic operators: % (remainder), ++, --, - (returns negative of value), + (returns positive of value), ** (calculates exponents)
- Bitwise operators: &, "\|", ^, ~, \<\<, >>, >>>
- Logical operators: &&, "\|\|", !
- String operators: +, +=
- Conditional (ternary) operator: condition ? val1 : val2
- Comma operator: ,
- Unary operators: delete, typeof, void
- Relational operators: in, instanceof

Operator precedence:
- Determines order they are applied when evaluating an expression.
  - Can override using paretheses.

Expressions:
- Any valid unit of code that resolves to a value.

## Functions

Functions are a fundamental building block in JavaScript.

To use them, they must be defined within the scope it is being called from.

Function declarations consist of:
- Keyword <u>function</u>
- Name of the function
- Parameters passed to the function
- Code block defining the function statements, enclosed in curly brackets

```html
function area(length, width) {
  return length * width;
}
```

Function scope means something declared within the function cannot be seen outside of that function.
