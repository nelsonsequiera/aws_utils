import os
import re
import setuptools


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(ROOT, 'aws_utils', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setuptools.setup(
    name='aws_utils_for_lambda',
    version=get_version(),
    scripts=[],
    author="Nelson Sequiera",
    author_email="nelsonsequiera@gmail.com",
    description="AWS utils for lambda",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nelsonsequiera/aws_utils_for_lambda",
    packages=setuptools.find_packages(),
    install_requires=[
        "boto3==1.9.120"
    ],
    python_requires='>=2.7',
    classifiers=[
        "Programming Language :: Python :: 3, 2.7",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
)
