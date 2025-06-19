import os
import subprocess

def run_python_file(working_directory, file_path):
    abfile = os.path.abspath(file_path)
    abwork = os.path.abspath(working_directory)
    abdir = os.path.dirname(abfile) 
    abworkdir = os.path.dirname(abwork)

    if not abdir.startswith(abworkdir):
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory') 
    if not os.path.exists(abfile): 
        return (f'Error: File "{file_path}" not found.') 
    if not file_path.endswith(".py"):
        return (f'Error: "{file_path}" is not a Python file.')

    tout = 30 

    try:
        result = subprocess.run(["python3", abfile], capture_output=True, timeout=tout)

    except Exception as e:
        return (f'Error: executing Python file: {e}')

    outstr = "" 
    
    soutput = result.stdout
    serr = result.stderr 
    rcode = result.returncode

    soutput = "STDOUT:" + str(result.stdout) + "\n"
    serr = "STDERR:" + str(result.stderr) + "\n"
    if result.returncode != 0: 
        nonzero = (f"Process exited with code {result.returncode}")
    else:
        nonzero = "" 
    
    if result.stdout + result.stderr == "":
        return "No output produced"
    else: 
        totout = soutput + serr + nonzero
        return totout 
    




