import os.path
import shutil

print("This program performs the functions of CAT command in LINUX")

print("1. Create an empty file")
print("2. Read a file")
print("3. Append to a file")
print("4. Copy the contents of file")

choice = input("Enter your desired operation(1, 2, 3, 4): ")

if choice == "1":
    print(" 1. TXT \n 2. PDF \n 3. JPG")
    file_format = input("Specify the format(1, 2, 3): ")
    if file_format == "1":
        f = open("created file.txt", "w")
        print("TXT file created.")
        f.close()
    elif file_format == "2":
        f = open("created file.pdf", "w")
        print("PDF file created.")
        f.close()
    elif file_format == "3":
        f = open("created file.jpg", "w")
        print("JPG file created")
        f.close()
    else:
        print("Wrong format. Terminating.")
elif choice == "2":
    file_name = input("Enter the name of the file with extension: ")
    file_status = os.path.isfile(file_name)     # to verify if the file exists, returns boolean value
    if file_status:
        f = open(file_name, "r")
        contents = f.read()
        print(contents)
        f.close()
        input("Press enter to exit" )
    else:
        print("Mentioned file does not exists. Creating new file.")
        f = open(file_name, "w")
        print("New file with name \"" + file_name + "\" created.")
        f.close()
elif choice == "3":
    file_name = input("Enter the name of the file with extension: ")
    f = open(file_name, "a")
    contents = input("Enter the data to appended: ")
    f.write(contents)
    f.close()
    f = open(file_name, "r")
    print("File after appending: \n" + f.read())
    f.close()
elif choice == "4":
    print("1. Append from file_1 to file_2")
    print("2. Over-write from file_1 to file_2")
    choice = input("Enter your choice(1, 2): ")
    name_file1 = input("Enter file_1 name: ")
    name_file2 = input("Enter file_2 name: ")
    if choice == "1":
        f1 = open(name_file1, "r")
        f2 = open(name_file2, "a")
        contents = f1.read()
        f2.write(contents)
        print(f2.read())
        f1.close()
        f2.close()
    elif choice == "2":
        shutil.copy(name_file1, name_file2)
        f = open(name_file2, "r")
        contents = f.read()
        print(contents)
    else:
        print("Wrong input. Terminating.")
        exit()
else:
    print("Wrong input. Terminating.")


