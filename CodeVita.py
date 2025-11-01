# unable to give effecient code in python

"""

Uno Game

Problem Description
It was a lazy Sunday, and Dhruv was feeling bored. He picked up his phone and sent a message in his group, inviting anyone interested in playing Uno to come over. Within a few minutes, N children from the neighbourhood arrived to join the fun.

Among the group, there are some friends-pairs and some rivals-pairs.

Friends: If one friend is selected, the other must also be selected into the game. Each friends pair always consists of exactly two members, and no person can belong to more than one friends pair. For example, if (A, B) is a friend pair, neither A nor B will appear in any other friend pair.
Rivals: Both members of a rival pair cannot be selected into the team.
Each player has a uno score representing their skill level. Dhruv sets a limit for the team's total uno score and tries to select the maximum number of players without exceeding that limit.

Dhruv wanted to start the game quickly, but he is unsure which players to pick. Can you help him choose the optimal team?

Constraints
1 <= length of player name <= 10

1 <= max limit Dhruv set <= 1000

1 <= skill level of each player <= 100

1 <= total number of players <= 25

1 <= number of friends + number of rival pairs <= 10

Input
The first line contains an integer N, the total number of players.

The second line contains N space-separated strings, representing the player's names.

The third line contains N space-separated integers, representing the skill level of each corresponding player.

The fourth line contains an integer N1, the number of friend pairs.

The next N1 lines each contain two space-separated names, representing a pair of friends.

The following line contains an integer N2, the number of rival pairs.

The next N2 lines each contain two space-separated names, representing a pair of rivals.

The last line contains a single integer, representing the skill limit set by Dhruv.

Output
Print the maximum number of players Dhruv can select obeying the friend, rival, and the skill limit rules.

Time Limit (secs)
1

Examples
Example 1

Input

10

Ram Raj Vishnu Teja Alekhya Keerti Ganesh Seetha Rakesh Latha

1 2 3 4 5 6 7 8 9 1

2

Ram Latha

Alekhya Keerti

3

Ram Teja

Raj Rakesh

Seetha Raj

10

Output

4

Explanation

Dhruv can form a team consisting of {Ram, Latha, Raj, Vishnu} that follows all the friends and rival rules. The combined skill value of this team is 1 + 1 + 3 + 4 = 9, which is within the limit of 10. Therefore, Dhruv can select a maximum of 4 players, and no other combination can include more people than this.

Example 2

Input

8

Aarav Maya Rohan Neha Karan Sana Vikram Isha

1 4 9 10 11 17 2 6

2

Aarav Isha

Maya Karan

2

Aarav Neha

Rohan Neha

80

Output

7

Explanation

Within the skill limit, Dhruv can select everyone except Neha. So, the maximum number of players he can select is 7, hence print the same.


C++ code


#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p;
    DSU(int n): p(n) { iota(p.begin(), p.end(), 0); }
    int find(int x) { return p[x]==x?x:p[x]=find(p[x]); }
    void unite(int a, int b) {
        a=find(a); b=find(b);
        if(a!=b) p[b]=a;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if(!(cin >> n)) return 0;

    vector<string> names(n);
    vector<int> skill(n);
    for(int i=0;i<n;i++) cin >> names[i];
    for(int i=0;i<n;i++) cin >> skill[i];

    unordered_map<string,int> name_to_idx;
    for(int i=0;i<n;i++) name_to_idx[names[i]] = i;

    int n1; cin >> n1;
    DSU dsu(n);
    for(int i=0;i<n1;i++){
        string a,b; cin>>a>>b;
        dsu.unite(name_to_idx[a], name_to_idx[b]);
    }

    int n2; cin >> n2;
    vector<pair<int,int>> rivals;
    for(int i=0;i<n2;i++){
        string a,b; cin>>a>>b;
        rivals.push_back({name_to_idx[a], name_to_idx[b]});
    }

    int limit; cin >> limit;

    // build friend groups
    unordered_map<int, vector<int>> groups;
    for(int i=0;i<n;i++) groups[dsu.find(i)].push_back(i);

    int g = groups.size();
    vector<int> weights(g,0), counts(g,0);
    vector<int> group_id(n);
    int idx=0;
    unordered_map<int,int> root_to_gid;
    for(auto &kv: groups){
        root_to_gid[kv.first]=idx;
        for(int x: kv.second){
            weights[idx]+=skill[x];
            counts[idx]++;
            group_id[x]=idx;
        }
        idx++;
    }

    // rival check
    vector<int> rival_mask(g,0);
    for(auto &r: rivals){
        int ga = group_id[r.first];
        int gb = group_id[r.second];
        if(ga==gb){ cout<<0<<"\n"; return 0; }
        rival_mask[ga] |= (1<<gb);
        rival_mask[gb] |= (1<<ga);
    }

    int MAX_MASK = 1<<g;
    const int INF = 1e9;
    vector<int> dp_skill(MAX_MASK, INF);
    vector<int> dp_players(MAX_MASK, 0);
    dp_skill[0]=0;

    for(int mask=0; mask<MAX_MASK; mask++){
        if(dp_skill[mask]>limit) continue;
        for(int i=0;i<g;i++){
            if(mask & (1<<i)) continue;
            if(mask & rival_mask[i]) continue;
            int new_mask = mask | (1<<i);
            int new_skill = dp_skill[mask] + weights[i];
            if(new_skill>limit) continue;
            int new_players = dp_players[mask] + counts[i];
            if(new_skill < dp_skill[new_mask] ||
              (new_skill==dp_skill[new_mask] && new_players>dp_players[new_mask])){
                dp_skill[new_mask] = new_skill;
                dp_players[new_mask] = new_players;
            }
        }
    }

    int ans=0;
    for(int mask=0; mask<MAX_MASK; mask++){
        if(dp_skill[mask]<=limit)
            ans=max(ans, dp_players[mask]);
    }
    cout << ans << "\n";
    return 0;
}
"""

# -------------------------------------------------------------------------------------------------


"""

ABC Challenge

Problem Description
Three sisters - Anita, Binita, and Charita, possess a collection of items.
Each item is marked with the first letter of its owner: A (Anita), B (Binita), or C (Charita).
The items are arranged in line but not grouped by owner.
The Challenge
The goal is to rearrange the items so that all of Anita's items are together, all of Binita's are together, and all of Charita's are together.
You can pick an item and shift it to another position. When you shift an item, everything in between shifts to make space.
Some positions are "fixed" - i.e. the item at these spots must stay with the same owner even after rearranging. You have to do this grouping of items with minimum number of shiftings.
Constraints
The given string will contain only the characters [A, B, C]

1 <= number of items <= 500

1 <= number of fixed positions <= 10

Input
First line consists of a single integer denoting the total number of items.

The second line contains a string representing the arrangement of items (space separated), where each character A, B, or C, indicates the owner of the item: Anita, Binita, or Charita respectively.

The third line contains a list of fixed positions (1-based index).

Output
If it's possible to group all items by owner while keeping the fixed positions unchanged (the owner of the item at those positions must remain the same after rearranging), print the minimum number of shifts needed.
If it's not possible, print "Impossible".
Time Limit (secs)
1

Examples
Example 1

Input

8

A B C B A C C A

1 4 7

Output

3

Explanation

Given that at the indices {1, 4, 7} the ownership of the items before and after shifting must be same. One possible shifting is shown below, which results in minimum number of shifts.

Keep the A at index 1. Shift the A's at index 5 and 8 to the positions 2 and 3. Number of shifts made so far is 2 and the string becomes AAABCBCC.

Shift the B at index 6 to index 5, the string becomes AAABBCCC, where all the items with same ownership are grouped. Hence the number of shifts made is 2 + 1 = 3 which is minimum possible.

Example 2

Input

10

C A B B C C B A B C

1 4 10

Output

Impossible

Explanation

Given that the ownership of items at positions {1, 4, 10} must remain unchanged after the rearrangement, we can observe that no matter how the items are shifted, it's not possible to group each person's items together while satisfying this condition. Therefore, the output should be "Impossible".

"""

import sys

def read_all():
    data = sys.stdin.read().strip().split()
    if not data:
        return None
    it = iter(data)
    n = int(next(it))
    arr = [next(it) for _ in range(n)]
    # remaining tokens form fixed positions (may be exactly n_f or maybe line separated)
    fixed = []
    # If no tokens left -> empty fixed
    for tok in it:
        fixed.append(int(tok) - 1)
    return n, arr, fixed

def lcs_length(a, b):
    # space-optimized LCS (only 2 rows). a and b are lists of chars length up to 500
    n, m = len(a), len(b)
    if n == 0 or m == 0:
        return 0
    prev = [0] * (m + 1)
    cur  = [0] * (m + 1)
    for i in range(1, n + 1):
        ai = a[i-1]
        # compute cur row
        for j in range(1, m + 1):
            if ai == b[j-1]:
                cur[j] = prev[j-1] + 1
            else:
                # max of left(cur[j-1]) and top(prev[j])
                if cur[j-1] >= prev[j]:
                    cur[j] = cur[j-1]
                else:
                    cur[j] = prev[j]
        prev, cur = cur, prev  # reuse arrays (swap)
    return prev[m]

def solve():
    parsed = read_all()
    if parsed is None:
        return
    n, arr, fixed = parsed

    cntA = arr.count('A')
    cntB = arr.count('B')
    cntC = arr.count('C')

    orders = [
        ('A','B','C'),
        ('A','C','B'),
        ('B','A','C'),
        ('B','C','A'),
        ('C','A','B'),
        ('C','B','A')
    ]

    INF = 10**9
    best = INF

    for order in orders:
        # compute ranges for each letter in target
        seg = {}
        start = 0
        for ch in order:
            length = {'A': cntA, 'B': cntB, 'C': cntC}[ch]
            seg[ch] = (start, start + length - 1)  # inclusive
            start += length

        # validate fixed positions
        ok = True
        for f in fixed:
            if f < 0 or f >= n:
                # ignore invalid indexes if any, but typically shouldn't happen
                ok = False
                break
            expected_letter = None
            # find which segment index f falls into
            # because segments are contiguous and cover 0..n-1, just check arr[f] should equal expected
            # Instead: we need expected letter at index f in target:
            for ch in order:
                lo, hi = seg[ch]
                if lo <= f <= hi:
                    expected_letter = ch
                    break
            if expected_letter is None or arr[f] != expected_letter:
                ok = False
                break
        if not ok:
            continue

        # build target sequence (list of letters) deterministically
        target = []
        for ch in order:
            length = {'A': cntA, 'B': cntB, 'C': cntC}[ch]
            if length > 0:
                target.extend([ch] * length)

        # now compute LCS(arr, target)
        l = lcs_length(arr, target)
        moves = n - l
        if moves < best:
            best = moves

    if best == INF:
        print("Impossible")
    else:
        print(best)

if __name__ == "__main__":
    solve()

# -------------------------------------------------------------------------------------------------