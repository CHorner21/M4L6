# Step 1: Write to learning_python.txt
with open('learning_python.txt', 'w') as file:
    file.write("In Python you can...\n")
    file.write("In Python you can also...\n")
    file.write("Python is a versatile programming language.\n")

# Step 2: Read and print the content three times
# Method 1: Read the entire file
with open('learning_python.txt', 'r') as file:
    content = file.read()
    print("Reading the entire file:")
    print(content)

# Method 2: Loop over the file object
with open('learning_python.txt', 'r') as file:
    print("\nLooping over the file object:")
    for line in file:
        print(line, end='')

# Method 3: Store lines in a list and work with them outside the with block
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()
    print("\nWorking with lines outside the with block:")
    for line in lines:
        print(line, end='')

# Step 3: Replace 'Python' with another language (e.g., PHP)
with open('learning_python.txt', 'r') as file:
    modified_lines = [line.replace('Python', 'PHP') for line in file]
    print("\n\nReplacing 'Python' with 'PHP':")
    for modified_line in modified_lines:
        print(modified_line, end='')

# Note: You can take a screenshot of the executed code in your Python environment.

