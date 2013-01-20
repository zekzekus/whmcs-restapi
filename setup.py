# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.0.1'

install_requires = [
    'flask',
    'simplejson',
    'pywhmcs',
]


setup(
    name='whmcs-restapi',
    version=version,
    description="Rest API server for WHMCS SOAP like HTTP API",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        # classifiers
    ],
    keywords='rest server api flask whmcs http',
    author='Zekeriya Koc',
    author_email='zekzekus@gmail.com',
    url='',
    license='Gnu General Public License v3',
    packages=find_packages('src'),
    package_dir={'': 'src'}, include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['whmcs-restapi=whmcsrestapi:main']
    }
)
