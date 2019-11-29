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

    def predict(self,
                image_path: str,
                image_name: str,
                mimetype: str = 'image/jpeg',
                **kwargs: dict
                ):
        url = self.url + 'predict'
        image = open(image_path, 'rb')
        files = {'image': (image_name, image, mimetype)}
        r = self.make_request(
            request_type='POST',
            url=url,
            files=files,
            **kwargs
        )
        image.close()
        return r.json().get('result')
