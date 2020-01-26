import requests

from app.utils.config import redis_db
from run import celery


def insert_data(name, hyper_drive_rating):
    """
    :param name:
    :param hyper_drive_rating:
    :return: None
    """

    redis_db.hset('mydata', name, hyper_drive_rating)


@celery.task
def paginate_requested_data():
    """
    This is a function for
    requesting data from an external api.
    :return: None
    """

    pagination = 1
    url = 'https://swapi.co/api/starships/'
    params = {'page': pagination}
    r = requests.get(url, params=params)

    data = r.json()

    for i in data['results']:
        insert_data(str(i['name']), str(i['hyperdrive_rating']))

    while r.status_code == 200:
        try:
            pagination += 1
            params['page'] = pagination
            r = requests.get(url, params=params)
            data = r.json()
            for i in data['results']:
                insert_data(str(i['name']), str(i['hyperdrive_rating']))
        except KeyError as k:
            print(k)
            return {'error': 'An error has occurred during this operation. {}'.format(k)}
