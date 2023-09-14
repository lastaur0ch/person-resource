# person-resource

## Installation

### Clone repository
> git clone https://github.com/lastaur0ch/person-resource.git
> cd person-resource

### Create virtual environment
> py -m venv venv
> .\venv\Scripts\activate

### Install requirements
> pip install -r requirements.txt

### Start server
> uvicorn app.main:app


## Sample Requests

### Create a person

> curl -X POST -H "Content-Type: application/json" -d '{"name": "John Wick"}' http://127.0.0.1:8000/api

### Fetch a person

> curl http://127.0.0.1:8000/api/John%20Wick

### Update a person

> curl -X PUT -H "Content-Type: application/json" -d '{"name": "Keanu Reeves"}' http://127.0.0.1:8000/api/John%20Wick

### Remove a person

> curl -X DELETE http://127.0.0.1:8000/api/Keanu%20Reeves

## Testing 

You can test the following requests using python script, postman or swagger:
- Adding a new person
- Fetching details of a person
- Modifying the details of an existing person
- Removing a person

### Using Pytest
> pytest

### Using Postman
Import and run the [postman collection file](HNGx-jjxavier-2.postman_collection.json). Each request includes a test.
### Swagger
> https://person-resource-x.onrender.com/docs

## Documentation
See [DOCUMENTATION.md](./DOCUMENTATION.md)