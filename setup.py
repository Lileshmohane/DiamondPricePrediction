from  setuptools import find_packages,setup
from typing import List 



HYPER_E_DOT ='-e .'
# tru to open  requrement file
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT) 

setup(
    
    name='Diamond_price',
    version ='0.0.1',
    author='lilesh',
    author_email= 'lileshmohane2002@gamil.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)