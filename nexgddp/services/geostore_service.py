"""Geostore SERVICE"""

from RWAPIMicroservicePython import request_to_microservice

from nexgddp.errors import GeostoreNotFound


class GeostoreService(object):
    """."""

    @staticmethod
    def execute(config):
        try:
            response = request_to_microservice(config)
            if not response or response.get('errors'):
                raise GeostoreNotFound
            geostore = response.get('data', None).get('attributes', None)
            geojson = geostore.get('geojson', None)
            bbox = geostore.get('bbox', None)
        except Exception as e:
            raise GeostoreNotFound(message=str(e))
        return geojson, bbox

    @staticmethod
    def get(geostore):
        config = {
            'uri': '/geostore/' + geostore,
            'method': 'GET'
        }
        return GeostoreService.execute(config)
