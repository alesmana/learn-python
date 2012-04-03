try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'Aditya',
    'url' : 'http://adityalesmana.com',
    'download_url' : 'http://adityalesmana.com',
    'author_email' : 'alesmana@gmail.com',
    'version' : '0.0',
    'install_requires' : ['nose'],
    'packages' :  ['NAME'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config)

