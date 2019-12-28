import requests
import os
import logging
import tarfile
import shutil


SOURCE_URL = "https://sparse.tamu.edu/"


def read_matrix_list_file(file_path):
    """
    Reads matrix names from the given file.

    Parameters:
    -----------
    file_path (string): source file's path

    Returns:
    --------
    matrices (array[][]<string>): matrix groups and names
    """

    if not os.path.exists(file_path):
        logging.critical("List file couldn't found exiting...")
        raise SystemExit()

    matrices = []

    with open(file_path) as list_file:
        content = list_file.read().splitlines()

    matrices = [tuple(line.split('/')) for line in content]
    return matrices


def download_data_files(matrix_list, destination=None, keep_archive_files=False):
    """
    Downloads the given list of matrices from SparseSuit Collection.

    Parameters:
    -----------
    matrix_list (array[][]<string>): matrix groups and names
    destination (string, optional): root dir path of data files, default=None
    keep_archive_files (bool, optinal): to save or remove downloaded archive files
                                        default=False
    """
    
    if not destination:
        destination = './'
        logging.info("`destination` paramater isn't provided. Downloading to `./`")

    os.makedirs('./archive', exist_ok=True)
    file_list = []

    for item in matrix_list:
        matrix_name = item[0] + '_' + item[1]
        matrix_url = SOURCE_URL + 'MM' + '/' + item[0] + '/' + item[1] + '.tar.gz'
        matrix_archive = requests.get(matrix_url)

        if matrix_archive.status_code == 200:
            tmp = './archive/' + matrix_name + '.tar.gz'
            with open(tmp, 'wb') as f:
                f.write(matrix_archive.content)
            file_list.append(tmp)
            logging.debug(matrix_name + " downloaded.")
        else:
            logging.warning(matrix_name + " couldn't download!")

    logging.info("Archive files downloaded successfully.")
    extract_archive_files(file_list, destination)

    if not keep_archive_files:
        shutil.rmtree('./archive')
        logging.info('Archive files deleted.')


def extract_archive_files(file_list, destination=None):
    """
    Extract downloaded archive files.

    Parameters:
    -----------
    file_list (string): list of archive files
    destination (string, optional): a path for extracting the archives into, default=None
    """

    for f in file_list:
        with tarfile.open(f, "r:gz") as tar:
            tar.extractall(path=destination)
            logging.debug("`" + f + '` extracted to ' + destination)

    logging.info("Archive files are extracted to: " + destination)
