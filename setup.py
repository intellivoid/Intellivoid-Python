from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='intellivoid',
    version='1.0.0',
    description='Official Intellivoid & COA API Wrapper for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['intellivoid', 'intellivoid.coa'],
    package_dir={
        'coffeehouse': 'coffeehouse'
    },
    author='Intellivoid Technologies',
    author_email='netkas@intellivoid.net',
    url='https://accounts.intellivoid.net/',
    install_requires=[
        'requests>=2.3.0'
    ]
)
