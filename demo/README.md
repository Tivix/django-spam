## Demo using django-spam

This demo is provided as a convenience feature to allow potential users to try the app straight from the app repo without having to create a django project.

It can also be used to develop the app in place.

To run this example, follow these instructions:

1. Navigate to the `demo` directory

2. Install required packages with Poetry.

		poetry install
	
3. Make and apply migrations

		poetry run python manage.py makemigrations
		
		poetry run python manage.py migrate
		
4. Run the server

		poetry run python manage.py runserver
		
4. Access from the browser at `http://127.0.0.1:8000`
