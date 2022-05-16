from src.unzip import unzip_all_files_in_directory

if __name__ == '__main__':
    # Print the program name
    print('UNZIP AND RENAME APP\n')
    # Ask the user for a directory
    zip_directory = input('Please, inform the directory where the zip files '
                          'are located:\n')
    # Ask for the files extension to filter
    extension = input('Please, inform the extension of the files you want to '
                      'extract:\n')
    # Extract files
    unzip_all_files_in_directory(zip_directory, extension, True)
    # Prints the success message
    print('All files extracted')
