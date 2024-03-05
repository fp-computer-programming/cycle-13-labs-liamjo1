# Liam O'Hara

# Liam O'Hara

# Open the alma-mater.txt file in read mode
with open("alma-mater.txt", 'r') as file:
   # Iterate over each line in the file
   for line in file:
       # Print the current line
       print(line.strip())  # strip() removes leading/trailing whitespace
       # Print a blank line
       print()