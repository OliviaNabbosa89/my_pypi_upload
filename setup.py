import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='omuliga_matrix', # Replace with your own username
    version="0.0.1",
    author="Olivia Nabbosa",
    author_email="olivia.nabbosa@outlook.com",
    description= "Matrix Operations",
    zip_safe=False,
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OliviaNabbosa89/my_pypi_upload/blob/master/README.md",
    project_urls={
        "Bug Tracker": "https://github.com/OliviaNabbosa89/my_pypi_upload/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
