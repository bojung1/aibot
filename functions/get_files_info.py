import os 

def get_files_info(working_directory, directory=None):
    if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):  
       return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(directory): 
        return (f'Error: "{directory}" is not a directory') 

    apdir = os.path.abspath(directory)

    out = "" 
    for a in os.listdir(apdir):
        b = os.path.join(apdir, a)
        try: 
            isd = os.path.isdir(b)
        except:
            return (f'Error: Could not determine if "{a}" is a directory') 

        if isd != True: 
            try:
                fsize = os.path.getsize(b)
            except:
                return (f'Error: Could not get size of file called {a}') 
        else: 
            fsize = 128
        out += "- "
        out += a
        out += ": file_size="
        out += str(fsize)
        out += " bytes, is_dir="
        out += str(isd)
        out += "\n"

    return out 


    
