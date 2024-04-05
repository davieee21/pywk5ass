# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Line 1: file name no. 3.")
            file.write("Line 2: 12345")
            file.write("Line 3: Python 3.")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    else:
        print("File 'my_file.txt' created successfully!")


# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Contents of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    else:
        print("File read successfully!")


# File Appending
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Line 4: Appended line.")
            file.write("Line 5: 98765")
            file.write("Line 6: Another appended line.")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    else:
        print("Content appended to 'my_file.txt' successfully!")


# Error Handling
def main():
    create_file()
    read_file()
    append_file()


if __name__ == "__main__":
    main()
