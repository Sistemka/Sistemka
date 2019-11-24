import requests
from requests.adapters import HTTPAdapter


class BaseService(object):
    def __init__(self,
                 service_name: str,
                 url: str,
                 scheme: str = 'http',
                 pool_connections: int = 10,
                 pool_maxsize: int = 10,
                 ):
        self.service_name = service_name
        self.url = url
        self.scheme = scheme
        self.pool_connections = pool_connections
        self.pool_maxsize = pool_maxsize
        self.session = requests.Session()
        adapter = HTTPAdapter(
            pool_connections=self.pool_connections,
            pool_maxsize=self.pool_maxsize
        )

        self.session.mount(prefix=self.scheme, adapter=adapter)

    def make_request(self,
                     request_type: str,
                     url: str,
                     json: dict = None,
                     **kwargs
                     ) -> requests.Response:
        s = self.session
        request_func = {
            'GET': s.get,
            'POST': s.post
        }
        func = request_func.get(request_type)
        if request_type is None:
            raise KeyError('unsupported request type')
        r = func(
            url=url,
            headers={'X-SERVICE-NAME': self.service_name},
            json=json,
            params=kwargs.pop('params', None),
            files=kwargs.pop('files', None),
            **kwargs
        )
        return r
