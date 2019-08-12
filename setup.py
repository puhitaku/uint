from pathlib import Path
from setuptools import setup, find_packages


__version__ = '0.0.1'
__author__ = 'Takumi Sueda'
__author_email__ = 'puhitaku@gmail.com'
__license__ = 'MIT License'
__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7']

with open(Path(__file__).parent / 'README.md') as f:
    readme = f.read()

setup(
    name='uint',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url='https://github.com/puhitaku/uint',
    description='Fixed-width integer and calculation for Python',
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=__classifiers__,
    packages=find_packages(),
    license=__license__,
    test_suite='tests',
    include_package_data=True)
