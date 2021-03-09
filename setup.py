from setuptools import setup, find_packages


with open("README.rst") as f:
    long_desc = f.read()


setup(
    name="sphinxcontrib-bibtexpdflink",
    version="0.1.6",
    author="Jeff Teeters",
    author_email="jeff@teeters.us",
    license="MIT",
    description="Sphinx extension to add links to PDF and note files to BiBTeX style citations",
    long_description=long_desc,
    install_requires=["Sphinx>=2.0", "sphinxcontrib-bibtex==1.0.0",],
    # zip_safe=False,
    packages=find_packages(),
    namespace_packages=["sphinxcontrib"],
    # package_data={"sphinxcontrib": ["*.css", "*.js"]},
    # project_urls={
    #     "Documentation": "https://sphinxcontrib-temptestplatformpicker.readthedocs.io/",
    #     "Source Code": "https://github.com/jeffteeters/sphinxcontrib-temptestplatformpicker",
    #     "Bug Tracker": "https://github.com/jeffteeters/sphinxcontrib-temptestplatformpicker/issues",
    # },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
)
