# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements

version = '0.7.0'
requirements = parse_requirements("requirements.txt", session="")

setup(
	name='release_test',
	version=version,
	description='Release Test',
	author='Revant',
	author_email='revant@revant.me',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.req) for ir in requirements],
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
