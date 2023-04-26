from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import *
import json
from auth.auth import AuthError, requires_auth
from flask_cors import CORS

NUMBER_OF_ROWS_PER_PAGE=10


def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.after_request
  def requested_header(response):
        response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,DELETE,OPTIONS')
        return response


  def paginate_results(request, selection):
        page = request.args.get('page', 1, type=int)
        per_page = NUMBER_OF_ROWS_PER_PAGE

        start = (page - 1) * per_page
        end = start + per_page

        objects_formatted = [object_name.format() for object_name in selection]
        paginated_objects = objects_formatted[start:end]

        return paginated_objects



    # ===============ROUTES
  @app.route('/', methods = ['GET'])
  def index():

      return jsonify({
          'success': True,
          'message':'Backend of Capstone casting project is  Successfully connected.'})



    #==================ROUTES FOR ACTORS=================
  @app.route('/actors', methods=['GET'])
  @requires_auth('view:actors')  
  def get_actors(jwt):
      selection = Actor.query.all()
      actors_paginated = paginate_results(request, selection)

      if not actors_paginated:
        abort(404, {'message': 'No actors found.'})

      return jsonify({
          'success': True,
          'actors': actors_paginated
      })


  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def add_actors(jwt):
    body = request.get_json()

    if not body:
          abort(400)

    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', 'Other')
    
    if not name:
        abort(422, {'message': 'please enter name.'})

    if not age:
        abort(422, {'message': 'please enter age.'})
  
    try:
        actor = Actor(name,gender,age)
        actor.insert()

    except Exception as e:
        abort(422,{'message': {'message': str(e)}})

    return jsonify(
      {
          'success': True,
          'created': actor.id
      })


  @app.route('/actors/<actor_id>', methods=['PATCH'])
  @requires_auth('update:actors')
  def update_actors(jwt,actor_id):
    body = request.get_json()

    if not actor_id:
        abort(400, {'message': 'please append an actor id to the request url.'})

    if not body:
        abort(400, {'message': 'request does not contain a valid JSON body.'})

    findActor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    
    if findActor is None:
          abort(404,{'message': 'Actor with id {} not found in database.'.format(actor_id)})
      
    try:
        name = body.get('name',findActor.name)
        age = body.get('age',findActor.age)
        gender = body.get('gender',findActor.gender)
        movie_id = body.get('movie_id',findActor.movie_id)


        findActor.name = name
        findActor.age = age
        findActor.gender = gender
        findActor.movie_id = movie_id

        findActor.update()

    except Exception as e:
        abort(422,{'message': str(e)})

    return jsonify({
          'success': True,
          'updated': findActor.id,
          'actor' : [findActor.format()]
        })


  @app.route('/actors/<actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(jwt,actor_id):
    body = request.get_json()

    if not actor_id:
        abort(400, {'message': 'please append an actor id to the request url.'})


    findActor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    
    if findActor is None:
          abort(404,{'message': 'Actor with id {} not found in database.'.format(actor_id)})
      
    try:
        findActor.delete()

    except Exception as e:
        abort(422,{'message':str(e)})

    return jsonify({
          'success': True,
          'deleted': findActor.id,
        })

    
    

    #==================ROUTES FOR MOVIES=================
  @app.route('/movies', methods=['GET'])
  @requires_auth('view:movies')  
  def get_movies(jwt):
      selection = Movie.query.all()
      movies_paginated = paginate_results(request, selection)

      if not movies_paginated:
          abort(404, {'message': 'No movie found in database.'})
        
      
      return jsonify({
          'success': True,
          'movies': movies_paginated
      })



  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def add_movies(jwt):
    body = request.get_json()

    if not body:
      abort(400, {'message': 'request does not contain a valid JSON body.'})

    title = body.get('title', None)
    release_date = body.get('release_date', None)
    
    if not title:
      abort(422, {'message': 'please enter title of movie.'})

    if not release_date:
      abort(422, {'message': 'please enter release date of movie'})
  
    try:
        movie = Movie(title,release_date)
        movie.insert()

    except Exception as e:
        abort(422,{'message': str(e)})

    return jsonify({
        'success': True,
        'created': movie.id
      })

    

  @app.route('/movies/<movie_id>', methods=['PATCH'])
  @requires_auth('update:movies')
  def update_movies(jwt,movie_id):
    body = request.get_json()

    if not movie_id:
        abort(400, {'message': 'please append an movie id to the request url.'})

    if not body:
        abort(400, {'message': 'request does not contain a valid JSON body.'})

    findMovie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    
    if findMovie is None:
          abort(404,{'message': 'movie with id {} not found in database.'.format(movie_id)})
      
    try:
        title = body.get('title',findMovie.title)
        release_date = body.get('release_date',findMovie.release_date)

        findMovie.title = title
        findMovie.release_date = release_date
        findMovie.update()

    except Exception as e:
        abort(422,{'message': str(e)})

    return jsonify({
          'success': True,
          'updated': findMovie.id,
          'actor' : [findMovie.format()]
        })


  @app.route('/movies/<movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(jwt,movie_id):
    body = request.get_json()

    if not movie_id:
        abort(400, {'message': 'please append an movie id to the request url.'})


    findActor = Movie.query.filter(Movie.id == movie_id).one_or_none()
    
    if findActor is None:
          abort(404,{'message': 'Movie with id {} not found in database.'.format(movie_id)})
      
    try:
        findActor.delete()

    except Exception as e:
        abort(422,{'message': str(e)})

    return jsonify({
          'success': True,
          'deleted': findActor.id,
        })

    

  





  # Error Handling
  '''
  Example error handling for unprocessable entity
  '''
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": error.description.get('message', 'unprocessable')
    }), 422



  @app.errorhandler(400)
  def not_found(error):
      return jsonify({
              "success": False,
              "error": 400,
              "message":error.description.get('message', 'resource not found')
              }), 400

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
              "success": False,
              "error": 404,
              "message": error.description.get('message', 'request does not contain a valid JSON body')
              }), 404


  @app.errorhandler(403)
  def not_found(error):
      return jsonify({
              "success": False,
              "error": 403,
              "message": error.description.get('message', 'Unauthorized request')
              }), 404


  @app.errorhandler(AuthError)
  def notAuthenticatedUser(auth_error):
      return jsonify({
          "success": False,
          "error": auth_error.status_code,
          "message": auth_error.error
      }), 401

  return app

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)