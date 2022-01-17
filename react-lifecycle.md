# State and Props

### React Lifecycle  
In the React lifecycle, 'componentDidMount' has to come before 'render'.  
The very first thing that happens in the React lifecycle is the call for a constructor.  This is required to occur prior to mounting.

The basic steps of the React lifecycle occur in the following order:  
* constructor
* render
* componentDidMount
* React updates
* componentWillUnmount
(Taken from [React: Component Lifecycle Events](https://medium.com/@joshuablankenshipnola/react-component-lifecycle-events-cb77e670a093))

componentDidMount allows us to execute the React code when the component has already been placed in the DOM.  
(Taken from [ReactJS componentDidMount() Method](https://www.geeksforgeeks.org/reactjs-componentdidmount-method))

### React State vs Props  

1. What types of things can you pass in the props?  
Props are passed to the component similar to how an argument is passed to a function.  This means that anything that will remain static within the component may be passed in via props.

2. What is the big difference between props and state?  
State is contained within a component while props are used to pass data from one component to another.  Props are also read-only, cannot be modified, and are immutable.  State, on the other hand, can be modified and is mutable.

3. When do we re-render our application?  
Applications are re-rendered after we use setState to change the value of the variable in state.

4. What are some examples of things that we could store in state?  
Examples of what could be stored in state are data that may be a string, number, or object.
(Taken from [When it's not good to use state for storing data in React](https://blog.devgenius.io/when-its-not-good-to-use-state-for-storing-data-in-react-adcf261e8467))
