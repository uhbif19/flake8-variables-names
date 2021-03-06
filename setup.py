from typing import Optional

from setuptools import setup, find_packages


package_name = 'flake8_variables_names'


def get_version() -> Optional[str]:
    with open('flake8_variables_names/__init__.py', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('__version__'):
            return line.split('=')[-1].strip().strip("'")


def get_long_description() -> str:
    with open('README.md') as f:
        return f.read()


setup(
    name=package_name,
    description='A flake8 extension that helps to make more readable variables names',
    long_description=get_long_description(),
    packages=find_packages(),
    include_package_data=True,
    keywords='flake8 naming',
    version=get_version(),
    author='Ilya Lebedev',
    author_email='melevir@gmail.com',
    install_requires=['setuptools'],
    entry_points={
        'flake8.extension': [
            'VNE = flake8_variables_names.checker:VariableNamesChecker',
        ],
    },
    url='https://github.com/best-doctor/flake8-variables-names',
    license='MIT',
    py_modules=[package_name],
    zip_safe=False,
)
