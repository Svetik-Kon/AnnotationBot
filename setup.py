from setuptools import setup, find_packages

# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()

setup(
    name='AnnotationBot',
    version='1.0.0',
    packages=find_packages(),
    # install_requires=requirements,
    entry_points={
        'console_scripts': [
            'my_project = main:main',  # Замените main на имя вашего основного модуля
        ],
    },
)
