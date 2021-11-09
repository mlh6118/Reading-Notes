## Transforms

Two different settings:
- Two-dimensional
- Three-dimensional

Syntax:
transform: property(amount);
-may include browser specific prefixes

2D Transforms:
- work on x (horizontal) and y (vertical) axes
- rotate - transform: rotate(15deg);
  - values may be positive or negative and between 0 and 360deg
- scale - transform: scale(.50);
  - a value of 1 is default scale
  - a value less than 1 will shrink the element
  - a value greater than 1 will enlarge the element
  - scaleX and scaleY may be used independently
- translate - transform: translate(15%, 15px);
  - works similar to relative positioning
  - x-axis is the first value in a value pair
  - positive values move element down and right
  - negative values move element up and left
- skew - transform: skew(15deg, -10deg);
  - x-axis is the first value in a value pair
  - only uses units of degrees
- transforms may be combined
  - separate the list of transforms without a comma between them
- origin - transform-origin: 0, 0;
  - moves the origin from the center of the element to wherever specified

3D Transforms:
- requires use of a perspective value
  - perspective value is similar to a drawing's vanishing point
  - transform: perspective(100px);
- can rotate element around an axis
  - transform: perspective(50px) rotateX(45deg);
  - positive values rotate clockwise
  - negative values rotate counter-clockwise
- no skew in 3D transforms

## Transitions

Four properties:
- transition-property
  - determines what will be changed
  - not all properties are available to transition
  - ex: transition-property: background, border-radius;
- transition-duration
  - can be done using various timing values
- transition-timing-function
  - sets the speed a transition will move
  - linear means moving in a constant speed
  - ease-in means starts slow and speeds up
  - ease-out means starts fast and slows down
  - ease-in-out means start slow, speed up, then slow down
- transition-delay
  - a time value in seconds or milliseconds before transition starts

- shorthand transitions
 - group multiple transitions on the same line
 - separate each group by a comma

 ## Animations

- use @keyframes rule
  - includes animation name, animation breakpoints, and properties to be animated
  - animations can only apply a transition within a single property (i.e., top to bottom will not work)
- may be iterated
  - animation-iteration-count: infinite;
- may be reversed in direction
- may be paused
