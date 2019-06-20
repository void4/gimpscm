from setuptools import setup
setup(
  name = 'gimpscm',         # How you named your package folder (MyLib)
  packages = ['gimpscm'],   # Chose the same as "name"
  version = '1.2',      # Start with a small number and increase it with every change you make
  license='CC BY-NC 3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Automatically generate and execute gimp script files',   # Give a short description about your library
  author = 'void4',                   # Type in your name
  author_email = 'void4.noreply@github.io',      # Type in your E-Mail
  url = 'https://github.com/void4/gimpscm',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/void4/gimpscm/archive/1.2.tar.gz',
  keywords = ['gimp', 'image', 'editing'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',

    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license

    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  include_package_data=True,
)
