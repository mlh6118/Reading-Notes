# Document Object Model

## Objects

> Objects group together a set of variables and functions to create a model of something you would recognize from the real world. (Duckett, pg 100)

In an object:
- variable --> property
- function --> method
- name     --> key
- value    --> value

Literal notation of an object:
- Object stored in a variable with contents within curly braces.
- Contents are properties and methods.
- Contents are separated by a comma.
- The last key-value pair does not have a comma after it.

Accessing object contents:
- Dot notation vs Square bracket syntax
  - Dot notation:
    - Contents are called using `object.property/method name` (ex. `car.model` and `car.acceleration()`)
  - Square bracket syntax:
    - Used when 
      - Property or method has a special character in the name.
      - Variable is used in place of property name.
      - `object['property/method name']` (ex. `car['model']` and `car['acceleration']()`)

## Nodelists
Index starts at 0<br>
Can use () or []

| Live                                     | Static                                                   |
|------------------------------------------|----------------------------------------------------------|
| getElementBy...                          | querySelector                                            |
| updated at same time script updates page | reflect document when query was made, not script changes |
| searches HTML for class name             | searches HTML page for what the CSS code would look for  |

## DOM Manipulation
1. Create the element  
  createElement()
2. Give it content
  createTextNode()
3. Add it to the DOM
  appendChild()

### Removing
1. Store element to remove in variable (document.getElementBy)
1. Store parent of element in variable (removeEl.parentNode)
1. Remove element from containing element (removeChild())

### Attribute Nodes
1. Select element node with attribute
  document.getElementByID('one')
1. Use a method or property to work with attribute
  getAttribute('class')

  putting it all together:  
  document.getElementById('one').getAttribute('class');

**Source: Javascript & Jquery by Jon Duckett**