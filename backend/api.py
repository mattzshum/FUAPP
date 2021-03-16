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
    Fuck,
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
    
    @app.route('/user/<int:userID>', methods=['GET'])
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
                'deleted':userID
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
                'keywords':[keyword.format() for keyword in keywords],
                'total_keywords':len(keywords)
            })
        except Exception as E:
            print(E)
            abort(422)
    
    @app.route('/keywords/<string:keywordID>', methods=['GET'])
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
        
    @app.route('/keywords', methods=['POST'])
    def postKeyword():
        try:
            body = request.get_json()

            new_keyword = body.get('keyword', None)

            newKeyword = KeyWord(keyword=new_keyword)
            newKeyword.insert()

            return jsonify({
                'success':True,
                'keyword':newKeyword.format(),
                'created':newKeyword.id
            })
        except Exception as E:
            print(E)
            abort(422)

    @app.route('/keywords/<string:keywordID', methods=['DELETE'])
    def deleteKeyword(keywordID):
        try:
            keyword = KeyWord.query.filter(KeyWord.id == keywordID).one_or_none()

            if keyword is None:
                print(f'ERROR FINDING {keywordID}')
                abort(404)
            
            keyword.delete()

            return jsonify({
                'success':True,
                'deleted':keywordID
            })
        except Exception as E:
            print(E)
            abort(422)
    
    @app.route('/fuck', methods=['GET'])
    def fuck():
        try:
            fuckList = Fuck.query.order_by(Fuck.id).all()

            if fuckList is None:
                print('ERROR empty Fuck database')
                abort(404)
            
            return jsonify({
                'success':True,
                'fucks':[fuck.format() for fuck in fuckList],
                'total_fucks':len(fuckList)
            })
        except Exception as E:
            print(E)
            abort(422)
    
    @app.route('/fuck/<int:fuckID>', methods=['GET'])
    def specificFuck(fuckID):
        try:
            fuck = Fuck.query.filter(Fuck.id == fuckID).one_or_none()

            if fuck is None:
                print('Database could not give a Fuck')
                abort(404)
            
            return jsonify({
                'success':True,
                'fuck':fuck.format()
            })
        except Exception as E:
            print(E)
            abort(422)
    
    @app.route('/fuck', methods=['POST'])
    def postFuck():
        try:
            body = request.get_json()

            new_userID = body.get('userID', None)
            new_keyword = body.get('keyword', None)

            fuck = Fuck(userID = new_userID,
                        keyword = new_keyword)
            fuck.insert()

            return jsonify({
                'success':True,
                'fuck':fuck.format(),
                'created':fuck.id
            })
        except Exception as E:
            print(E)
            abort(422)
    
    @app.route('/fuck/<int:fuckID>', methods=['DELETE'])
    def deleteFuck(fuckID):
        try:
            fuck = Fuck.query.filter(Fuck.id == fuckID).one_or_none()

            if fuck is None:
                print('Database could not give a Fuck')
                abort(404)
            
            fuck.delete()

            return jsonify({
                'success':True,
                'deleted':fuckID
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