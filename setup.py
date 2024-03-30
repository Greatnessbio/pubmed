from setuptools import setup, find_packages

setup(
    name="pubmed_scraper",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "asyncio",
        "beautifulsoup4",
        "bs4",
        "lxml",
        "pandas",
        "requests",
        "streamlit",
        "numpy"
    ]
)
