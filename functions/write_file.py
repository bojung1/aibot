import os

def write_file(working_directory, file_path, content): 
    abfile = os.path.abspath(file_path)
    abwork = os.path.abspath(working_directory)
    abdir = os.path.dirname(abfile)

    if not abfile.startswith(abwork):
        return (f'Error: Cannot write to "{abfile}" as it is outside the permitted working directory')
    if not os.path.exists(abdir):
        try: 
            os.makedirs(abdir)
        except Exception as e:
            return (f'Error: {str(e)}') 
    try: 
        with open(file_path, "w") as f:
            f.write(content)
    except Exception as ee:
        return (f'Error: {str(ee)}')

    return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)') 

