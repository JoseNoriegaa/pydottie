from setuptools import setup  # type: ignore
from setuptools import find_packages

VERSION = '0.0.2'
DESCRIPTION = 'PyDottie is a library based on dottie.js written in Python 3.'

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

# Setting up the package
setup(
    name='pydottie',
    url='https://github.com/JoseNoriegaa/pydottie',
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='josenoriega (Jose Noriega)',
    author_email='josenoriega723@gmail.com',
    install_requires=[],
    keywords=[
        'pydottie',
        'dottie',
        'dict',
        'dot path',
        'dot notation',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/pypa/sampleproject/issues',
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
)
