from setuptools import setup

with open("README", 'r', encoding="utf8") as f:
    long_description = f.read()

setup(
   name='mpiyango',
   version='0.0.7',
   description='A module to get various lottery data from National Lottery Administration of Turkey (in Turkish)',
   license="MIT",
   long_description=long_description,
   author='Cagrimanoka',
   author_email='cs.mirap@pm.me',
   url="https://github.com/Cagrimanoka/MPiyango",
   classifiers=[
      "Programming Language :: Python :: 3",
   ],
   python_requires='>=3.6',
   install_requires=['requests'],
   packages=['mpiyango']
)