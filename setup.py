from setuptools import find_packages,setup

def get_requirements(file_path):
    """
    This function will return the list of packages 
    """

    with open(file_path) as fb:
        requirements=[ line.replace('\n'," ") if line != "-e ." for line in fb.readlines()]
    return requirements



setup(

    name='MLPROJECT'
    version='0.0.1'
    author='Sasi'
    author_email='sasi.dhar6025@gmail.com'
    packages=find_packages()
    install_requires=get_requirements('requirements.txt')

)