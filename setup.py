from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in picklist/__init__.py
from picklist import __version__ as version

setup(
	name="picklist",
	version=version,
	description="Pick list",
	author="mismail@anvilerp.com",
	author_email="mismail@anvilerp.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
