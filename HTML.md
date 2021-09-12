## Wireframes

- Black and white
- Basic block sketch of major elements and their alignment on page
- Easy to distribute to team members
- Easy to modify
- Purpose:
  - Clarity
  - Confidence
  - Simplicity

### 6 Steps to making a wireframe

1. Do research.
    1. Who is audience?
    1. What are requirements?
    1. What are use cases?
1. Prepare research for quick reference.
    1. Research data notes collated.
    1. Cool features on competitor sites.
    1. Choice quotes from audience for user's experiences.
1. Make sure user flow is mapped out.
    - How to get from one place to another and back.
1. Draft, don't draw.  Sketch, don't illustrate.
    - Ask following questions while doing this:
        1. How does organization support users' goals?
        1. Which info should be prominent and where?
        1. What will be expected on certain areas of page from user standpoint?
        1. What buttons/touch points are needed to completed desired actions?
1. Add some detail and test.
    1. Add from top to bottom, left to right.
    1. Adding content and copy, still high level.
    1. Consider:
        1. Usability conventions (e.g., navigation at top, search box on top right)
        1. Easy to follow text
        1. Elements to build trust with users
        1. Tooltips to indicate functionality
    1. Perform user tests (likely with colleagues).
1. Turn wireframes into prototypes.

## HTML Basics

1. HTML stands for Hypertext Markup Language.
1. HTML defines structure of content.
    1. Consists of elements (tags).
        1. Elements consist of opening tag, content, and closing tag.
            - Tags are enclosed in angle brackets \< \>.
            - Closing tags require a forward slash \/ before the element name.
    1. Attributes which are extra information that isn't actual content.
        - Attributes contain
            - Attribute name
            - An equal sign =
            - Attribute value </br>
                Example: \<p font="Helvetica"\>
    1. Nesting elements
        - Elements that go inside of other elements.
        - Must be closed prior to the closing of the element it is contained within.
    1. Empty elements
        - Have no content and no closing tag.
1. Anatomy of an HTML document
    - \<!DOCTYPE html>
    - \<html><\/html>
      - Wraps all content of page
      - Known as root element
    - \<head><\/head>
      - Container for items on page that isn't content
        - Includes:
          - Keywords
          - Page description
          - CSS
    - \<meta charset="utf-8>
      - Character set that includes most characters from majority of written languages.
    - \<title><\/title>
      - Appears at top of tab in browser.
      - Used as default for bookmark/favorite description.
    - \<body><\/body>
      - Contains all web page content to view.
    - \<img>
      - Used to add pictures to pages.
      - 'alt=" "' adds text for visually impaired screen readers.
    - \<h#>
      - Headings where the size is dictated by the number that replaces the # in the tag.
    - Lists
      - \<ul><\/ul>
        - Unordered lists that are shown with bullet points.
      - \<ol><\/ol>
        - Ordered lists that are numbered.
      - Each item inside either type of list requires the \<li><\/li> tags.
    - \<a><\/a>
      - Links to a given site.  Typically used with 'href="website.html"'.
    