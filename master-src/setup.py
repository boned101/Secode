#!/usr/bin/env python

# This is the setup.py script for "secode".

"""Setup script for the secode tool."""

from setuptools import setup # Don't need find_packages

setup (# Distribution meta-data
       name = "secode",
       version = "2",
       # We install a script, not a separate package.
       # packages = ["secode"], # Must be same as name
       # Do not need: packages=find_packages(),
       description = "a program that examines source code looking for security weaknesses",
       author = "--",
       author_email = "--",
       license = 'GPL-2.0+',
       long_description = """secode is a program that can scan
C/C++ source code and identify out potential security flaws,
ranking them by likely severity.
It is released under the GNU GPL license.""",
       url = "http://dwheeler.com/secode/",
       download_url = "https://sourceforge.net/projects/secode/files/secode-2.0.8.tar.gz/download",
       zip_safe = True,
       keywords = ['analysis', 'security', 'analyzer'],
       classifiers = [
           'Development Status :: 5 - Production/Stable',
           'Environment :: Console',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
           'Natural Language :: English',
           'Programming Language :: Python :: 2.7',
           'Programming Language :: Python :: 3',
           'Programming Language :: Python :: 3.6',
           'Operating System :: OS Independent',
           'Topic :: Security',
           'Topic :: Software Development :: Build Tools',
           'Topic :: Software Development :: Quality Assurance',
           'Topic :: Software Development :: Testing'
           ],
       python_requires = '>=2.7',
       scripts = [ 'secode' ],
       data_files = [ ('share/man/man1', [ 'secode.1.gz' ]) ],
       py_modules = [ ],
      )
