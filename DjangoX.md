# DjangoX

DjangoX is a Django project that has been built out with a lot of stuff 
already implemented within it.  (The author of the code refers to this as 
"A batteries-included Django starter project.")  One thing that does need 
to be handled for security purposes is how someone will log in to the site 
that is deployed.  This is done using a Custom User Model.  One needs to:
1. perform a setup
2. update django_project/settings.py
3. create a new CustomUser model
4. create new UserCreation and UserChangeForm
5. update the admin

All of the instructions for this can be found at [Django Best Practices: 
 Custom User Model](https://learndjango.com/tutorials/django-custom-user-model).