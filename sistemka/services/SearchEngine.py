from .base import BaseService


class SearchEngine(BaseService):
    def __init__(self,
                 service_name: str = 'SearchEngine',
                 url: str = 'http://165.22.95.38:4991/',
                 **kwargs: dict
                 ):
        super(SearchEngine, self).__init__(
            service_name=service_name,
            url=url,
            **kwargs
        )

    def search(self,
               image_path: str,
               **kwargs: dict
               ):
        url = self.url + 'search'
        image = open(image_path, 'rb')
        files = {'image': image}
        r = self.make_request(
            request_type='POST',
            url=url,
            files=files,
            **kwargs
        )
        image.close()
        return r.json().get('result')

    def indexing(self,
                 **kwargs: dict
                 ):
        url = self.url + 'indexing'

        r = self.make_request(
            request_type='GET',
            url=url,
            **kwargs
        )
        return r.json().get('message')
