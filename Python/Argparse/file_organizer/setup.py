# setup.py

from setuptools import setup, find_packages

setup(
    name="file-organizer",
    version="1.0.0",
    description="CLI tool to organize files automatically",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "organize=organizer.main:main"
        ]
    },
)