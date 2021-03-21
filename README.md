# Casting Agency API
# Introduction 
The Casting Agency API supports a basic casting agency by allowing users to query the database  for movies and actors.
There are three differents users roles (and related permissions), Which are:

- Casting Assistant
    - Can view actors and movies
- Casting Director
    - All permissions a Casting Assistant has and...
    - Add or delete an Actor from the database
    - Modify actors or movies
- Executive Producer
    - All permissions a Casting Director has and
    - Add or delete a movie from the database

# Motivation
- I developed this project to make use of the knowledge you acquired in this nanodegree and hence gain confidence in these skills.
## Capstone Project for Udacity's Full Stack Developer Nanodegree
Heroku Link: https://test-iden.herokuapp.com/

While running locally: http://localhost:5000
## Getting Started

### Installing Dependencies

#### Python 3.8.5

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Create and activate the virtual environment
```bash
python3 -m venv env
source env/bin/activate
```
#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in api.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

# Deploy to heroku
- Create app in heroku
- Set your environment variables
- Define your Procfile file
- Push your code to github
- Connect your repository to heroku
- Click on deploy option
## Running the server

First you have to start the postgresql service by running the following command
```bash
sudo service postgresql start
```
After that you have to create the database by running

```bash
sudo -u postgres psql
DROP DATABASE capstone;
CREATE DATABASE capstone;
```

From within the `./capstone` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export DATABASE_URL=postgresql://postgres:root@localhost:5432/capstone
export FLASK_APP=app.py
export AUTH0_DOMAIN='myauth-iden.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='capstone'
export CLIENT_ID='yskLRo0FodADDnqeN6dCzPa4QK0uD2bd'
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
    - `https://test-iden.herokuapp.com/actors`

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
    - `https://test-iden.herokuapp.com/actors/1`

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
    - `https://test-iden.herokuapp.com/actors`
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
    - `https://test-iden.herokuapp.com/actors/2`
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
   - `https://test-iden.herokuapp.com/actors/12`

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
    - `https://test-iden.herokuapp.com/movies`

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
   - `https://test-iden.herokuapp.com/movies/2`

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
    - `https://test-iden.herokuapp.com/movies`
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
   - `https://test-iden.herokuapp.com/movies/9`
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
   - `https://test-iden.herokuapp.com/movies/9`


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
dropdb capstone
createdb capstone
psql capstone < capstone.sql
python test.py
```