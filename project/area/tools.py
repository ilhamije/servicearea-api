import geopy
import geopy.distance as distance
from shapely.geometry import Polygon


def generate_polygon(origin_point: tuple):
    # 5km
    d = distance.distance(kilometers=5000/1000)
    point_1 = geopy.Point(origin_point)
    point_2 = d.destination(point=point_1, bearing=0)
    point_3 = d.destination(point=point_2, bearing=90)
    point_4 = d.destination(point=point_3, bearing=180)

    results = [(p.latitude, p.longitude) for p in [
        point_1, point_2, point_3, point_4
    ]]

    return Polygon(results)
