from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='free_email_domains',
    version='1.0.2',
    author='Luke Renton',
    description='A package containing a list of free email domains.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LukeRenton/free-email-domain-list",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)