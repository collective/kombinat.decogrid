from setuptools import setup, find_packages
import os

version = '0.4.dev0'

setup(
    name='kombinat.decogrid',
    version=version,
    description="A decogrid generator for plone columns.css file.",
    long_description="\n".join([
        open("README.rst").read() + "\n" +
        open("CHANGES.rst").read(),
    ]),
    # Get more strings from
    # https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone decogrid columns css generator',
    author='Daniel Widerin',
    author_email='daniel@widerin.net',
    maintainer='Leonardo Caballero',
    maintainer_email='leonardocaballero@gmail.com',
    url='https://github.com/collective/kombinat.decogrid',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['kombinat'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points={
        'console_scripts': [
            'decogrid_generatecss = kombinat.decogrid.grid:generator',
        ]
    },
)
