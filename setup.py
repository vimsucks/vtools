from setuptools import setup

setup(
    name = 'vtools',
    version = '0.1.0',
    keywords='tools utils',
    description = 'useless tool set',
    license = 'MIT License',
    url = 'https://github.com/vimsucks/vtools',
    author = 'Vimsucks',
    author_email = 'dev@vimsucks.com',
    zip_safe = False,
    packages = ["vtools"],
    package_dir={'vtools': 'vtools'},
    install_requires = [],
)
