from setuptools import setup, find_packages

setup(name="sdownloader",
      version="0.1.0",
      description="A little program to download given list of matrices from SuiteSparse.",
      url="https://github.com/talhaokur/sdownloader",
      author="Talha Okur",
      author_email="talhao@acm.org",
      license="MIT",
      packages=find_packages(),
      install_requires=[
          "requests",
      ],
      python_requires=">=3",
      classifiers=[
          "Programming Language :: Python :: 3",
          "Development Status :: 2 - Pre-Alpha",
          "Environment :: Console",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Intended Audience :: End Users/Desktop",
      ],
      entry_points={
          'console_scripts': [
              'sdownloader=src.main:main',],
              },
      )
