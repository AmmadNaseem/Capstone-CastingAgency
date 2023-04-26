# FSND: Capstone Project Casting Project

## Content

1. [Motivation](#motivation)
2. [Start Project locally](#start-locally)
3. [API Documentation](#api)
4. [Authentification](#authentification)
5. [Unit testing](#unittesting)

## Motivations & Covered Topics

This is the last project of the `Udacity-Full-Stack-Nanodegree` Course.
It covers following technical topics in 1 app:

1. Database modeling with `postgres` & `sqlalchemy` (see `models.py`)
2. API to performance CRUD Operations on database with `Flask` (see `app.py`)
3. Automated testing with `Unittest` (see tests folder `test_app`)
4. Authorization & Role based Authentification with `Auth0` (see in auth folder `auth.py`)
5. Deployment on `Heroku`

## Start Project locally

Make sure you `cd` into the correct folder (with all app files) before following the setup steps.
Also, you need the latest version of [Python 3](https://www.python.org/downloads/)
and [postgres](https://www.postgresql.org/download/) installed on your machine.

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```bash
  $ virtualenv --no-site-packages env_capstone
  $ source env_capstone/scripts/activate
  ```

2. Install the dependencies:
```bash
$ pip install -r requirements.txt
```

3. Database creation using migration: set this in model.py
  DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
  DB_USER = os.getenv('DB_USER', 'postgres')
  DB_PASSWORD = os.getenv('DB_PASSWORD', '')
  DB_NAME = os.getenv('DB_NAME', 'capstone')
  database_path = "postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)


4. Setup Auth0
  If you only want to test the API (i.e. Project Reviewer) :Below link used for creating the tokens.
  https://fullstacknanodegreeaamad.us.auth0.com/authorize?audience=castingApi&response_type=token&client_id=fiAGHWKtEF8eIjMysUqYQpvVjrSB0Mmh&redirect_uri=http://localhost:4200/login-results

  ### Using These credential you can create tokens:
    1. castingassistant@gmail.com
    2. castingdirector@gmail.com
    3. executiveproducer@gmail.com
    4. Password: RVTDKTAk9n82dHn


5. Run the development server:
  ```bash 
  1. export FLASK_APP=app.py
  2. flask run
  ```



## API Documentation

### Base URL

**http://127.0.0.1:5000**

### Available Endpoints

Here is a short table about which ressources exist and which method you can use on them.

                          Allowed Methods
       Endpoints    |  GET |  POST |  DELETE | PATCH  |
                    |------|-------|---------|--------|
      /actors       |  [x] |  [x]  |   [x]   |   [x]  |   
      /movies       |  [x] |  [x]  |   [x]   |   [x]  |   

### How to work with each endpoint

Click on a link to directly get to the ressource.

1. Actors
   1. [GET /actors](#get-actors)
   2. [POST /actors](#post-actors)
   3. [DELETE /actors](#delete-actors)
   4. [PATCH /actors](#patch-actors)
2. Movies
   1. [GET /movies](#get-movies)
   2. [POST /movies](#post-movies)
   3. [DELETE /movies](#delete-movies)
   4. [PATCH /movies](#patch-movies)

Each ressource documentation is clearly structured:
1. Description in a few words
2. `curl` example that can directly be used in terminal
3. More descriptive explanation of input & outputs.
4. Required permission
5. Example Response.
6. Error Handling (`curl` command to trigger error + error response)

### 1. GET /actors

Query paginated actors.

```bash
$ curl -X GET http://127.0.0.1:5000/actors?page1
```
- Fetches a list of dictionaries of examples in which the keys are the ids with all available fields
- Request Arguments: 
    - **integer** `page` (optional, 10 actors per page, defaults to `1` if not given)
- Request Headers: **None**
- Requires permission: `read:actors`
- Returns: 
  1. List of dict of actors with following fields:
      - **integer** `id`
      - **string** `name`
      - **string** `gender`
      - **integer** `age`
  2. **boolean** `success`

#### Example response
```js
{
  "actors": [
    {
      "age": 25,
      "gender": "Male",
      "id": 1,
      "name": "Matthew"
    }
  ],
  "success": true
}
```
#### Errors
If you try fetch a page which does not have any actors, you will encounter an error which looks like this:

```bash
$ curl -X GET http://127.0.0.1:5000/actors?page123124
```

will return

```js
{
  "error": 404,
  "message": "no actors found in database.",
  "success": false
}
```

### 2. POST /actors

Insert new actor into database.

```bash
$ curl -X POST http://127.0.0.1:5000/actors
```

- Request Arguments: **None**
- Request Headers: (_application/json_)
       1. **string** `name` (<span style="color:red">*</span>required)
       2. **integer** `age` (<span style="color:red">*</span>required)
       3. **string** `gender`
- Requires permission: `create:actors`
- Returns: 
  1. **integer** `id from newly created actor`
  2. **boolean** `success`

#### Example response
```js
{
    "created": 1,
    "success": true
}

```
#### Errors
If you try to create a new actor without a requiered field like `name`,
it will throw a `422` error:

```bash
$ curl -X GET http://127.0.0.1:5000/actors?page123124
```

will return

```js
{
  "error": 422,
  "message": "no name provided.",
  "success": false
}
```

### 3. PATCH /actors

Edit an existing Actor

```bash
$ curl -X PATCH http://127.0.0.1:5000/actors/1
```

- Request Arguments: **integer** `id from actor you want to update`
- Request Headers: (_application/json_)
       1. **string** `name` 
       2. **integer** `age` 
       3. **string** `gender`
- Requires permission: `edit:actors`
- Returns: 
  1. **integer** `id from updated actor`
  2. **boolean** `success`
  3. List of dict of actors with following fields:
      - **integer** `id`
      - **string** `name`
      - **string** `gender`
      - **integer** `age`

#### Example response
```js
{
    "actor": [
        {
            "age": 30,
            "gender": "Other",
            "id": 1,
            "name": "Test Actor"
        }
    ],
    "success": true,
    "updated": 1
}
```
#### Errors
If you try to update an actor with an invalid id it will throw an `404`error:

```bash
$ curl -X PATCH http://127.0.0.1:5000/actors/125
```

will return

```js
{
  "error": 404,
  "message": "Actor with id 125 not found in database.",
  "success": false
}
```
Additionally, trying to update an Actor with already existing field values will result in an `422` error:

```js
{
  "error": 422,
  "message": "provided field values are already set. No update needed.",
  "success": false
}
```

### 4. DELETE /actors

Delete an existing Actor

```bash
$ curl -X DELETE http://127.0.0.1:5000/actors/1
```

- Request Arguments: **integer** `id from actor you want to delete`
- Request Headers: `None`
- Requires permission: `delete:actors`
- Returns: 
  1. **integer** `id from deleted actor`
  2. **boolean** `success`

#### Example response
```js
{
    "deleted": 5,
    "success": true
}

```
#### Errors
If you try to delete actor with an invalid id, it will throw an `404`error:

```bash
$ curl -X DELETE http://127.0.0.1:5000/actors/125
```

will return

```js
{
  "error": 404,
  "message": "Actor with id 125 not found in database.",
  "success": false
}
```

### 5. GET /movies

Query paginated movies.

```bash
$ curl -X GET http://127.0.0.1:5000/movies?page1
```
- Fetches a list of dictionaries of examples in which the keys are the ids with all available fields
- Request Arguments: 
    - **integer** `page` (optional, 10 movies per page, defaults to `1` if not given)
- Request Headers: **None**
- Requires permission: `read:movies`
- Returns: 
  1. List of dict of movies with following fields:
      - **integer** `id`
      - **string** `name`
      - **date** `release_date`
  2. **boolean** `success`

#### Example response
```js
{
  "movies": [
    {
      "id": 1,
      "release_date": "Sun, 16 Feb 2020 00:00:00 GMT",
      "title": "Matthew first Movie"
    }
  ],
  "success": true
}

```
#### Errors
If you try fetch a page which does not have any movies, you will encounter an error which looks like this:

```bash
$ curl -X GET http://127.0.0.1:5000/movies?page123124
```

will return

```js
{
  "error": 404,
  "message": "no movies found in database.",
  "success": false
}
```

### 6. POST /movies

Insert new Movie into database.

```bash
$ curl -X POST http://127.0.0.1:5000/movies
```

- Request Arguments: **None**
- Request Headers: (_application/json_)
       1. **string** `title` (<span style="color:red">*</span>required)
       2. **date** `release_date` (<span style="color:red">*</span>required)
- Requires permission: `create:movies`
- Returns: 
  1. **integer** `id from newly created movie`
  2. **boolean** `success`

#### Example response
```js
{
    "created": 5,
    "success": true
}
```
#### Errors
If you try to create a new movie without a requiered field like `name`,
it will throw a `422` error:

```bash
$ curl -X GET http://127.0.0.1:5000/movies?page123124
```

will return

```js
{
  "error": 422,
  "message": "no name provided.",
  "success": false
}
```

### 7. PATCH /movies

Edit an existing Movie

```bash
$ curl -X PATCH http://127.0.0.1:5000/movies/1
```

- Request Arguments: **integer** `id from movie you want to update`
- Request Headers: (_application/json_)
       1. **string** `title` 
       2. **date** `release_date` 
- Requires permission: `edit:movies`
- Returns: 
  1. **integer** `id from updated movie`
  2. **boolean** `success`
  3. List of dict of movies with following fields:
        - **integer** `id`
        - **string** `title` 
        - **date** `release_date` 

#### Example response
```js
{
    "created": 1,
    "movie": [
        {
            "id": 1,
            "release_date": "Sun, 16 Feb 2020 00:00:00 GMT",
            "title": "Test Movie 123"
        }
    ],
    "success": true
}

```
#### Errors
If you try to update an movie with an invalid id it will throw an `404`error:

```bash
$ curl -X PATCH http://127.0.0.1:5000/movies/125
```

will return

```js
{
  "error": 404,
  "message": "Movie with id 125 not found in database.",
  "success": false
}
```
Additionally, trying to update an Movie with already existing field values will result in an `422` error:

```js
{
  "error": 422,
  "message": "provided field values are already set. No update needed.",
  "success": false
}
```

### 8. DELETE /movies

Delete an existing movie

```bash
$ curl -X DELETE http://127.0.0.1:5000/movies/1
```

- Request Arguments: **integer** `id from movie you want to delete`
- Request Headers: `None`
- Requires permission: `delete:movies`
- Returns: 
  1. **integer** `id from deleted movie`
  2. **boolean** `success`

#### Example response
```js
{
    "deleted": 5,
    "success": true
}

```
#### Errors
If you try to delete movie with an invalid id, it will throw an `404`error:

```bash
$ curl -X DELETE http://127.0.0.1:5000/movies/125
```

will return

```js
{
  "error": 404,
  "message": "Movie with id 125 not found in database.",
  "success": false
}
```

# Authentification

All API Endpoints are decorated with Auth0 permissions. To use the project locally, you need to config Auth0 accordingly

### Auth0 for locally use
#### Create an App & API

1. Login to https://DOMAAIN.auth0.com/ 
2. Click on Applications Tab
3. Create Application
4. Give it a name like `Music` and select "Regular Web Application"
5. Go to Settings and find `domain`. Copy & paste it into config.py => auth0_config['AUTH0_DOMAIN'] (i.e. replace `"example.eu.auth0.com"`)
6. Click on API Tab 
7. Create a new API:
   1. Name: `Music`
   2. Identifier `Music`
   3. Keep Algorithm as it is
8. Go to Settings and find `Identifier`. Copy & paste it into config.py => auth0_config['API_AUDIENCE'] (i.e. replace `"Example"`)

#### Create Roles & Permissions

1. Before creating `Roles & Permissions`, you need to `Enable RBAC` in your API (API => Click on your API Name => Settings = Enable RBAC => Save)
2. Also, check the button `Add Permissions in the Access Token`.
2. First, create a new Role under `Users and Roles` => `Roles` => `Create Roles`
3. Give it a descriptive name like `Casting Assistant`.
4. Go back to the API Tab and find your newly created API. Click on Permissions.
5. Create & assign all needed permissions accordingly 
6. After you created all permissions this app needs, go back to `Users and Roles` => `Roles` and select the role you recently created.
6. Under `Permissions`, assign all permissions you want this role to have. 


## Existing Roles

They are 3 Roles with distinct permission sets:

1. Casting Assistant:
  - GET /actors (view:actors): Can see all actors
  - GET /movies (view:movies): Can see all movies
2. Casting Director (everything from Casting Assistant plus)
  - POST /actors (create:actors): Can create new Actors
  - PATCH /actors (edit:actors): Can edit existing Actors
  - DELETE /actors (delete:actors): Can remove existing Actors from database
  - PATCH /movies (edit:movies): Can edit existing Movies
3. Exectutive Dircector (everything from Casting Director plus)
  - POST /movies (create:movies): Can create new Movies
  - DELETE /movies (delete:movies): Can remove existing Motives from database

In your API Calls, add them as Header, with `Authorization` as key and the `Bearer token` as value. Don´t forget to also
prepend `Bearer` to the token (seperated by space).

For example: (Bearer token for `Executive Director`)
```js
 {
  'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
 }
For example: (Bearer token for `casting assisitant`)
```js
{
  'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzYTNlMTExOGRhODNmZjFhNGZlIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2OTA4MSwiZXhwIjoxNjgwMTc2MjgxLCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.DC4GE1mvpmxkVHnM2hog_3AZyrUI7xWTESOF0OPZg7VkXC5YoG9ea6JH2WPuRMn8yJcAFCtB1sWJ56C2NMVJThqN9b1k9yIHV84jARvbgnQ8CYpwcgogmt_PGfhE8N6IoyhR_flw3ZIiXJcnEYhl65OMV4O9kIldJMak1_yl7d5J0IZz3c34zxxKvRXh3g-YA52QTKCiQ-bruMFOwKXzegW8s4-l-QlEQLFt3tgK0g81H36O5fM8l4iVm0cVzrXTmQCLBcqCGccp5k0_XWny5ufWvSqdhZtZ8vih4ASTaXCnqIf9uQxkOy-LM4jeoIyLv5Z-IAcjGmxcke8UeUXj0A"
  
}

```

# Unit testing
#### How to run unit test of apis?

1. cd tests [go to the test folder]: add below string in main.py
      DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
      DB_USER = os.getenv('DB_USER', 'postgres')
      DB_PASSWORD = os.getenv('DB_PASSWORD', '')
      DB_NAME = os.getenv('DB_NAME', 'test_capstone')
      database_path = "postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

##### Using these we will set the separate test database

2. export FLASK_APP=main.py
3. flask db init 
4. flask db migrate
5. flask db upgrade
6. To execute tests, run
```bash 
$ python test_app.py
```
If you choose to run all tests, it should give this response if everything went fine:

```bash
$ python test_app.py
.................
----------------------------------------------------------------------
Ran 17 tests in 3.813s

OK
```

# Developed By Aamad Naseem




