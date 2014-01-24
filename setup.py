# coding: utf-8

""" Create awesome visualisations using data from NASA's ADS """

import os
import re
import sys

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

major, minor1, minor2, release, serial =  sys.version_info

readfile_kwargs = {"encoding": "utf-8"} if major >= 3 else {}

def readfile(filename):
    with open(filename, **readfile_kwargs) as fp:
        contents = fp.read()
    return contents

version_regex = re.compile("__version__ = \"(.*?)\"")
contents = readfile(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "adshax",
    "__init__.py"))

version = version_regex.findall(contents)[0]

setup(name="adshax",
      version=version,
      author="Andrew R. Casey",
      author_email="andy@astrowizici.st",
      packages=["adshax"],
      url="http://www.github.com/andycasey/adshax/",
      license="GPLv2",
      description="Create awesome visualisations using data from NASA's ADS",
      long_description=readfile(os.path.join(os.path.dirname(__file__), "README.md")),
      install_requires=[
        "ads"
      ]
     )
