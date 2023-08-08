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

# List of directories and files
dir_list = os.listdir(path) 

# Save file at dir
def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)

# Creates a new file
with open('myfile.txt', 'w') as fp:
    pass
    # To write data to new file uncomment
    # this fp.write("New file created")

# Check whether the path is a file
isFile = os.path.isfile(path)