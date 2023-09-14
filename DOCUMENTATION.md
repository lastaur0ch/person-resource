# Person-Resource Documentation
For installation, see [README.md](./README.md)

## Create a Person
This is used to create a new person. Only a name is required in the body of the request and it must be unique.
**Method**: POST
**Path**: /api

### Sample URL
> https://person-resource-x.onrender.com/api

### Sample Body
>{
>    "name": "Daniel"
>}

### Sample Response
> **Status**: 201 Created

>{
>    "data": {
>        "user_id": 5,
>        "name": "Daniel"
>    }
>}


##  Get a Person

This request is used to fetch a person using their user id.
**Method**: GET
**Path**: /api/{user_id}
### Sample URL
>https://person-resource-x.onrender.com/api/Daniel

### Sample Response
> **Status**: 200 OK

>{
>    "data": {
>        "user_id": 5,
>        "name": "Daniel"
>    }
>}

## Update Person

This request is used to update a person identified using their user id. Enter the new name in the body of the request.
**Method**: PUT
**Path**: /api/{user_id}

### Sample URL
>https://person-resource-x.onrender.com/api/Daniel

### Sample Body
>{
>    "name": "John"
>}

### Sample Response
> **Status**: 200 OK

>{
>    "data": {
>        "user_id": 5,
>        "name": "John"
>    }
>}


## Delete Person
This request is used to delete a person using their user id.
**Method**: DELETE
**Path**: /api/{user_id}

### Sample URL
> https://person-resource-x.onrender.com/api/John

### Sample Response
> **Status**: 204 No content


## Schema

### Person
- **name**: string, unique (required)
- **id**: integer (generated)
- **created_at**: timestamp (generated)