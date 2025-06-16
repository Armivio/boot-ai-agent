import os

def get_files_info(working_directory, directory=None):
    
    abs_working_dir = os.path.abspath(working_directory)
    path = abs_working_dir
    if directory:
        path = os.path.abspath(os.path.join(working_directory, directory))
    # print(path)
    if not path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # path = os.path.join(abs_working_dir, directory)
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    # print(path)
    files = os.listdir(path)
    list_of_files_with_details = ""
    for file in files:
        list_of_files_with_details += f"- {file}: file_size={os.stat(os.path.join(path, file)).st_size} bytes, is_dir={os.path.isdir(os.path.join(path, file))}\n"
    return list_of_files_with_details