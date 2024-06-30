"""

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.

"""


def createSublistsOfAList(element_list):
    """
    """
    sublist_list = []
    # 
    for i in range(0,len(element_list)):
        temp_list_1 = element_list[i:len(element_list)]
        # 
        for r in range(0,len(temp_list_1)):
            temp_list_2 = temp_list_1[0:len(temp_list_1)-r]
            sublist_list.append(temp_list_2)
    # 
    return sublist_list


def minion_game(string):
    """
    """
    string_list = list(string.lower())
    sublist_list = createSublistsOfAList(element_list=string_list)
    # 
    Vowel_list = ['a','e','i','o','u']
    # 
    stuart_point = 0
    kevin_point = 0
    # 
    for sublist in sublist_list:
        if sublist[0] in Vowel_list:
            kevin_point = kevin_point + 1
        # 
        else:
            stuart_point = stuart_point + 1
    # 
    if stuart_point > kevin_point:
        return 'Stuart ' + str(stuart_point)
    # 
    elif kevin_point > stuart_point:
        return 'Kevin ' + str(kevin_point)
    # 
    elif kevin_point == stuart_point:
        return 'Draw'


def sublists(lst):
    n = len(lst)
    sublists = []
     
    for start in range(n):
        for end in range(start + 1, n + 1):
            sublists.append(lst[start:end])
     
    return sublists


def minion_game(string):
    """
    """
    sublist_list = sublists(lst=string.lower())
    # 
    Vowel_list = ['a','e','i','o','u']
    # 
    stuart_point = 0
    kevin_point = 0
    # 
    for sublist in sublist_list:
        if sublist[0] in Vowel_list:
            kevin_point = kevin_point + 1
        # 
        else:
            stuart_point = stuart_point + 1
    # 
    if stuart_point > kevin_point:
        return 'Stuart ' + str(stuart_point)
    # 
    elif kevin_point > stuart_point:
        return 'Kevin ' + str(kevin_point)
    # 
    elif kevin_point == stuart_point:
        return 'Draw'
