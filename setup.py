from setuptools import setup
from setuptools import find_packages
import subprocess
import os

pycw_version = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as file:
    long_description = file.read()

setup(
    name='pyconnectwise',
    version=pycw_version,
    license='gpl-3.0',
    author="Health IT",
    author_email='dev@healthit.com.au',
    description='A full-featured Python client for the ConnectWise API\'s',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HealthITAU/pyconnectwise',
    keywords=['ConnectWise', 'Manage', 'Automate', 'API', 'Python', 'Client', 'Annotated', 'Typed', 'MSP'],
    install_requires=[
          'requests',
          'pydantic>=2',
          'jinja2'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',  
        'Intended Audience :: Developers',   
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.10',
    ],
    package_dir = {"":"src"},
    packages = find_packages(where="src"),
    python_requires = ">=3.10.1"
)