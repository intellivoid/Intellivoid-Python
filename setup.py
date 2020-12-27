#  Intellivoid - COA API Interface
#  Copyright (C) 2020 Intellivoid <https://github.com/intellivoid>
#
#  This file is part of the Intellivoid package.
#
#  This package is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This package is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this package.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='intellivoid',
    version='1.0.4',
    description='Official Intellivoid Services API Wrapper for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['intellivoid'],
    package_dir={
        'intellivoid': 'intellivoid'
    },
    author='Intellivoid Technologies',
    author_email='netkas@intellivoid.net',
    url='https://accounts.intellivoid.net/',
    install_requires=[
        'requests>=2.3.0',
        'httpx',
        'trio'
    ]
)
