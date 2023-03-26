from setuptools import find_packages,setup
from typing import List
Hyphem_E_Dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    #"this function call return list of requirements"
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        # it contains \n also
        requirements = [req.replace("\n","") for req in requirements]
        # add -e . to trigger setup.py automatically 
        if Hyphem_E_Dot in requirements:
            requirements.remove(Hyphem_E_Dot)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Gowtham",
    author_email="gowthamregeti@gmail.com",
    packages=find_packages(),
    install_packages=get_requirements('requirements.txt')

)