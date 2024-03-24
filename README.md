# Directory to Txt

This Python script traverses through the files and folders of a specified directory, collects the contents of each file into a single text file, and generates a directory tree structure. It allows you to exclude certain files and directories and select the file types to include in the output.

## Features

- Traverses through the files and folders of a specified directory
- Collects the contents of each file into a single text file
- Generates a directory tree structure in the output file
- Allows excluding specific files and directories
- Allows selecting the file types to include in the output
- Provides an option to include all file types by entering "all"
- Handles files with different encodings (UTF-8 and Latin-1)

## Usage

1. Run the script using a Python interpreter.
2. Enter the directory path when prompted.
3. Enter the desired output file name.
4. Enter the exception files/directories (comma-separated) to exclude from the output.
5. Enter the file types (comma-separated) to include in the output or enter "all" to include all file types.
6. The script will traverse the directory, collect the file contents, and generate the output file.

## Example

- Enter the directory path: /path/to/your/directory
- Enter the output file name: output.txt
- Enter exception files/directories (comma-separated): .git,.env
- Enter file types to include (comma-separated) or 'all' to include all file types: py, txt

This will traverse the `/path/to/your/directory` directory, exclude the `.git`, `node_modules`, and `.env` files/directories, and include only the files with extensions `.py` and `.txt`. The output will be saved to `output.txt`.

## Note

- The script attempts to handle files with different encodings (UTF-8 and Latin-1). If a file cannot be decoded using either encoding, it will be skipped, and a message will be printed indicating the skipped file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
