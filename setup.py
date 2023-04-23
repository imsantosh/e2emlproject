from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirments(file_path:str)->List[str]:
    '''
    this function will return requirements
    '''
    requirements=[]

    with open(file_path) as file_ojb:
        requirements=file_ojb.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
   name='e2emlproject',
   version='0.0.1',
   author='Santosh Singh',
   packages=find_packages(),
   install_requires= get_requirments('requirements.txt')
)