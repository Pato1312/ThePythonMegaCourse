"""
To open a file you need to use the open() function, and specify the file direction, if the file has the same directory 
as the program you can only use the name 

To get the conted inside the file you can use the read() function
"""

"""
my_file = open(
    "C:\\Users\\pato1\\OneDrive\\Documentos\\PythonMegaCourse\\modules\\module 11\\fruits.txt"
)

content = my_file.read()

my_file.close()

print(content)

print()
"""

with open(
    "C:\\Users\\pato1\\OneDrive\\Documentos\\PythonMegaCourse\\modules\\module 11\\vegetables.txt",
    "w+",
) as my_file:
    my_file.write("Tomato\n")
    my_file.write("Onion\n")
    my_file.write("Lettuce\n")

    my_file.seek(0)  # let's go to the start of the file to read
    content = my_file.read()

print(content)
