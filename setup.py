try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

VERSION = '0.0.1'
DOCUMENTATION = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
	name='django-lab',
	packages=['django_lab'],
	version=VERSION,
	author='Bogdan Opanchuk',
	author_email='mantihor@gmail.com',
	url='http://github.com/Manticore/django_lab',
	description='Virtual lab application for Django CMS',
	long_description=DOCUMENTATION,
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Web Environment',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Topic :: Scientific/Engineering :: Physics'
	]
)
