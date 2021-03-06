#!/usr/bin/env/python
"""
Setup script for PuLP added by Stuart Mitchell 2007
Copyright 2007 Stuart Mitchell
"""
import sys
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

Description = open('README').read()

License = open('LICENSE').read()

# read the version number safely from the constants.py file
version_dict = {}
exec(open('src/pulp/constants.py').read(), version_dict)
VERSION = version_dict['VERSION']

#hack because pyparsing made version 2 python 3 specific
if sys.version_info[0] <= 2:
    pyparsing_ver = 'pyparsing<=1.9.9'
else:
    pyparsing_ver = 'pyparsing>=2.0.0'

setup(name="PuLP",
      version=VERSION,
      description="""
PuLP is an LP modeler written in python. PuLP can generate MPS or LP files
and call GLPK, COIN CLP/CBC, CPLEX, and GUROBI to solve linear
problems.
""",
      long_description = Description,
      license = License,
      keywords = ["Optimization", "Linear Programming", "Operations Research"],
      author="J.S. Roy and S.A. Mitchell",
      author_email="s.mitchell@auckland.ac.nz",
      url="http://pulp-or.googlecode.com/",
      classifiers = ['Development Status :: 5 - Production/Stable',
                     'Environment :: Console',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: BSD License',
                     'Natural Language :: English',
                     'Programming Language :: Python',
                     'Topic :: Scientific/Engineering :: Mathematics',
      ],
      #ext_modules = [pulpCOIN],
      package_dir={'':'src'},
      packages = ['pulp', 'pulp.solverdir'],
      package_data = {'pulp' : ["AUTHORS","LICENSE",
                                "pulp.cfg.linux",
                                "pulp.cfg.win",
                                "pulp.cfg.osx",
                                "LICENSE.CoinMP.txt",
                                "AUTHORS.CoinMP.txt",
                                "README.CoinMP.txt",
                                ],
                      'pulp.solverdir' : ['*','*.*']},
      install_requires = [pyparsing_ver],
      entry_points = ("""
      [console_scripts]
      pulptest = pulp:pulpTestAll
      pulpdoctest = pulp:pulpDoctest
      """
      ),
)
