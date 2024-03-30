from setuptools import setup, Extension
import numpy

setup(
    name="pubmed_scraper",
    ext_modules=[Extension("pubmed_scraper", ["pubmed_scraper.py"])],
    include_dirs=[numpy.get_include()],
    install_requires=["numpy"]
)
