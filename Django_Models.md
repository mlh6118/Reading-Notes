# Django Models

Django models define the structure of stored data, including field types, 
 defaults, and options.

The model definition is independent of the underlying database.

Models are usually defined in an applications models.py file.

A model should have a class method __str__() to return a human-readable 
 string for each object.

Once models have been created (or updated), the database migrations need to 
 be re-run.
- python3 manage.py makemigrations
- python3 manage.py migrate