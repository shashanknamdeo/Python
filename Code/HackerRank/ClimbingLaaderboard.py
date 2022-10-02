"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
Example



The ranked players will have ranks , , , and , respectively. If the player's scores are ,  and , their rankings after each game are ,  and . Return .

Function Description

Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):

int ranked[n]: the leaderboard scores
int player[m]: the player's scores
Returns

int[m]: the player's rank after each new score
Input Format

The first line contains an integer , the number of players on the leaderboard.
The next line contains  space-separated integers , the leaderboard scores in decreasing order.
The next line contains an integer, , the number games the player plays.
The last line contains  space-separated integers , the game scores.

Constraints

 for 
 for 
The existing leaderboard, , is in descending order.
The player's scores, , are in ascending order.
Subtask

For  of the maximum score:

Sample Input 1

CopyDownload
Array: ranked
100
100
50
40
40
20
10

 



Array: player
5
25
50
120

 
7
100 100 50 40 40 20 10
4
5 25 50 120
Sample Output 1

6
4
2
1
Explanation 1

Alice starts playing with  players already on the leaderboard, which looks like this:

image

After Alice finishes game , her score is  and her ranking is :

image

After Alice finishes game , her score is  and her ranking is :

image

After Alice finishes game , her score is  and her ranking is tied with Caroline at :

image

After Alice finishes game , her score is  and her ranking is :

image


Sample Input 2

CopyDownload
Array: ranked
100
90
90
80
75
60

 



Array: player
50
65
77
90
102

 
6
100 90 90 80 75 60
5
50 65 77 90 102
Sample Output 2

6
5
4
2
1
"""
def climbingLeaderboard(rank_list, player_score):
    rank_dict={}
    i=0
    temp_element=rank_list[0]+1
    for element in rank_list:
        if element < temp_element:
            rank_dict[i+1]=element
            temp_element=element
            temp_i=i+1
            i=temp_i
    #
    for score in player_score:
        temp_score=0
        for dict_score in rank_dict:
            if score>dict_score:
                if score < temp_score:
                    return rank_dict[temp_score]+1
                elif score == temp_score:
                    return rank_dict[temp_score]
            temp_score=dict_score




def climbingLeaderboard(rank_list, player_score):
    rank_dict={}
    i=0
    temp_element=rank_list[0]+1
    for element in rank_list:
        if element < temp_element:
            rank_dict[i+1]=element
            temp_element=element
            temp_i=i+1
            i=temp_i
    #
    print(rank_dict)
    for score in player_score:
        temp_score=0
        for dict_score in rank_dict:
            if score>rank_dict[dict_score]:
                if score < rank_dict[temp_score]:
                    print('if1')
                    print(temp_score+1)
                elif score ==rank_dict[temp_score]:
                    print('if2')
                    print(temp_score)
                elif score > rank_dict[temp_score]:
                    print('if3')
                    print(1)
            temp_score=dict_score



def ranking(rank_list):
    rank_dict={}
    i=0
    temp_element=rank_list[0]+1
    for element in rank_list:
        if element < temp_element:
            rank_dict[i+1]=element
            temp_element=element
            temp_i=i+1
            i=temp_i
    return rank_dict
