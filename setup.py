import io
import os

from setuptools import find_packages
from setuptools import setup


# Package meta-data.
NAME = 'leab'
DESCRIPTION = 'Lets Python do AB testing analysis.'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
URL = 'https://github.com/tlentali/leab'
EMAIL = 'thomas.lentali@gmail.com'
AUTHOR = 'Thomas Lentali'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.1'

# Package requirements.
base_packages = [
        'numpy>=1.18.2',
        'scipy>=1.4.1',
        'pandas>=1.0.3',
        'statsmodels>=0.11.1',
        'matplotlib>=3.0.2',
    ]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name=NAME,
    packages=find_packages(),
    version=VERSION,
    license="MIT",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    keywords=['data-science', 'ab-testing', 'analysis','statistics', 'datascience', 'data'],
    install_requires=base_packages,
    classifiers=[
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
