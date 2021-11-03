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
