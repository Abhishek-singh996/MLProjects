from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(filepath:str)->List[str]:
    '''
    This function will return list of all the requirements
    '''

    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='MLProjects',
    version='0.0.1',
    author='Abhishek Singh',
    author_email='nitianabhishek996@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)