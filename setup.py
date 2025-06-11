from setuptools import setup, find_packages

setup(
    name='ai_coder',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'echo-app=ai_coder.cli:main',
        ],
    },
    install_requires=[
        'pytest',
        'asyncio',
    ],
)