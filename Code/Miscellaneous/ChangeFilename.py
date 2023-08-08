def changeNameOfFile(filename):
    temp_filename = filename.replace(" ", "")
    temp_filename = temp_filename.replace("_", "")
    if temp_filename.find("-") >= 0:
        temp_filename = temp_filename.replace("-", "(")
        temp_filename = temp_filename.replace(".",").")
    return temp_filename


path = r""
filename_list = os.listdir(path)
for filename in filename_list:
    old_name = os.path.join(path,filename)
    filename = changeNameOfFile(filename)
    new_name = os.path.join(path,filename)
    try:
        os.rename(old_name, new_name)
    except Exception as e:
        print(filename)
        pass

