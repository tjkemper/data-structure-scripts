from setuptools import setup, find_packages

setup(
    name='data_structure_scripts',
    version=0.1,
    description='CLI for data structures.',
    author='Taylor Kemper',
    author_email='tjkemper6@gmail.com',
    url='https://github.com/tjkemper/data-structure-scripts',
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    tests_require=['pytest'],
    entry_points='''
        [console_scripts]
        maxheap=src.cli.commands:maxheap
        avl=src.cli.commands:avl
    ''',
)
