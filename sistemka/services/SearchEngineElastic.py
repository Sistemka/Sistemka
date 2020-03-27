from pathlib import Path
from typing import ByteString

from .base import BaseService


class SearchEngineElastic(BaseService):
    def __init__(self,
                 service_name: str = 'SearchEngineElastic',
                 url: str = 'http://95.216.215.173:5002/',
                 **kwargs: dict
                 ):
        super().__init__(
            service_name=service_name,
            url=url,
            **kwargs
        )

    def search(self,
               image_path: [str, Path] = None,
               image_bytes: [bytes, ByteString] = None,
               **kwargs: dict
               ):
        url = self.url + 'image/search'
        if image_path:
            image = open(image_path, 'rb')
        else:
            image = image_bytes
        files = {'image': image}
        r = self.make_request(
            request_type='POST',
            url=url,
            files=files,
            **kwargs
        )
        image.close()
        return r.json().get('result')

    def add_image(self,
                  image_path_param: str,
                  image_path: [str, Path] = None,
                  image_bytes: [bytes, ByteString] = None,
                  **kwargs: dict
                  ):
        if image_path is None and image_bytes is None:
            raise ValueError('no file passed')
        url = self.url + 'image/add'
        if image_path:
            image = open(image_path, 'rb')
        else:
            image = image_bytes
        files = {'image': image}
        r = self.make_request(
            request_type='POST',
            url=url,
            files=files,
            params={'image_path': image_path_param},
            **kwargs
        )
        image.close()
        return r.json().get('message')

    def indexing(self,
                 **kwargs: dict
                 ):
        url = self.url + 'image/add/from_image_manager'

        r = self.make_request(
            request_type='GET',
            url=url,
            **kwargs
        )
        return r.json().get('message')
