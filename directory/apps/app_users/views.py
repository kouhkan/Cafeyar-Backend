from flask import request, abort
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from sqlalchemy.exc import IntegrityError

from . import users

from directory import db
from directory.utils.request import json_only
from directory.utils.redis import (user_to_redis,
                                   get_user_from_redis,
                                   remove_user_from_redis)


@users.route('/register', methods=['POST'])
@json_only
def user_register():
    args = request.get_json()

