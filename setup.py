from setuptools import setup, find_packages

setup(name="suite_downloader",
      version="0.1.0",
      description="A little program to download given list of matrices from SuiteSparse.",
      url="https://github.com/talhaokur/suite_downloader",
      author="Talha Okur",
      author_email="talhao@acm.org",
      license="MIT",
      packages=find_packages(where='./'),
      install_requires=[
          "requests",
      ],
      python_requires=">=3",
      entry_points={
          'console_scripts': [
              'suite_downloader=src.main:main',],
              },
      )
