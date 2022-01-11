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

componentDidMount allows us to execute the React code when the component has already been placed in the DOM.  
(Taken from [ReactJS componentDidMount() Method](https://www.geeksforgeeks.org/reactjs-componentdidmount-method))

### React State vs Props  
