## Local Storage

Original version for the web was the use of cookies.  
Drawbacks of cookies are:  
1. Included with each http request slowing the web application down by repetitive data transmission
1. Included with each http request sending unencrypted data over the internet
1. Limited to around 4KB of data

The desired solution would have:  
1. A lot of storage space  
1. Be on the client
1. Persist beyond a page refresh
1. Not transmitted to the server

HTML5 Storage:  
A way for web pages to store named key/value pairs locally, within the client web browser.  
Supported by every browser now.

To access HTML5 Storage:  
In JavaScript code, use `localStorage` on global `window` object.  

Using HTML5 Storage:  
named key - a string  
value - any data type supported by JavaScript  
  - Note that data is actually stored as a string.  
  - Non-string data needs to be coerced using things like parseInt() to put it back into the expected JavaScript datatype.
`setItem()` that uses a named key that already exists will overwrite the previous value.  
`getItem()` with a non-existent key will return `null`.

`localStorage` can be treated as an associative array.  
- May be written using square brackets instead of `getItem()` and `setItem()`.

Methods that exist
- `removeItem()` - removes the value for a given named key
- `clear()` - deletes all keys and values at once
- `readonly attribute unsighed long length;` - get total number of values in storage area
- `getter DOMString key(in unsigned long index);` - iterate through all of the keys by index

