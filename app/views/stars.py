from app.utils.config import redis_db
from app.utils.tasks import paginate_requested_data
from run import app


@app.route('/api/v1/starwars', methods=['GET'])
def get_star_ships():
    """
    Returns the json of the sorted
        data of star ships.
    :return:
    """

    known_star_ships = []
    unknown_star_ships = []
    paginate_requested_data().delay()
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
