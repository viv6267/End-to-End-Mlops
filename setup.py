import setuptools
from typing import List

hypen_e_name ='-e .'

def get_requirements(file_path:str)->List[str]:

    """
    this is a function that returns a list of requirements
    """
    with open(file_path, 'r') as f:
        requirements=f.readlines()
        requirements=[requirement.replace('\n','') for requirement in requirements]
        if hypen_e_name in requirements:
            requirements.remove(hypen_e_name)
    return requirements

with open("README.md",'r',encoding='utf-8')as f:
    long_description = f.read()

__version__ = '0.0.1'

REPO_NAME='End-to-End-Mlops'
AUTHOR_USER_NAME='Vivek Kumar'
SRC_REPO="mlProject"
AUTHOR_EMAIL="viv6267@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A comprehensive end-to-end machine learning project with CI/CD pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/viv6267/" + SRC_REPO,
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)



