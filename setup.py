from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='kombinat.decogrid',
      version=version,
      description="A decogrid generator for plone columns.css file.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Environment :: Console",
        "Programming Language :: Python",
        ],
      keywords='decogrid',
      author='Daniel Widerin',
      author_email='daniel.widerin@kombinat.at',
      url='http://svn.plone.org/svn/collective/kombinat.decogrid/trunk',
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
            ]},
      )
