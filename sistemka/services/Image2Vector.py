from typing import List, Union

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

    def vectorize(
            self,
            image_paths: Union[str, List[str]],
            **kwargs: dict
    ):
        url = self.url + '/image2vector'
        images = {}
        if isinstance(image_paths, str):
            images['image'] = open(image_paths, 'rb')
        else:
            for image in image_paths:
                images[image] = open(image, 'rb')
        r = self.make_request(
            request_type='POST',
            url=url,
            files=images,
            **kwargs
        )
        for image in images.values():
            image.close()
        return r.json().get('result')
