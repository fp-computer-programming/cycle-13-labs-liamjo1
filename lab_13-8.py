# Liam O'Hara

# Open a file for writing
with open("my_file.txt", 'w') as file:
   # Add three lines to the file
   file.write("LO 3/5/2024\n")  # My initials and today's date
   file.write("Hello World!\n")
   file.write("Playing rugby and being with friends\n")

# Confirm that the file is closed automatically after the 'with' block

# Alternatively, you can close the file explicitly using the close method
# file.close()