try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project for ex 47',
    'author' : 'Aditya',
    'url' : 'http://adityalesmana.com',
    'download_url' : 'http://adityalesmana.com',
    'author_email' : 'alesmana@gmail.com',
    'version' : '0.0',
    'install_requires' : ['nose'],
    'packages' :  ['ex47'],
    'scripts' : [],
    'name' : 'ex47_project'
}

setup(**config)

