# Big O Notation
Big O notation describes the performance or complexity of an algorithm.  Big 
O describes the worst-case scenario, along with the time required or space 
used to run that algorithm.

### Notation: When Used
* O(1): Always executes in the same time or space regardless of the size of 
  the input data set.
* O(N): Grows linearly and in direct proportion to the size of the input 
  data set.  Typical of a single for loop.
* O(N<sup>2</sup>): Directly proportional to the square of the size of the 
  input data set.  The exponent is based on the number of loops that are nested.
* O(2^N): Growth doubles with each addition to the input data set.  Typical 
  of a recursive function.
* O(log N): Typically a binary search of sorted data sets.

##### Reference: [A beginner's guide to Big O Notation](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation)