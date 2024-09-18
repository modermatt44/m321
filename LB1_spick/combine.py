import os
import glob

# Get a list of all markdown files in the current directory
markdown_files = glob.glob("*.md")

# Open the output file
with open("combined.md", "w") as outfile:
    # Iterate over the list of files
    for filename in markdown_files:
        # Open each file in read mode
        with open(filename, "r") as infile:
            # Read the content of the file
            content = infile.read()
            # Write the content to the output file
            outfile.write(content)
            # Add a newline character to separate the content of different files
            outfile.write("\n")