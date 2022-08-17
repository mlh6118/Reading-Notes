# Django CRUD and Forms
Forms are groups of one or more fields/widgets on a web page to collect info 
from users for submission to a server.  Forms are a relatively secure way of 
sharing data with the server in POST requests with cross-site request 
forgery (csrf) protection.  

Django forms take a lot of work out of all the steps needed to write HTML 
for them that would be required by writing HTML code directly.  It does this 
by doing the following:
1. Display the default form the first time it is requested by the user.
2. Receive data from a submit request and bind it to the form.
3. Clean and validate the data.
4. If any data is invalid, re-display the form, this time with any user 
   populated values and error messages for the problem fields.
5. If all data is valid, perform required actions.
6. Once all actions are complete, redirect the user to another page.

Like creating a basic page in Django, there are certain steps that need to 
be done (in any order) for adding a form.
1. Add a forms.py file which needs to include:
   1. The Form declaration which is similar to that of a Model.
   2. Create the class to use the form.
   3. Add the form fields that are needed.
   4. Add data validation.
2. Add the path to the application urls.py file.
3. Add the form to the views.py file.
4. Create the template file.

Django provides generic editing views for creating, editing, and deleting 
views based on models.  These are, respectively, CreateView, UpdateView, and 
DeleteView.

##### Source: [Django Tutorial Part 9: Working with forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
