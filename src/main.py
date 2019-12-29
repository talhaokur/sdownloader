import argparse
import logging
import os
from . import fetch, utils, __version__

def main():
    parser = argparse.ArgumentParser(
        prog="sdownloader", 
        description="Data downloader from SparseSuite.")
    parser.add_argument("-V", "--verbose", help="toggle verbose mode.", action="store_true")
    parser.add_argument('-v', '--version', action='version', version="%(prog)s ("+__version__+")")

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