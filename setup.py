from setuptools import setup, find_packages


setup(
    name='sandbox_package',  # Remplacez par le nom de votre package
    version='0.0.1',  # La version de votre package
    packages=find_packages(),  # Trouve automatiquement tous les packages
    license='VISIOOS',  # Licence sous laquelle est distribué votre package
    description='package sandbox',  # Une courte description
    long_description=open('README.md').read(),  # Une description longue depuis le README
    long_description_content_type='text/markdown',  # Type de contenu pour la description longue
    author='Yann',  # Votre nom
    author_email='',  # Votre email
    url='https://github.com/yg-c/sandbox_package',  # L'URL du projet
    install_requires=open('requirements.txt').read().splitlines(),  # Les dépendances
    classifiers=[  # Classificateurs pour décrire votre projet
        'Development Status :: 3 - Alpha',  # Le stade de développement
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)