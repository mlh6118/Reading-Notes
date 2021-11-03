## Constructors

Declare constructor  
`var car = new Object();`

Add methods and properties via dot notation  
`car.brand = 'Honda';`  
`car.model = 'Civic';`  
```
car.acceleration = function(){  
  return 60/numSectionds;  
}
```

To update property values:
`car.brand = 'Toyota';`  
`car['model'] = 'Cressida';`

To remove a property:
`delete car.model;`  
`delete` is a keyword

## Object Constructor Template

Allows multiple object creation from single function steps:
1. Create new function with Object group name.  
  Ex: `function Car(){}`
1. Add properties and methods inside {}  
use keyword `this` instead of object name because properties and methods belong to the function object created.  
  Ex: `this.brand = brand;`  
  be sure to include property in parameters list.
1. Create instances of object using constructor function.
  requires keyword `new`  
  properties are given as arguments to the function  
  Ex: `let carOne = new Car('Honda', 'Civic', 10);`  
      `let carTwo = new Car('Toyota', 'Cressida', 9);`
1. Add or remove properties to existing constructor.  
  use dot notation  
  Ex: `Car.modelYear = 2007;`  
      `delete Car.acceleration;`

### this (keyword)

Used inside functions and objects  
Where function declared changes what `this` means  
Always refers to one object

### Arrays

Are objects  
Key values are the index number  
Has a length property  
Can be in an object  
Can have objects

### Object Model

A group of objcts that represent related things from the real world that combined form a model of something larger  
Objcects may contain other objects  

1. Browser Object Model (access using `window.property`)
2. Document Object Model (access using `document.property`)
3. Global Javascript Objects (access using `function.property`)
4. 
