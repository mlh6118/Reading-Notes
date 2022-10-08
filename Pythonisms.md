# Pythonisms
## Dunder Methods
* Set of predefined methods to enrich classes.
* Recognized because they start and end with `__` (double underscores).
* Also referred to as "magic methods".
* Let you emulate behavior of built-in types.

## Iterators
* Another way to handle for-in loops.
* Needs `__init__`, `__iter__`, and `__next__` methods within the class.
* `__next__` needs to `raise StopIteration` to prevent errors from going to 
  the console.

## Generators
* Calling a generator function creates and returns a generator object.
* Requires a `yield` in the code.
* `yield` suspends the function and retains its local state.