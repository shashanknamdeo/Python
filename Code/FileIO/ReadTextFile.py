file_name=r'C:\Users\Notebook\Downloads\Orders\Orders01.csv'
with open(file_name, 'r') as input_file:
    lines = input_file.read().splitlines()


# To print file data
"""here file is a list as lines are its elements,we need to convert list element into lines"""
# Methord 1
for r in range(0,len(lines)):
     print(lines[r])

# Methord 2
for line in file:
    print(line)