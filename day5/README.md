# Day 5

## Reference

  - Flask https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
  - Example app https://gist.github.com/sanspace/55fcf6c9df922abbdafb830f102b7135
  - Review request.method and request.json properties
  - Flask RESTful - https://flask-restful.readthedocs.io/en/latest/index.html
  - Pipenv https://docs.python-guide.org/dev/virtualenvs/ (refer only pipenv in this page, you don't need to know other lower level tools for now)

  You don't have to know all these right now. But, this would makes it so much easier for testing during your API development and even after.

  - Postman https://www.postman.com/use-cases/api-first-development/
  - Requests https://requests.readthedocs.io/en/master/
  - Curl https://ec.haxx.se/http/http-basics

## Research

  - MongoDB and the diff between Relational and NOSQL databases
  - psycopg - python db adapter for Postgres
  - What an ORM is?
  - SQLAlchemy - ORM for Python

## Practice

  - Create a REST API with flask
    - use venv and pip to manage your packages for this project
    - create collection and resource endpoints for your use case
      - support appropriate HTTP methods
      - respond with appropriate HTTP codes
    - create tests using pytest and requests to test these endpoints
  - Create a REST API with flask-restful
    - use pipenv to manage your venv and packages
    - create collection and resource endpoints for your use case
      - support appropriate HTTP methods
      - respond with appropriate HTTP codes
    - run the tests using pytest that was created earlier

### Deliverables

You should have 3 github repos as the deliverable for these

  1. Flask API
  2. Flask Restful API
  3. Pytest tests
