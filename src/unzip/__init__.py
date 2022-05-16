import os
import zipfile


def unzip_file(zip_path, extension=None, rename_to_zipname=False):
    """Unzips specified files"""
    if '.' not in extension:
        raise ValueError("The specified extension must begin with a dot(.)")

    if zipfile.is_zipfile(zip_path):
        if rename_to_zipname:
            # Get zip file name without the extension
            zip_filename = ''.join(os.path.basename(zip_path).split('.')[:-1])
        with zipfile.ZipFile(zip_path) as zip_object:
            listOfFiles = zip_object.namelist();
            for file in listOfFiles:
                if extension:
                    # Extract files with the specified extension
                    if file.endwith(filter):
                        zip_object.extract(
                            member=file,
                            path='zip_filename/'
                        )

                # Extract all files
                else:
                    zip_object.extractall(
                        path='zip_filename/'
                    )

                # Rename file to the name of the zip file
                if rename_to_zipname:
                    os.rename(file, zip_filename + extension)


def unzip_all_files_in_directory(directory_path,
                                 extension=None,
                                 rename_to_zipname=False):
    """Unzips all zip files in a directory"""
    entries_in_directory = os.listdir(directory_path)
    for entry in entries_in_directory:
        if os.isfile(entry) and entry.endwith('.zip'):
            unzip_file(entry, extension, rename_to_zipname)
