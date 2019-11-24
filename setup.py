import json

from setuptools import setup, find_packages


def requirements():
    requirements_list = []
    with open('Pipfile.lock', "r") as requirements:
        data = json.load(requirements)
    data = data['default']
    for i in data:
        try:
            req = i + data[i]['version'].replace('==', '>=')
        except KeyError:
            req = f"-e git+{data[i]['git']}@{data[i]['ref']}#egg={i}"
        requirements_list.append(req)
    return requirements_list


setup(
    name='nlogic',
    version='0.1.1',
    description='Connectors for Sistemka micro-services',
    author='Sistemka',
    author_email='antipinsuperstar@yandex.ru',
    url='https://github.com/Sistemka/Sistemka',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=requirements(),
)
