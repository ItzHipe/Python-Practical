# Write and append to a text file
with open("sample.txt", "w") as f:
    f.write("This is a sample file.\n")

with open("sample.txt", "a") as f:
    f.write("Appending a line to the file.\n")

# Read from the file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)

# Copy content to a new file
with open("sample.txt", "rb") as src_file:
    with open("copy_sample.txt", "wb") as dest_file:
        dest_file.write(src_file.read())
