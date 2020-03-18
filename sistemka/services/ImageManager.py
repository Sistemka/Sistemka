from pathlib import Path

from .base import BaseService


class ImageManager(BaseService):
    def __init__(self,
                 service_name: str = 'ImageManager',
                 url: str = 'http://165.22.95.38:4992/',
                 **kwargs: dict
                 ):
        super(ImageManager, self).__init__(
            service_name=service_name,
            url=url,
            **kwargs
        )

    def upload_image(self,
                     image_path: str,
                     type: str,
                     **kwargs: dict
                     ):
        url = self.url + 'image/upload'
        params = {'type': type}
        image = open(image_path, 'rb')
        files = {'image': image}
        r = self.make_request(
            request_type='POST',
            url=url,
            params=params,
            files=files,
            **kwargs
        )
        image.close()
        return r.json().get('message')

    def upload_image_bytes(self,
                           params):
        url = self.url + 'image/upload'
        files = {'image': params.pop('image')}
        r = self.make_request(
            request_type='POST',
            url=url,
            files=files,
            params=params
        )
        return r.json().get('message')

    def download_image(self,
                       url: str,
                       path_to_download: str,
                       **kwargs: dict
                       ):
        url = self.url + f"image/download/{url}"
        r = self.make_request(
            request_type='GET',
            url=url,
            **kwargs
        )
        Path(Path(path_to_download).parent).mkdir(
            parents=True, exist_ok=True
        )
        with open(Path(path_to_download), 'wb') as f:
            f.write(r.content)

    def get_urls(self,
                 **kwargs: dict
                 ):
        url = self.url + 'url/all'

        r = self.make_request(
            request_type='GET',
            url=url,
            **kwargs
        )
        return r.json().get('result')
    
    def get_image_info(self, image_path: str, **kwargs):
        url = self.url + 'image/get-info'

        r = self.make_request(
            request_type='GET',
            url=url,
            **kwargs
        )
        return r.json().get('result')

