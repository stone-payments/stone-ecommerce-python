# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = '1.0.1'
__description__ = 'Python stone payment api'
__long_description__ = 'Sdk for integration with stone payment api'

__author__ = 'Stone Pagamentos'
__author_email__ = 'devcenter@stone.com.br'

requires = [i.strip() for i in open("requirements.txt").readlines()]

testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='stone_ecommerce_python',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='Apache',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/stone-pagamentos/stone-ecommerce-python',
    keywords=['stone', 'rest', 'sdk', 'payments'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7'
    ],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)
