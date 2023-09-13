# Person-Resource Documentation
For installation, see [README.md](./README.md)

## POST - Create Person | /api
This is used to create a new person. Only a name is required in the body of the request and it must be unique.

### Sample URL
> https://person-resource-x.onrender.com/api

### Sample Body
>{
>    "name": "Daniel"
>}

### Sample Response
>Status: 201 Created

>{
>    "data": {
>        "user_id": 5,
>        "name": "Jane"
>    }
>}


## GET - Get Person | /api/{user_id}
This request is used to fetch a person using their user id.

### Sample URL
>https://person-resource-x.onrender.com/api/6

### Sample Response
>Status: 200 OK

>{
>    "data": {
>        "user_id": 5,
>        "name": "Cynthia"
>    }
>}

## PUT - Update Person | /api/{user_id}
This request is used to update a person identified using their user id. Enter the new name in the body of the request.

### Sample URL
>https://person-resource-x.onrender.com/api/6

### Sample Body
>{
>    "name": "Corleone"
>}

### Sample Response
> Status: 200 OK

>{
>    "data": {
>        "user_id": 5,
>        "name": "Mary"
>    }
>}


## DELETE - Delete Person | /api/{user_id}
This request is used to delete a person using their user id.

### Sample URL
> https://person-resource-x.onrender.com/api/7

### Sample Response
> Status: 204 No content