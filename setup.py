from setuptools import setup

setup(
    name='keydecomposer',
    version='0.1.0',
    description='A set of functions to find the smallest unique column set in a pandas dataframe',
    url='https://github.com/DocSchlock/KeyDecomposer-py',
    author='Andrew Schlachter',
    author_email='',
    license='BSD 3-clause',
    packages=['keydecomposer'],
    python_requires =">=3.9",
    install_requires=['pandas>=1.3.0',
                      'typing',
                      ],

    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
)
