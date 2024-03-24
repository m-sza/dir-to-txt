import os


def print_directory_tree(directory, output_file, exceptions, file_types, level=0):
    """
    Prints the directory tree structure to the output file.

    Args:
        directory (str): The path to the directory.
        output_file (TextIOWrapper): The file object to write the output.
        exceptions (list): A list of exception files/directories to exclude.
        file_types (list): A list of file types to include.
        level (int): The current indentation level.
    """
    # Print the directory name at the top level
    if level == 0:
        output_file.write(f"{os.path.basename(directory)}\n")

    # Iterate over the items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # If the item is a directory and not in the exceptions list
        if os.path.isdir(item_path) and item not in exceptions:
            # Write the directory name with appropriate indentation
            output_file.write("│   " * level + "├── " + item + "/\n")
            # Recursively call the function for the subdirectory
            print_directory_tree(item_path, output_file, exceptions, file_types, level + 1)
        # If the item is a file and its type is in the file_types list or file_types contains "all"
        elif os.path.isfile(item_path) and (file_types == ["all"] or item.split('.')[-1] in file_types):
            # Write the file name with appropriate indentation
            output_file.write("│   " * level + "├── " + item + "\n")


def collect_file_contents(directory, output_file, exceptions, file_types):
    """
    Collects the contents of files in the specified directory and writes them to the output file.

    Args:
        directory (str): The path to the directory.
        output_file (str): The name of the output file.
        exceptions (list): A list of exception files/directories to exclude.
        file_types (list): A list of file types to include.
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Print the directory tree structure to the output file
        print_directory_tree(directory, outfile, exceptions, file_types)

        # Write a separator line
        outfile.write("\n" + "=" * 50 + "\n\n")

        # Walk through the directory tree
        for root, dirs, files in os.walk(directory):
            # Exclude directories mentioned in the exceptions list
            dirs[:] = [d for d in dirs if d not in exceptions]

            # Iterate over the files in the current directory
            for file in files:
                # If the file is not in the exceptions list and its type is in the file_types list or file_types contains "all"
                if file not in exceptions and (file_types == ["all"] or file.split('.')[-1] in file_types):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, directory)

                    try:
                        # Try opening the file with UTF-8 encoding
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            # Write the file path and contents to the output file
                            outfile.write(f"File: {relative_path}\n\n")
                            outfile.write(infile.read())
                            outfile.write("\n\n" + "-" * 50 + "\n\n")
                    except UnicodeDecodeError:
                        try:
                            # If UTF-8 fails, try opening the file with Latin-1 encoding
                            with open(file_path, 'r', encoding='latin-1') as infile:
                                # Write the file path and contents to the output file
                                outfile.write(f"File: {relative_path}\n")
                                outfile.write(infile.read())
                                outfile.write("\n\n" + "-" * 50 + "\n\n")
                        except UnicodeDecodeError:
                            # If both encodings fail, skip the file and print a message
                            print(f"Skipping file: {relative_path} (unsupported encoding)")


# Get user input
directory = input("Enter the directory path: ")
output_file = input("Enter the output file name: ")
exceptions = input("Enter exception files/directories (comma-separated): ").split(',')
file_types = input("Enter file types to include (comma-separated) or 'all' to include all file types: ").split(',')

# Clean up the user input
exceptions = [exc.strip() for exc in exceptions]
file_types = [ft.strip() for ft in file_types]

# Call the function to collect file contents
collect_file_contents(directory, output_file, exceptions, file_types)
print(f"File contents collected and saved to {output_file}")