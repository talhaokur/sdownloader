import argparse
import logging
import os
from . import fetch, utils

def main():
    parser = argparse.ArgumentParser(
        prog="sdownloader", 
        description="Data downloader from SparseSuite.")
    parser.add_argument("-f", "--list-file", help="matrix name list file destination.", required=True)
    parser.add_argument("-d", "--destination", help="destination path.", default=os.getcwd())
    parser.add_argument("-v", "--verbose", help="toggle verbose mode. Enters the DEBUG mode", action="store_true")

    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO

    logging.basicConfig(level = log_level, format="[%(asctime)s]:%(levelname)s:%(message)s", datefmt='%H:%M:%S')

    if not utils.check_internet_connection():
        logging.critical("Can not connect to the Internet")
        raise SystemExit("Can not connect to the Internet, please check your connection. Exiting...")

    utils.check_version()
    matrices = fetch.read_matrix_list_file(args.list_file)
    fetch.download_data_files(matrices, destination=args.destination, keep_archive_files=False)

if __name__ == "__main__":
    main()