
# https://docs.google.com/spreadsheets/d/1hXserPuxVoWMG9Hs7y8wVdRCJTcj3xMBAEYUOXQ5Xag/edit?gid=0#gid=0

# last date 6

def clean_string(string):
    result = ''
    for char in string:
        if char.isalpha() or char.isnumeric():  # keeps only A-Z and a-z
            result += char
    return result


def isPalindrome(string):
    """
    """
    string = clean_string(string=string)
    string = string.lower()
    len_string = len(string)
    # 
    left  = 0
    right = len_string -1
    # 
    while left < right:
        if string[left] == string[right]:
            left  += 1
            right -= 1
        else:
            return False
    # 
    return True


s = ' '

print(isPalindrome(string=s))