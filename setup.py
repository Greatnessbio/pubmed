from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension("*", ["*.pyx"],
              include_dirs=[numpy.get_include()])
]

setup(
    name="pubmed_scraper",
    ext_modules=cythonize(extensions),
    include_dirs=[numpy.get_include()]
)
