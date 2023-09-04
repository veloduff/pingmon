"""
pingmon
---------------
"""

#
# Copyright 2020 Mark Duffield
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.
#

# setup.py classifiers
# https://pypi.python.org/pypi?%3Aaction=list_classifiers

_version = "1.0.2"

import os
import io
from setuptools import setup, find_packages


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))


console_scripts = ['pingmon = pingmon.pingmon:main',
                   'pinggraph = pingmon.pinggraph:main',
                    ]

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pingmon',
    packages=['pingmon'],
    version=_version,
    python_requires='>=3',
    url='https://github.com/veloduff/pingmon',
    license="Apache License 2.0",
    author='Mark Duffield',
    author_email='veloduff@gmail.com',
    description='Monitor, record, and display ping results',
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'matplotlib>=3.1.3',
        'requests'
    ],
    keywords='ping monitor',
    entry_points=dict(console_scripts=console_scripts),
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
