## CSS - Cascading Style Sheets

CSS is a language for document presentation specifications (i.e., aesthetics)

CSS is a rule-based language.
- Rules defined for styles to apply to elements on webpage.
  - Can apply to a particular element or groups of elements.

CSS Rules:
- Selector followed by curly braces { } with declarations inside the braces.
- Declarations are of the form "property: value".

To search for properties, use "mdn css-feature-name" in a search engine.

CSS is broken down into modules.  This allows for things related to be defined together.

CSS specifications are developed by W3C to ensure backwards compatibility.
- Adds new features asked for by developers.
- Adds something browsers are interested in having a capability of.
- Adds something because the group has identified a requirement.

Ways to use CSS:
1. External CSS - Document that requires a link within the page header to be used.  Contains all information desired for the styling of the page and can be used by multiple pages.
2. Internal CSS - Styles are defined at the top of the HTML page code within the /<head> code.  Can only be used by the page it is written within.
3. Inline CSS - Styles are defined at the point of use within the HTML page code.  Like Internal CSS, these cannot be used by other pages.

* It is important to note that a style that is read later will override the previous style.  For example, if a color is defined for text in an External CSS and within the calling page as an Internal CSS, the Internal CSS will be used.
