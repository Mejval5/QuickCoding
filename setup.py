from setuptools import setup, find_packages

setup(
    name="quick_coding",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
)
