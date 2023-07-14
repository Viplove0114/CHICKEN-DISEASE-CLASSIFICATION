import setuptools

with open("README.md", "r", encoding ="utf-8") as f:
    long_description = f.read()

__version__ = 0.0.1

REPO_NAME = "CHICKEN-DISEASE-CLASSIFICATION"
AUTHOR_USER_NAME = "Viplove0114"
SRC_REPO = "chicken_classifier"
AUTHOR_EMAIL = "viplovethakran4@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__
    author=AUTHOR_USER_NAME
    author_email=AUTHOR_EMAIL
    description="A small python pakage for CNN app",
    Long_description=long_description,
    Long_description_content="txt/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    project_url={
    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO}/issues",
    }
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where="src")

)
