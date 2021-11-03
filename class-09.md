## Events

- Fired or raised - event has occurred.
- Trigger scripts

### Event Handling

3 Steps:
1. Select the element node(s) the script should respond to.
1. Indicate which event on selected node will trigger response (referred to as building an event to a DOM node).
1. State code to run when event occurs.

3 Types of Event Handlers:
1. HTML Event Handlers (now considered bad practice)
1. Traditional DOM Event Handlers  
  - only attach a single function to an event
1. DOM Level 2 Event Listeners (preferred way to handle events)  
  - can allow one event to trigger multiple functions
  
#### Traditional DOM Event Handlers

Format: element.event = code  
  `element.onevent = functionName;`  
  Ex: `el.onblur = checkUsername;`  
  - element = DOM element node to target  
  - event = event bound to nodes preceded by word "on"  
  - code = name of function to call without parens after  
    - adding parens after would cause code to run immediately
    
#### Event Listeners

Can deal with more than one function at a time  
Format: `element.method(event, code, event flow);`  
  - element = DOM node to target  
  - method = adds event listener to DOM element node  
  - event = event to bind node to  
  - code = name of function to call  
  - event flow = indicates something called capture, usually set to false
  
  generic example: `element.addEventListener('event', functionName, [boolean]);`  
  specific example: `el.addEventListener('blur', checkUsername, false);  
    - parens omitted from function call  
    - removeEventListener() does the opposite of addEventListener()
    
  passing arguments requires workaround  
  - use an anonymous function around named function with arguments  
  Ex: ```
  el.addEventListener('blur', function(){  
    checkUsername(5);  
  }, false);
  ```
