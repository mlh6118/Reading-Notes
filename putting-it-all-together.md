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


