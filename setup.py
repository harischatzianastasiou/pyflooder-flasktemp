from setuptools import find_packages
from setuptools import setup

setup(
        name='flasktemp',
        version='1.0.0',
        description='Displays a
                message on webpage server via python flask and
                runs an HTTP Flood Python script that could stop
                webpage in 10s',
        author='tchatzian',
        author_email='harischatzi1988@gmail.com',
        url='https://github.com/tchatzian/flasktemp',
        packages=['flasktemp'],
        include_package_data=True,
        zip_safe=False,
        scripts=['flasktemp/pyflooder.py']
)

