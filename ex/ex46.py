"""
0. Project skeleton can be found <here>/projects/skeleton

1. Get easy_install and pip using distribute package (NOT SETUPTOOL)
    1. Install distribute http://pypi.python.org/pypi/distribute
    
    2. (optional) if you are behind proxy, set this environmental variable: 'set http_proxy=http://username:my%20long%20password@proxy.whatever.com:80'
    
    3. run 'python distribute_setup.py' (see #4 if you encountered problem with proxy)

    4. Add F:\Interpreter\Python272\Scripts into path to access easy_install command

    5. Documentation for distribute is located http://packages.python.org/distribute/
    
    6. (not sure if this will be helpful) documentation for old 'easy_install' is located http://peak.telecommunity.com/DevCenter/EasyInstall
    
    7. Not fogetting run 'easy_install pip' to install pip
    
2. get nose and virtualenv
    1. pip install nose
    2. pip install virtualenv
    3. yes... that's all you need :)

3. These are descriptions of packages that need to be installed for ex46 and how to install it
    1. Distribute
    Distribute extends the packaging and installation facilities provided by the distutils in the standard library. Once you add Distribute to your Python system you can download and install any compliant Python software product with a single command. It also enables you to add this network installation capability to your own Python software with very little work.    
    Distribute is a fork of Setuptools
    Distribute is intended to replace Setuptools as the standard method for working with Python module distributions.
        Distribute is a drop-in replacement for Setuptools
        The code is actively maintained, and has over 10 commiters
        Distribute offers Python 3 support !
    2. pip
    pip installs packages. Python packages. An easy_install replacement.
    pip is better than easy_install because:
        All packages are downloaded before installation. Partially-completed installation doesn’t occur as a result.
        Care is taken to present useful output on the console.
        The reasons for actions are kept track of. For instance, if a package is being installed, pip keeps track of why that package was required.
        Error messages should be useful.
        The code is relatively concise and cohesive, making it easier to use programmatically.
        Packages don’t have to be installed as egg archives, they can be installed flat (while keeping the egg metadata).
        Native support for other version control systems (Git, Mercurial and Bazaar)
        Uninstallation of packages.
        Simple to define fixed sets of requirements and reliably reproduce a set of packages.
    pip however does not:
        It cannot install from eggs. It only installs from source. (In the future it would be good if it could install binaries from Windows .exe or .msi – binary install on other platforms is not a priority.)
        It doesn’t understand Setuptools extras (like package[test]). This should be added eventually.
        It is incompatible with some packages that extensively customize distutils or setuptools in their setup.py files.
    3. nose
    Nose for running unit test suites
    4. virtualenv
    The virtualenv kit provides the ability to create virtual Python environments that do not interfere with either each other, or the main Python installation. If you install virtualenv before you begin coding then you can get into the habit of using it to create completely clean Python environments for each project. This is particularly important for Web development, where each framework and application will have many dependencies.    
    
4. Using The Skeleton
    You are now done with most of your yak shaving. Whenever you want to start a new project, just do this:
        1. Make a copy of your skeleton directory. Name it after your new project.
        2. Rename (move) the NAME module to be the name of your project or whatever you want to call your root module.
        3. Edit your setup.py to have all the information for your project.
        4. Rename tests/NAME_tests.py to also have your module name.
        5. Double check it's all working using nosetests again.
        6. Start coding.

source: 
    http://guide.python-distribute.org/installation.html
    http://www.stuartellis.eu/articles/python-development-windows/
    http://guide.python-distribute.org/introduction.html#current-state-of-packaging (nice infographics)
    http://www.pip-installer.org/en/latest/other-tools.html#pip-compared-to-easy-install
    http://pypi.python.org/pypi/virtualenv/
        
"""