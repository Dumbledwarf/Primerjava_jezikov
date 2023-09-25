def count_non_empty_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                if line.strip():
                    line_count += 1
            return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1

# List of file paths
file_paths = ["Kadan.c","Kadan.go","Kadan.java","Kadan.py"]

for file_path in file_paths:
    line_count = count_non_empty_lines(file_path)
    if line_count >= 0:
        print(f"Number of non-empty lines in '{file_path}': {line_count}")
    print()  # Print an empty line for separation
