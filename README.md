# Hello world
# Casting Agency API
# Capstone project for udacity's full stack developer nanodegree

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

This will install all of the required packages we selected within the `requirements.txt` file.
# Error Handling
Errors are returned as JSON objects in the following format:

```json
{
    "error": 404,
    "message": "resource not found",
    "success": false
}
```
The API will return the following errors based on how the request fails:
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 404: Not Found
    - 405: Method Not Allowed
    - 422: Unprocessable Entity
    - 500: Internal Server Error


# Endpoints

#### GET /

- General
    - root endpoint
    - requires no authentication
- Sample Request
    - `http:my-app-heroku.com`

- Sample Response

```json
{
    "success": true,
    "message": "Healthy!!"
}
```


#### GET /actors

- General
    - Get all the actors
    - requires `get:actors` permission

- Sample Request
    - `http:my-app-heroku.com/actors`

- Sample Response

```json
{
    "actors": [
        {
            "created_at": "Thu, 18 Mar 2021 18:49:18 GMT",
            "gender": "male",
            "id": 1,
            "name": "Tobey"
        },
        {
            "created_at": "Thu, 18 Mar 2021 18:49:54 GMT",
            "gender": "female",
            "id": 2,
            "name": "Kirsten"
        },
        {
            "created_at": "Thu, 18 Mar 2021 18:50:05 GMT",
            "gender": "female",
            "id": 3,
            "name": "Rosemary"
        },
        {
            "created_at": "Thu, 18 Mar 2021 18:50:22 GMT",
            "gender": "male",
            "id": 4,
            "name": "Willen"
        },
        {
            "created_at": "Thu, 18 Mar 2021 19:26:34 GMT",
            "gender": "male",
            "id": 5,
            "name": "Robert"
        },
        {
            "created_at": "Thu, 18 Mar 2021 19:34:32 GMT",
            "gender": "male",
            "id": 6,
            "name": "Chris Evans"
        },
        {
            "created_at": "Thu, 18 Mar 2021 19:34:49 GMT",
            "gender": "male",
            "id": 7,
            "name": "Robert Downey"
        },
        {
            "created_at": "Thu, 18 Mar 2021 19:35:08 GMT",
            "gender": "female",
            "id": 8,
            "name": "Jennifer Lawrence"
        },
        {
            "created_at": "Thu, 18 Mar 2021 19:35:20 GMT",
            "gender": "female",
            "id": 9,
            "name": "Margot Robbie"
        },
        {
            "created_at": "Thu, 18 Mar 2021 19:35:49 GMT",
            "gender": "female",
            "id": 10,
            "name": "Scarlett Johansson"
        },
        {
            "created_at": "Thu, 18 Mar 2021 19:39:27 GMT",
            "gender": "male",
            "id": 11,
            "name": "Tom Holland"
        },
        {
            "created_at": "Thu, 18 Mar 2021 19:39:50 GMT",
            "gender": "male",
            "id": 12,
            "name": "Mark Ruffalo"
        }
    ],
    "success": true
}
```

#### GET /actors/{actor_id}

- General
    - Gets an specific actor
    - requires `get:actors-info` permission

- Sample Request
    - `http:my-app-heroku.com/actors/actors/1`

- Sample Response


```json
{
    "actor": {
        "created_at": "Thu, 18 Mar 2021 18:49:18 GMT",
        "gender": "male",
        "id": 1,
        "name": "Tobey"
    },
    "success": true
}

```

#### POST /actors
- General
    - Creates a new Actor
    - Requires `post:actor` permission
- Sample Request
    - `https://ry-fsnd-capstone.herokuapp.com/actors`
    - Request Body
    ```
        {
            "name":"Mark Ruffalo",
            "age": 53,
            "gender": "male" 
        }
    ```
- Sample Response

```json
{
    "created_actor": "Mark Ruffalo",
    "success": true,
    "total_actors": 12
}  
```

#### PATCH /actors/{actor_id}

- General
    - Updates the information for an actor
    - requires `patch:actors` permission

- Sample Request
    - `https://ry-fsnd-capstone.herokuapp.com/actors/2`
    - Request Body
    
    ```
        {
            "name":"Megan Fox",
            "age": 32,
            "gender": "female"
        }
    ```

- Sample Response

```json
{
    "patched_actor": 2,
    "success": true,
    "total_actors": 12
}
```

#### DELETE /actors/{actor_id}

 - General
   - deletes the actor
   - requires `delete:actors` permission
 
 - Sample Request
   - `https://ry-fsnd-capstone.herokuapp.com/actors/12`

 - Sample Response

```
{    
    "deleted": 12,
    "success": true,
    "total_actors": 11
}
```


#### GET /movies

- General
    - Gets the list of all movies
    - Requires `get:movies` permission

- Sample Request
    - `https://ry-fsnd-capstone.herokuapp.com/movies`

- Sample Response

```json
{
    "movies": [
        {
            "duration": 2,
            "id": 1,
            "release_year": 1976,
            "title": "kong I"
        },
        {
            "duration": 4,
            "id": 2,
            "release_year": 2005,
            "title": "spider man 3"
        },
        {
            "duration": 2,
            "id": 3,
            "release_year": 1998,
            "title": "Titanic"
        },
        {
            "duration": 3,
            "id": 4,
            "release_year": 2012,
            "title": "Avengers 1"
        },
        {
            "duration": 2,
            "id": 5,
            "release_year": 2015,
            "title": "Avengers 2"
        },
        {
            "duration": 2,
            "id": 6,
            "release_year": 1976,
            "title": "Rocky I"
        },
        {
            "duration": 2,
            "id": 8,
            "release_year": 2018,
            "title": "La hera del hielo"
        }
    ],
    "success": true
}
```
#### GET /movies/{movie_id}

- General
   - gets the information for a movie
   - requires `get:movies-info` permission
 
- Sample Request
   - `https://ry-fsnd-capstone.herokuapp.com/movies/2`

- Sample Response
```json
{
    "movie": {
        "duration": 4,
        "id": 2,
        "release_year": 2005,
        "title": "spider man 3"
    },
    "success": true
}
```


#### POST /movies
- General
    - creates a new movie
    - requires `post:movies` permission
 
- Sample Request
    - `https://ry-fsnd-capstone.herokuapp.com/movies`
    - Request Body
     ```
        {
            "title": "Robocop",
            "duration": 2,
            "release_year": 2015
        }
     ```

- Sample Response

```json
{
    "created_movie": 9,
    "success": true,
    "total_movies": 7
}
```


#### PATCH /movie/{movie_id}
 - General
   - updates the information for a movie
   - requires `patch:movies` permission
 
 
 - NOTE
   - Actors passed in the `cast` array in request body will completely replace the existing relationship.
   - So, if you want to append new actors to a movie, pass the existing actors also in the request.
 
 - Sample Request
   - `https://ry-fsnd-capstone.herokuapp.com/movies/9`
   - Request Body
     ```
       {
            "title": "Robocop II",
            "duration": 2,
            "release_year": 1990
       }
     ```


```json
{
    "success": true,
    "total_movies": 7,
    "updated_movie": 9
}
```
  

#### DELETE /movies/{movie_id}
 - General
   - deletes the movie with a given id
   - requires `delete:movies` permission
 
 - Sample Request
   - `https://ry-fsnd-capstone.herokuapp.com/movies/9`


```json
{
    "deleted": 9,
    "success": true,
    "total_movies": 6
}
```




## Testing
For testing the backend, run the following commands (in the exact order):
```
dropdb capstone_test
createdb capstone_test
psql capstone_test < casting.sql
python test.py
```