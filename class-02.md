# Process of Website Design

Before beginning to generate a website, one needs to go through the design process.  There are specific questions to ask oneself and answer:
- Who is the site for?  
  - Individuals?
  - Companies?
  - Both?
- Why are people going to visit the site?  
  - What are key motivations?  
  - What specific goals do they have?
- What are visitors trying to achieve?  
  - What info do they need?  
  - How often will they visit the site?

Once these questions are answered, a site map can be generated and card sorting to determine how the components of the website should be put together.

Following the site map generation, create a simple sketch of key info on each page called a wireframe.  These should not include anything that contains things like font, color schemes, and other "decorative" things.

Next should be organizing and prioritizing the various parts of the site map to help a visitor know how to read the page.  Because most users skim a page, there is a visual hierarchy requirement which refers to the order eyes perceive what they see.  Visual contrast is a key feature with a well-designed page being largely subliminal.  An element's size, color, and style all contribute to the visual hierarchy.  Grouping elements also makes a design easier to comprehend.

It is only after consideration of all of the above that any HTML, CSS, and JavaScript should be started.

## Basics of HTML, CSS, and JavaScript

**HTML**
HTML is used for setting up the content of a webpage.  There are two types of markups that make up HTML: structural and semantic.

Structural markup are the elements for headings and paragraphs.

Semantic markup provides extra info for the content, such as what should be emphasized in a sentence.

There are many different elements that can be used within HTML, but some common ones are:
* `<h#>`: 1 is the main heading of a page, 2 is a subheading, 3 is a subheading of 2, and so on.
* `<p>`: Denotes paragraphs and browsers default to putting space between each paragraph.
* `<b>` and `<i>`: Bold and italics.

It is important to note that browsers all treat white space the same: As a single space.  This means that two or more spaces, line breaks, etc., are collapsed into a single space when rendered on the screen.

**CSS**
CSS is used to create rules for how an element's content shall appear on webpage.

It is best to imagine a box around every HTML element when creating CSS.

Multiple elements may have the same style and only need the selectors (how elements are referred to) to be separated by a comma (,).