import os
from flask import (
    Flask,
    request,
    jsonify,
    abort
)
import json
from flask_cors import CORS
import babel

from models import (
    User,
    KeyWord,
    setup_db,
    db
)

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/users', methods=['GET'])
    def users():
        try:
            users = User.query.order_by(User.id).all()
            if users is None:
                print('No Users found. Empty database...')
                abort(404)
            return jsonify({
                'success':True,
                'users':[user.format() for user in users],
                'total_users':len(users)
            })
        except Exception as E:
            print(E)
            abort(422)
    
    @app.route('/user', methods=['GET'])
    def specificUser(userID):
        try:
            user = User.query.filter(User.id == userID).one_or_none()

            if user is None:
                print('USER NOT FOUND')
                abort(404)
            return jsonify({
                'success':True,
                'user':user.format()
            })
        except Exception as E:
            print(E)
            abort(422)

    @app.route('/users', methods=['POST'])
    def createUser():
        try:
            body = request.get_json()

            new_fName = body.get('fName', None)
            new_lName = body.get('lName', None)
            new_uName = body.get('uName', None)

            newUser = User(fName=new_fName,
                           lName=new_lName,
                           uName=new_uName)
            newUser.insert()

            return jsonify({
                'success':True,
                'user':newUser.format(),
                'created':newUser.id
            })
        except Exception as E:
            print(E)
            abort(422)
        
    @app.route('/users', methods=['DELETE'])
    def deleteUser(userID):
        try:
            targetUser = User.query.filter(User.id == userID).one_or_none()

            if targetUser is None:
                print('Could not delete nonexistent user')
                abort(422)
            targetUser.delete()

            return jsonify({
                'success':True,
                'deleted':targetUser.id
            })
        except Exception as E:
            print(E)
            abort(422)

    @app.route('/keywords', methods=['GET'])
    def keywords():
        try:
            keywords = KeyWord.query.order_by(KeyWord.id).all()

            if keywords is None:
                print('No keywords found. Empty database...')
                abort(404)
            
            return jsonify({
                'success':True,
                'keywords':[keyword.format() for keyword in keywords]
            })
        except Exception as E:
            print(E)
            abort(422)
    
    @app.route('/keywords', methods=['GET'])
    def specificKeyword(keywordID):
        try:
            keyword = KeyWord.query.filter(KeyWord.id == keywordID).one_or_none()

            if keyword is None:
                print(f'ERROR finding {keywordID}')
                abort(404)
            
            return jsonify({
                'success':True,
                'keyword':keyword.format()
            })
        except Exception as E:
            print(E)
            abort(422)
        
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success':True,
            'error':422,
            'message':'Not Processable'
        }), 422
    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success':False,
            'error':403,
            'message':'Forbidden. Authentication credentials sent with request are insufficient for the request'
        }), 403
    @app.errorhandler(405)
    def methodNotAllowed(error):
        return jsonify({
            'success':False,
            'error':405,
            'message':'Method Not Allowed. Method requested is not supported for the given response'
        }), 405
    @app.errorhandler(500)
    def internalServerError(error):
        return jsonify({
            'success':False,
            'error':500,
            'message':'Internal Server Error. An unexpected error occured while processing the request'
        }), 500
    return app