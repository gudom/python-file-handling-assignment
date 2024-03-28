try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("This is line 3 with some special characters: @#$%\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("This is line 4, appended.\n")
        file.write("67890\n")
        file.write("This is line 6, also appended.\n")

except FileNotFoundError:
    print("File not found. Please ensure the file exists.")
except PermissionError:
    print("Permission denied. Please check file permissions.")
except Exception as e:
    print("An error occurred:", e)

finally:
    print("File handling process completed.")
