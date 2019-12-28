Suite Downloader
===============

This is a small program that helps you to download given list of matrices from the
[SuiteSparse matrix collection](https://sparse.tamu.edu/) <sup>[1]</sup>.

### Installation
##### Install from source
``` sh
git clone https://github.com/talhaokur/sdownloader.git
cd sdownloader
python3 setup.py install

```

##### Install from PyPI
``` sh
pip3 install sdownloader
```

### Usage
``` sh
usage: sdownloader [-h] -f LIST_FILE [-d DESTINATION] [-v]

Data downloader from SparseSuite.

optional arguments:
  -h, --help            show this help message and exit
  -f LIST_FILE, --list-file LIST_FILE
                        matrix name list file destination.
  -d DESTINATION, --destination DESTINATION
                        destination path.
  -v, --verbose         toggle verbose mode. Enters the DEBUG mode

```

### Todo
- [X] Check internet connection
- [X] Control unit for checking if current version is the latest one
- [X] Upload to PyPI
- [ ] Single data download mode


### References
[1]: Timothy  A.  Davis  and  Yifan  Hu.  “The  University  of Florida  Sparse  Matrix  Collection”.  In: ACM  Trans. Math. Softw. 38.1 (Dec. 2011), 1:1–1:25. ISSN : 0098-3500. DOI : 10.1145/2049662.2049663. URL : http://doi.acm.org/10.1145/2049662.2049663 . 
