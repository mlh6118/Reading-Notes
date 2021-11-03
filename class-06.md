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


**Source: Javascript & Jquery by Jon Duckett**