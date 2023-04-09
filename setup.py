from setuptools import setup
import os

#requirements.txt lecture
REQUIREMENTS_PATH = os.path.join(os.path.curdir,'requirements.txt')
with open(REQUIREMENTS_PATH, 'r') as f:
    requires = f.readlines()
    for i in range(len(requires)):
        requires[i] = requires[i].replace('\n','')

#setup
setup(
   name='QR_API',
   version='0.0.1',
   description='API for the QR-Project',
   author='kevcangas',
   author_email='kev162020@gmail.com',
   packages= [os.path.abspath(os.getcwd())],  # would be the same as name
   install_requires=requires #external packages acting as dependencies
)