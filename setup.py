from setuptools import setup, find_packages

setup(
    name='AI_Coder',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ai-project=ai_project.cli:main',
        ],
    },
    install_requires=[],
)