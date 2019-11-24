# Sistemka
Http connection for Sistemka micro-services

Установить пакет

```shell script
pipenv install -e git+https://github.com/Sistemka/Sistemka.git#egg=sistemka
```

Любой сервис запускается пока так

```python
from sistemka.services import Image2Vector

a = Image2Vector()


if __name__ == '__main__':
    r = a.image_to_vector(
        image_path='/Users/markantipin/Downloads/5232.jpg',
        image_name='kasatka'
    )
    print(r)
```
