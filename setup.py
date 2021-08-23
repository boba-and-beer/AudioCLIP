from setuptools import setup, find_packages
from pip.req import parse_requirements
install_reqs = parse_requirements("requirements.txt")

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]
setup(
    name='audioclip',
    version='1.0.0',
    url='',
    author='',
    author_email='',
    description='',
    packages=find_packages(),    
    install_requires=reqs,
)
