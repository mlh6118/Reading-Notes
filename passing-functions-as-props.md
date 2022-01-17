# Passing Functions as Props

### Lists and Keys  
1. What does a .map() return?  
A .map() returns a new array equal to the number of elements in the original array.

2. If I want to loop through an array and display each value in JSX, how do I do that in React?  
To loop through an array and display each value in JSX in React, a .map of the array should be used with the return element contained within curly braces ('{ }').

3. Each list item needs a unique ____?  
Key. These need to be unique within the same array, but not globally.

4. What is the purpose of a key?  
Keys help React identify which items have changed, are added, or are removed.  Keys are also used to give elements within the array a stable identity.  It is recommended to not use an element's index as the key due to the fact that the order of most items may change while running a code.

### The Spread Operator  
1. What is the spread operator?  
The spread operator is an ellipsis (...) to expand an iterable object into the list of arguments.

2. List 4 things that the spread operator can do.  
The spread operator is useful for many routine tasks including:  
* Using Math functions  
* Adding an item to a list  
* Adding to state in React  
* Combining objects  

3. Give an example of using the spread oeprator to combine two arrays.  
```
const firstArray =['This', 'land', 'is', 'my', 'land.'];
const secondArray = ['This', 'land', 'is', 'your', 'land.'];
const fullArray = [...firstArray,...secondArray];
console.log(...fullArray);
```

4. Give an example of using the spread operator to add a new item into an array.  
```
const wordList = ['React', 'JSX', 'state', 'props'];
const moreWordsList = ['list', 'key', 'spread', ...wordList];
console.log(moreWordsList);
```

5. Give an example of using the spread operator to combine two objects into one.  
```
let senate = {
  state: 'California',
  name: 'Barbara Boxer'
};

let house = {
  state: 'California',
  name: 'Brad Sherman'
};

let congress = {
  ...senate,
  ...house
};
```

### Passing Functions Between Components   
1. The first step to pass functions between components is to create the function within the same location as the state exists.

2. The increment function takes in a name, compares it to the names within the array, and if the name is found, it will add one to the existing count, and set the state with the new count.

3. A method from a parent component may be passed to a child by using `functionName = {this.functionName}`.

4. The child component invokes a method passed to it from a parent component by using `this.props.functionName(this.props.propertyName)`.
