from setuptools import setup

setup(
    name='CRUD em massa Bravas',
    version='1.0',
    packages=[''],
    url='https://github.com/Mezali/stunning-adventure.git',
    license='MIT',
    author='Mezali',
    author_email='danieldelimamazali@hotmail.com',
    description='Uma ferramenta GUI para realizar CRUDs em massa no módulo de acesso bravas',
    install_requires=[
        'openpyxl~=3.1.2',
        'urllib3~=2.0.2',
        'requests==2.30.0',
        'PyQt5~=5.15.9',
        # Outras dependências necessárias
    ],
    entry_points={
        'console_scripts': [
            'Massa Bravas=main.py:__main__',
        ],
    },
)
