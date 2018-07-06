import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='drf-feedback',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  
    description='Feedbank APP for Django REST Framework with API Views.',
    long_description=README,
    # url='https://www.example.com/',
    author='Mahen Gandhi',
    author_email='mahengandhi19@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0', 
        'Intended Audience :: Developers',
       # 'Intended Audience :: Eductaion',
        'License :: OSI Approved :: MIT License',
        # 'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE v2(GPLv2)',
        # 'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE v3(GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
