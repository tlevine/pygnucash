from distutils.core import setup

setup(name='pygnucash',
      author='Matthias Braun',
      author_email='matze@braunis.de',
      description='read gnucash files in python',
      url='https://github.com/MatzeB/pygnucash',
      py_modules=['gnucash', 'gnucashutil'],
      scripts=['edit.py', 'gnucash2ledger.py', 'stockreport.py'],
      version='1.0.0',
      license='2-clause BSD',
)
