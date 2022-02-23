from datetime import datetime

from directory import db

# from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'tbl_users'
    username = db.Column(db.String(11), primary_key=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=True, unique=False)
    is_active = db.Column(db.Boolean(), default=False, nullable=False)
    date_joined = db.Column(db.DateTime(), default=datetime.now, nullable=True)

    # One-To-One field for every user has one field on tbl_profiles
    profile = db.relationship('Profile', backref='tbl_users', uselist=False)

    @validates('username')
    def validate_username(self, key, value):
        if value is None:
            raise ValueError("Username can't be empty")
        if len(value) < 11 or len(value) > 11:
            raise ValueError("Username must be 11 characters exactly")
        return value


class Profile(db.Model):
    __tablename__ = 'tbl_profiles'
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(11), db.ForeignKey('tbl_users.username'), index=True)
    first_name = db.Column(db.String(63), nullable=True, unique=False)
    last_name = db.Column(db.String(63), nullable=True, unique=False)
    avatar = db.Column(db.String(256), nullable=True, unique=False)
    birth_date = db.Column(db.DateTime(), nullable=True, unique=False)

    # user = db.relationship('User', back_populates='tbl_profiles')
