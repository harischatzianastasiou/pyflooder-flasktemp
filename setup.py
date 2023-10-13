from setuptools import find_packages
from setuptools import setup

setup(
        name='flasktemp',
        version='1.0.0',
        description='
                Runs an HTTP Flood Python script that could stop
                the webpage used in flasktemp',
        author='tchatzian',
        author_email='harischatzi1988@gmail.com',
        url='https://github.com/tchatzian/flasktemp',
        packages=['flasktemp'],
        include_package_data=True,
        zip_safe=False,
        scripts=['flasktemp/pyflooder.py']
)

