## Error Handling

Javascript throws an exception if there's an error.
- Interpreter stops and looks for exception-handling code.
- If interpreter does not find error handling code in the function, it looks at calling function and continues pattern until reaching the global context.
- If no error handler is found, an Error object is created.

### Types of Error Properties
- name
- message
- fileNumber: name of JS file
- line number: where error occurred

### Types of Error Objects:
- Error: generic that all others based on
- SyntaxError: issue like missing ";"
- ReferenceError: tried to use variable not delcared or within scope
- TypeError: unexpected data type
- RangeError: number not in acceptable range

### Dealing with Errors
- Debug the script
- Handle with:  
  - try
  - catch
  - throw
  - finally
