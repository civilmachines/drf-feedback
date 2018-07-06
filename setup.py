from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    README = readme.read()

setup(
    name='drf_feedback',
    version=__import__('drf_feedback').__version__,
    author=__import__('drf_feedback').__author__,
    author_email='mahengandhi19@gmail.com',
    description='Feedback APP for Django REST Framework with API Views.',
    long_description=README,
    long_description_content_type="text/markdown",
    license=__import__('drf_feedback').__license__,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/civilmachines/drf-drf_feedback',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
