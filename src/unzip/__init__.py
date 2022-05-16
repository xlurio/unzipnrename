import os
import zipfile


def unzip_file(zip_path, extension=None, rename_to_zipname=False):
    """Unzips specified files"""
    if '.' not in extension:
        raise ValueError("The specified extension must begin with a dot(.)")
    if extension:
        extension = extension.lower()

    if zipfile.is_zipfile(zip_path):
        if rename_to_zipname:
            # Get zip file name without the extension
            zip_filename = '.'.join(os.path.basename(zip_path).split('.')[:-1])

        with zipfile.ZipFile(zip_path) as zip_object:
            list_of_files = zip_object.namelist();
            unzip_to_directory = os.path.dirname(zip_path)
            unzip_to_directory = os.path.join(unzip_to_directory,
                                              'extracted_files')
            for file in list_of_files:
                if extension:
                    # Extract files with the specified extension
                    if file.lower().endswith(extension):
                        zip_object.extract(
                            member=file,
                            path=unzip_to_directory
                        )

                        # Rename file to the name of the zip file
                        if rename_to_zipname:
                            os.rename(
                                os.path.join(unzip_to_directory, file),
                                _get_new_name(
                                    os.path.join(unzip_to_directory,
                                                 zip_filename + extension)
                                )
                            )

                # Extract all files
                else:
                    zip_object.extractall(
                        path=unzip_to_directory
                    )


def unzip_all_files_in_directory(directory_path,
                                 extension=None,
                                 rename_to_zipname=False):
    """Unzips all zip files in a directory"""
    entries_in_directory = os.listdir(directory_path)
    for entry in entries_in_directory:
        if entry.lower().endswith('.zip'):
            zip_path = os.path.join(directory_path, entry)
            unzip_file(zip_path, extension, rename_to_zipname)


def _get_new_name(new_file_path, suffix=0):
    """Returns a valid file path"""
    if new_file_path:
        if suffix > 0:
            new_file_directory = os.path.dirname(new_file_path)
            new_file_basename = '.'.join(
                os.path.basename(new_file_path).split('.')[:-1]
            )
            new_file_extension = os.path.basename(new_file_path).split('.')[-1]
            new_file_name = (new_file_basename + f'({suffix})' + '.' +
                             new_file_extension)
            new_file_path = os.path.join(new_file_directory, new_file_name)

        if os.path.exists(new_file_path):
            suffix += 1
            return _get_new_name(new_file_path, suffix)
        else:
            return new_file_path
    else:
        raise ValueError(f'{new_file_path} is not a valid path')
