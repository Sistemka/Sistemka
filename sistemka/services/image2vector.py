from .base import BaseService


class Image2Vector(BaseService):
    def __init__(self,
                 service_name: str = 'Image2Vector',
                 url: str = 'http://165.22.95.38:4990/',
                 **kwargs: dict
                 ):
        super(Image2Vector, self).__init__(
            service_name=service_name,
            url=url,
            **kwargs
        )

    def image_to_vector(self,
                        image_path: str,
                        image_name: str,
                        mimetype: str = 'image/jpeg',
                        height: int = 224,
                        width: int = 224,
                        **kwargs: dict
                        ):
        url = self.url + 'image_to_vector'
        params = {'height': height, 'width': width}
        image = open(image_path, 'rb')
        files = {'image': (image_name, image, mimetype)}
        r = self.make_request(
            request_type='POST',
            url=url,
            params=params,
            files=files,
            **kwargs
        )
        image.close()
        return r.json().get('result')
