from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='mpiyango',
   version='0.1',
   description='A module to get various lottery data from National Lottery Administration of Turkey (in Turkish)',
   license="MIT",
   long_description=long_description,
   author='Çağrı Sarp Mirapoğlu',
   author_email='cs.mirap@pm.me',
   packages=['ornekler'],
   install_requires=['requests']
)