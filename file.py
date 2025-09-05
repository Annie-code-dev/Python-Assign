def read_and_modify_file():
    filename = input("Enter file to read:")
    try:
        with open(filename,"r") as Psyannie:
            content = Psyannie.read()
            modified_content = content.upper()
            new_filename = "modified_" + filename
            with open(new_filename, "w") as new_file:
                new_file.write(modified_content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("Error:", e)