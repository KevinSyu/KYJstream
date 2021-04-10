from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname('./'))
with open('README.md', 'rt') as f:
    long_description = f.read()

setup(
    name="KYJStream",
    version="0.1.0",
    author="KevinSyu & Dr.Chou",
    author_email="l8iunix8@gmail.com,callmeccy@gmail.com",
    description="Our side project",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="",
    packages=['lib','lib.exception']
)
