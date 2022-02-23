import redis

from directory.utils.utils import generate_random_code

redis = redis.Redis(
    host='172.17.0.3',
    db=0,
    port=6379,
)


def user_to_redis(username: str):
    code = generate_random_code()
    redis.set(username, code, ex=300)
    return code


def get_user_from_redis(username: str):
    user = redis.get(username)
    return user


def remove_user_from_redis(username: str):
    redis.delete(username)
    return True

