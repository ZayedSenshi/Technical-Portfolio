# Create empty lists to store names and dobs.
# Iterate through the txt file to access each line.
# Use strip and split to break them into components and store in variable.
# Store full name in variable by concatenating first and second index.
# Store ages by concatenating 3rd-5th index.
# Add a space in between the components.
# Use append method to add names to the empty lists.
# Print names and dobs using the for loop to iterate over created lists.
# Use relevant escape sequence to print headings in bold.

namelist = []
doblist = []

with open('DOB.txt', 'r+') as file:
    for line in file:
        components = line.strip().split()
        names = components[0] + " " + components[1]
        birthdates = components[2] + " " + components[3] + " " + components[4]

        namelist.append(names)
        doblist.append(birthdates)

# Now that names and DOBs are appropriately stored. Print separately.
print("\033[1m" + "Name" + "\033[0m")
for name in namelist:
    print(name)

print()

print("\033[1m" + "Birthdate" + "\033[0m")
for dobs in doblist:
    print(dobs)

