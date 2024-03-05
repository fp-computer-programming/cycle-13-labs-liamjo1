# Liam O'Hara

# Open the alma_mater.txt file in read mode
with open("alma_mater.txt", 'r') as file:
   # Read all lines from the file
   lines = file.readlines()

   # Reverse the order of lines
   lines.reverse()

   # Print each line in reverse order with a blank line between each line
   for line in lines:
       print(line.strip())  # strip() removes leading/trailing whitespace
       print()  # Print a blank line