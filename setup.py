import os.path
import io

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.rst')) as f:
    readme = f.read()

setup(
    name='oidc-register',
    version='0.2.1',
    description='OpenID Connect Dynamic Client Registration tool',
    long_description=readme,
    url='https://github.com/puiterwijk/oidc-register',
    author='Patrick Uiterwijk',
    author_email='patrick@puiterwijk.org',
    packages=[
        'oidc_register',
    ],
    install_requires=[
        'httplib2',
    ],
    tests_require=['nose', 'mock'],
    entry_points={
        'console_scripts': ['oidc-register=oidc_register.registration_util:main'],
    },
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
