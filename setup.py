"""Setup script for the PetintLib package"""

import sys
from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    """Executes setup when this script is the top-level"""
    import PetintLib as App

    setup(
        name=App.__project__,
        version=App.__version__,
        description=App.__doc__,
        long_description=read('README.md'),
        classifiers=App.__classifiers__,
        author=App.__author__,
        author_email=App.__author_email__,
        url=App.__url__,
        license=[
            c.rsplit('::', 1)[1].strip()
            for c in App.__classifiers__
            if c.startswith('License ::')
        ][0],
        keywords=App.__keywords__,
        packages=find_packages(),
        include_package_data=True,
        platforms=App.__platforms__,
        entry_points=App.__entry_points__,
        install_requires=App.__requires__,
        extras_require=App.__extra_requires__,
    )


if __name__ == '__main__':
    main()
