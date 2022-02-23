from flask import request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from sqlalchemy.exc import IntegrityError

from . import users
from .models import User, Profile

from directory import db
from directory.utils.request import json_only
from directory.utils.redis import (user_to_redis,
                                   get_user_from_redis,
                                   remove_user_from_redis)
from directory.utils.responses import response


@users.route('/authenticate', methods=['POST'])
@json_only
def user_register_login():
    args = request.get_json()

    new_user = User()
    try:
        new_user.username = args.get('username')
        new_user.password = args.get('password')

        # send code to phone number
        code = user_to_redis(new_user.username)
        print(code)

        db.session.add(new_user)
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        return response(None, 400, f'{e}'), 400
    except IntegrityError:
        db.session.rollback()
        # user login
        code = user_to_redis(new_user.username)
        print(code)

        return response(
            data=f'{new_user.username}',
            code=200,
            msg='user login'
        ), 200

    return response(
        data=f'{new_user.username}',
        code=201,
        msg='user created'
    ), 201


@users.route('/activate', methods=['PATCH'])
@json_only
def user_activate():
    pass


@users.route('/login', methods=['POST'])
@json_only
def user_login():
    pass


@users.route('/change-password', methods=['PATCH'])
@json_only
def user_change_password():
    pass


@users.route('/profile', methods=['PATCH'])
@json_only
def user_profile_complete():
    pass


@users.route('/token', methods=['PUT'])
@json_only
def user_new_token():
    pass

