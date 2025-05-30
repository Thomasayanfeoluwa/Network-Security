from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:

    """
    This function reads a requirements file and returns a list of requirements.
    """

    requirement_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                # Igore empty lines and cand -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Warning: requirements.txt not found.")

    return requirement_list

setup(
    name="Network Security",
    version="0.0.1",
    author="Idowu Thomas",
    author_email="ayanfeoluwadegoke@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)