from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(filepath: str) -> list:
    '''
    this function reads the requirements file and returns the list of requirements
    '''
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Mallanath',
    author_email='mallanathmise@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)