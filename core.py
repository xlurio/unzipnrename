from src.unzip import unzip_all_files_in_directory

if __name__ == '__main__':
    print('UNZIP AND RENAME APP')
    # Ask the user for a directory
    zip_directory = input('Please, inform the directory where the zip files '
                          'are located')
    unzip_all_files_in_directory(zip_directory)
