from typing import List

from .base import BaseService


class Image2Vector(BaseService):
    def __init__(
            self,
            service_name: str = 'Image2Vector',
            url: str = 'http://165.22.95.38:4990/',
            **kwargs: dict
    ):
        super(Image2Vector, self).__init__(
            service_name=service_name,
            url=url,
            **kwargs
        )

    def vectorize_bulk(
            self,
            images_paths: List[str],
            **kwargs: dict
    ):
        url = self.url + 'image2vector/bulk'
        files = {}
        for image in images_paths:
            files[image] = open(image, 'rb')
        r = self.make_request(
            request_type='POST',
            url=url,
            files=files,
            **kwargs
        )
        for image in files.values():
            image.close()
        return r.json().get('result')

    def vectorize(
            self,
            image_path: str,
            **kwargs: dict
    ):
        url = self.url + 'image2vector'
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
