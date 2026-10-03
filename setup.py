from setuptools import setup

setup(
    name='code2llm',
    version='0.1.0',
    author='Oladapo Salami',
    py_modules=['main', 'scanner'],
    install_requires=[
        'click',
        'rich',
        'pathspec',
        'pyperclip',
    ],
    entry_points={
        'console_scripts': [
            'code2llm = main:cli',
        ],
    },
)