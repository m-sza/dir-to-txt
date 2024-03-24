# dir-to-txt
A Python script that recursively traverses a directory, collects the contents of files into a single text file, and generates a directory tree structure. Allows filtering files by type and excluding specific files and directories.

This will traverse the `/path/to/your/directory` directory, exclude the `.git`, `node_modules`, and `.env` files/directories, and include only the files with extensions `.py` and `.txt`. The output will be saved to `output.txt`.

## Note

- The script attempts to handle files with different encodings (UTF-8 and Latin-1). If a file cannot be decoded using either encoding, it will be skipped, and a message will be printed indicating the skipped file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
