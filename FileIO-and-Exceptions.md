# FileIO and Exceptions

## FileIO
Reading and writing files are one of the most common tasks that can be done 
with Python.

### What is a file?
* A contiguous set of bytes used to store data.
</br></br>
* Parts of a file:
  * Header: metadata about the contents of the file (name, size, type, etc.)
  * Data: contents of the file
    * This is represented by the file extension.
  * End of file (EOF): special character that indicates the end of the the file
</br></br>
* Parts of file paths:
  * Folder path: file folder location on the file system
    * Folders are separated by "/" (Unix) or "\\" (Windows)
  * File name: actual name of the file
  * Extension: end of the file path pre-pended with a "." to indicate the 
    file type
</br></br>
* Line endings or new line:
  * Standardization diverged between ISO and ASA groups.  This caused 
    divergence in how Windows and Unix/Mac handle them.  This can impact how 
    to handle files if iterating over each line.
  * Windows: CR+LF (\\r\\n)
  * Unix/Mac: LF (\\r)
</br></br>
* Character encodings:
  * Encoding is a translation from byte data to human readable characters.  
    Typically, this is done by assigning a numerical value to represent a 
    character.  Two common encodings are ASCII and UNICODE.
  * ASCII is a subset of Unicode.
</br></br>
* Opening and Closing a file in Python:
  * Python built-in function `open()`
    * Usage: `file = open('file_name.ext')`
  * Always close a file that's been opened.
    * Two methods:
      * try-finally block where finally is `file.close()`
      * with statement (preferred method)
        * `with open('file_name.ext') as reader:`
  * Optional second positional argument is `mode`
    * 'r': Open for reading
    * 'w': Open for writing, overwrites the existing file
    * 'rb' or 'wb': Open in binary mode
    * 'a': append

##### Reference: [Reading and Writing Files in Python (Guide)](https://realpython.com/read-write-files-python/)

## Exceptions
Ways to handle exceptions:
* `raise`: allows you to throw an exception at any time.
* `assert`: enables you to verify if a certain condition is met and throw an 
  exception if it isn't.
* `try`: all statements are executed until an exception is encountered.
* `except`: used to catch and handle the exception(s) that are encountered 
  in the `try` clause.
* `else`: sections that should only run when no exceptions are encountered 
  in the `try` clause.
* `finally`: sections of code that should always run.

##### Reference: [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)