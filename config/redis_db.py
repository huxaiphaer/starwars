import os
from dotenv import load_dotenv
import redis
load_dotenv()

redis_db = redis.StrictRedis(
    host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=os.getenv("REDIS_DB"),
    charset=os.getenv("REDIS_CHAR_SET"), decode_responses=True
)
