import os
import zipfile
from pathlib import Path

from .base import BaseService


class Segmentator(BaseService):
    def __init__(
            self,
            service_name: str = 'Segmentator',
            url: str = 'http://165.22.95.38:4993/',
            **kwargs: dict
    ):
        super(Segmentator, self).__init__(
            service_name=service_name,
            url=url,
            **kwargs
        )

    def get_files(
            self,
            image_path: str,
            cropped_images_dir: str,
            **kwargs: dict
    ):
        url = self.url + 'segmentation'
        image = open(image_path, 'rb')
        files = {'image': image}
        r = self.make_request(
            request_type='POST',
            url=url,
            files=files,
            params={'return_vector': False},
            **kwargs
        )
        image.close()
        if r.status_code == 204:
            return None

        Path(cropped_images_dir).mkdir(parents=True, exist_ok=True)

        zip_file_path = f"{cropped_images_dir}.zip"

        with open(zip_file_path, 'wb') as f:
            f.write(r.content)
        with zipfile.ZipFile(zip_file_path, "r") as z_f:
            z_f.extractall(cropped_images_dir)

        os.remove(zip_file_path)

        cropped_images_paths = [
            Path(cropped_images_dir, image).as_posix() for image in os.listdir(cropped_images_dir)
            if os.path.isfile(Path(cropped_images_dir, image))
        ]

        return cropped_images_paths
