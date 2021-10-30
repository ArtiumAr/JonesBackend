# JonesBackend

Backend API for the Jones restauraunt.

To run in development do the following:

- Clone repo.
- Cd into the directory, with Pipenv installed run the following command: pipenv install
- rename dev.env to .env. Optional and highly recommended: use your own securely generated SECRET_KEY and plug it into the .dev file.
- Go into the pipenv shell with: pipenv shell
- run the Flask server with: flask run


To run the tests use: pytest -v 
