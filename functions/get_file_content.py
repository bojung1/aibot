import os 

def get_file_content(working_directory, file_path):
    abfile = os.path.abspath(file_path)

    if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):  
       return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if not os.path.isfile(abfile): 
        return (f'Error: File not found or is not a regular file: "{file_path}"') 

    MAX_CHARS = 10000

    try: 
        with open(abfile, "r") as f:
            file_content_string = f.read(MAX_CHARS)

    except Exception as e: 
        return (f'Error: {str(e)}') 

    return file_content_string
