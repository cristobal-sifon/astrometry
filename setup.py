import os
import re
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


# Taken from the Python docs:
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a
# top level README file and 2) it's easier to type in the README file
# than to put a raw string in below
def read(fname):
    fname = os.path.join(here, fname)
    if os.path.isfile(fname):
        return open(fname).read()


# this function copied from pip's setup.py
# https://github.com/pypa/pip/blob/1.5.6/setup.py
# so that the version is only set in the __init__.py and then read here
# to be consistent
def find_version(fname):
    version_file = read(fname)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="astrometry",
    version=find_version("src/astrometry/__init__.py"),
    author="Lukas Wenzl",
    description="Simple python3 tool to quickly correct the rough astronometry given by a telescope for a fits image.",
    entry_points={
        "console_scripts": [
            "astrometry=astrometry.astrometry:main",
            "photometry=astrometry.photometry:main",
        ]
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "astroquery",
        "astropy",
        "photutils",
        "matplotlib",
        "pandas",
        "numpy",
        "scipy",
    ],
)
