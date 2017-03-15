from setuptools import setup, find_packages

setup(
    name='data_structure_scripts',
    version=0.1,
    #packages=find_packages(),
    #include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        maxheap=src.cli.commands:maxheap
        avl=src.cli.commands:avl
    ''',
)
