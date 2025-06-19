from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file 
from functions.run_python import run_python_file

# this doesn't work
#print(get_files_info("calculator", "."))

#this will 
#print(get_files_info("calculator", "calculator"))
#print(get_files_info("calculator", "calculator/pkg"))
#print(get_files_info("calculator", "/bin"))
#print(get_files_info("calculator", "../"))

#print(get_file_content("calculator", "calculator/lorem.txt"))
#print(get_file_content(".", "main.py"))
#print(get_file_content("calculator", "calculator/main.py")) 
#print(get_file_content("calculator", "calculator/pkg/calculator.py"))
#print(get_file_content("calculator", "/bin/cat"))

#print(write_file("calculator", "calculator/lorem.txt", "wait, this isn't lorem ipsum"))
#print(write_file("calculator", "calculator/pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

print(run_python_file("calculator", "calculator/main.py"))
print(run_python_file("calculator", "calculator/tests.py"))
print(run_python_file("calculator", "../main.py")) #error
print(run_python_file("calculator", "nonexistent.py")) #error
