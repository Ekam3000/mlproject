#setup will be responsible in creating my machine learning applications as a package.  and that packages we can install , and use in our project.


from setuptools import find_packages,setup

from typing import List
#find_packages -> so this will find all packages in the entire machine learning applications in the directory we have created 



HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
# file_path is the input parameter in str form , 
#get_requirements will return a List
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj: # opening the file_path which is our requirement.txt
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        # when we goes to next string in requirement.txt (like pandas to numpy)
        # we replace \n with ""

        if HYPEN_E_DOT in requirements: #when get_requiremnts function is called the -e . , is also readed , so -e . should not come in setup.py 
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Ekam bhele',
author_email='ekambhelle030@gmail.com',
packages=find_packages(), # whenever find_packages runs , it will  go and see
# how many folders having file __init__.py and it consider that folders as 
# package itself . and then it will try to build this so once it builds 
# right you can probably import this 

#Package Initialization: When a Python package is imported, the
#  interpreter looks for the __init__.py file in the package 
# directory and executes it. This file can be used to perform any 
# initialization that is necessary for the package to work correctly.
install_requires=get_requirements('requirements.txt')
)