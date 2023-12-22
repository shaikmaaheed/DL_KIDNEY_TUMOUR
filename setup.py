from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0.0"

REPO_NAME = "DL_KIDNEY_TUMOUR"
AUTHOR_USER_NAME= "shaikmaaheed"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "shaikmaaheed@gamail.com"


setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app (personal learning)",
    long_description=long_description,
    long_description_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"}, 
    packages=find_packages(where="src")
)