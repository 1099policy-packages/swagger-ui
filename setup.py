import platform
from pathlib import Path

from setuptools import find_packages, setup
from distutils.version import StrictVersion


if StrictVersion(platform.python_version()) < StrictVersion('3.0.0'):
    raise Exception("`t99-swagger-ui` support python version >= 3.0.0 only.")

setup(
    name='t99-swagger-ui',
    version='21.12.08',
    description=(
        'Swagger UI for Python web framework (masonite)'
    ),
    long_description=Path(__file__).parent.joinpath('README.md').read_text(),
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    packages=find_packages(),
    package_data={
        'src': ['static/*', 'templates/*'],
    },
    install_requires=[
        "jinja2>=2.0",
        "PyYaml>=5.0",
    ],
    url='https://https://github.com/1099policy-packages/swagger-ui',
    author='cfkarakulak',
    author_email='cradexco@gmail.com',
)
