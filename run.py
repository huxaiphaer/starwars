import redis
import requests
from celery import Celery
from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

from config.config import app_config

app = Flask(__name__)

load_dotenv()
# Add Redis URL configurations
app.config["CELERY_BROKER_URL"] = os.getenv("REDIS_CONFIG")
app.config["CELERY_RESULT_BACKEND"] = os.getenv("REDIS_CONFIG")
app.config.from_object(app_config["development"])

# Add periodic tasks
celery_beat_schedule = {
    "time_scheduler": {
        "task": "run.paginate_requested_data",
        # Run every second
        "schedule": 300.0,
    }
}

# configure celery

celery = Celery(app.name)
celery.conf.update(
    result_backend=app.config["CELERY_RESULT_BACKEND"],
    broker_url=app.config["CELERY_BROKER_URL"],
    timezone="UTC",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    beat_schedule=celery_beat_schedule,
)

# connection to redis

redis_db = redis.StrictRedis(
    host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=os.getenv("REDIS_DB"),
    charset=os.getenv("REDIS_CHAR_SET"), decode_responses=True
)


def insert_data(db, name, hyper_drive_rating):
    """
    :param name:
    :param hyper_drive_rating:
    :return: None
    """

    db.hset('mydata', name, hyper_drive_rating)

    return {"data": "data inserted successfully"}, 200


@celery.task
def paginate_requested_data():
    """
    This is a function for
    requesting data from an external api with pagination
    :return: None
    """

    pagination = 1
    url = 'https://swapi.co/api/starships/'
    params = {'page': pagination}
    r = requests.get(url, params=params)

    data = r.json()

    for i in data['results']:
        insert_data(redis_db, str(i['name']), str(i['hyperdrive_rating']))

    while r.status_code == 200:
        try:
            pagination += 1
            params['page'] = pagination
            r = requests.get(url, params=params)
            data = r.json()
            for i in data['results']:
                insert_data(str(i['name']), str(i['hyperdrive_rating']))
            return {"success": " Done insertion"}, 200
        except KeyError as k:
            print(k)
            return {'error': 'An error has occurred during this operation. {}'.format(k)}, 500


# secret key
app.secret_key = os.getenv("SECRET_KEY")

# Cross Origin Resource Sharing
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return 'Welcome to Star Wars End point. Test the endpoints in postman'


@app.route('/api/v1/starwars', methods=['GET'])
def get_star_ships():
    """
    Returns the json of the sorted
        data of star ships.
    :return: Filtered Data
    """

    known_star_ships = []
    unknown_star_ships = []
    paginate_requested_data.delay()
    res = redis_db.hgetall('mydata')

    for k, v in res.items():

        if str(v).strip() != "unknown":

            dict_known_stars = {"name": k, "hyperdrive": round(float(v), 2)}

            known_star_ships.append(dict_known_stars)

        else:
            dict_unknown_star_ships = {"name": k}
            unknown_star_ships.append(dict_unknown_star_ships)

    res = {"starships": sorted(known_star_ships, key=lambda o: o['hyperdrive']),
           "starships_unknown_hyperdrive": unknown_star_ships}

    return res


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=app_config["development"].DEBUG)
