# Putting it All Together   

### React Docs - Thinking in React   
1. What is the single responsibility principle and how does it apply to components?   
A compnent should only do one thing.  If it grows, it should be decomposed into smaller subcomponents.

2. What does it mean to build a 'static' version of your application?   
A staic version of the application is one that has the data model and renders the UI, but has no interactivity.

3. Once you have a static application, what do you need to ad?   
Once the static application is built, interactivity needs to be added using state.

4. What are the three questions you can ask to determine if something is state?   
* Is it passed in from a parent via props?  If so, it probably isn't state.  
* Does it remain unchanged over time?  If so, it probably isn't state.  
* Can you compute it based on any other state or props in your component?  If so, it isn't state.

5. How can you identify where state needs to live?   
* Identify every component that renders something based on that state.  
* Find a common owner component (a single component above all the components that need the state in the hierarchy).  
* Either the common owner or another higher up in the hierarchy should own the state.
* If no component makes sense to own the state, create a new component solely for holding the state and add it somewhere in the hierarchy above the common owner component.

(Taken from [Thinking in React](https://reactjs.org/docs/thinking-in-react.html))

### Higher-Order Functions  
1. What is a "higher-order function"?  
Higher-order functions are functions that operate on other functions, either by taking them as arguments or by returning them.  

2. Explore the `greaterThan` function as defined in the reading.  What is line 2 of the function doing?  
Line 2: `return m => m > n;`  
This is taking a value that is passed in as "n" and checking if it is great than a value called "m".

3. Explain how either `map` or `reduce` oeprates with regard to higher-order functions.  
The map method transforms an array by applying a function to all of its elements and building a new array from the returned values.  The new array will have the same length as the input array, but its content will have been mapped to a new form by the function.

(Taken from [Chapter 5: Higher-Order Functions](https://eloquentjavascript.net/05_higher_order.html#h_xxCc98lOBK))
