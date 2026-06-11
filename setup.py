from setuptools import setup, find_packages
#testlisa
setup(
    name='mp-spdz-compiler',
    version='0.1.0',
    packages=find_packages(include=['Compiler', 'Compiler.*'])
)
