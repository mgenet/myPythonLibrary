import datetime
import os
import setuptools

# version = os.environ['CI_COMMIT_TAG']
version = datetime.date.today().strftime("%Y.%m.%d")

setuptools.setup(
    name="myPythonLibrary",
    version=version,
    author="Martin Genet",
    author_email="martin.genet@polytechnique.edu",
    description=open("README.md", "r").readlines()[1][:-1],
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.inria.fr/mgenet/myPythonLibrary",
    packages=["myPythonLibrary"],
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy'],
    # python_requires='>=3.6',
)

# keyring set https://upload.pypi.org/legacy martin.genet
# keyring set https://upload.pypi.org martin.genet

# python setup.py sdist bdist_wheel

# twine upload dist/*

# twine upload --repository-url https://gitlab.inria.fr/api/v4/projects/myPythonLibrary/packages/pypi dist/*
