import numpy as np

# CONSTANTS
NAME_INDEX = 0
P_INDEX = 1
GD_INDEX = 2
GF_INDEX = 3
GA_INDEX = 4

A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
H = 7

FIRST = 0
SECOND = 1

"""
setup groups with unfilled rankings
"""
def main():
    WC_DICT = make_WC_dictionary()
    print(f"The matchups will appear as 'Team1 VS Team2', write your predicted score in the format '0,3' to indicate a final score of Team1: 0, Team2: 3\n")
    # for all groups
    for i in WC_DICT:
        # get scores for each group game, create group rankings
        WC_DICT[i] = get_group_scores(WC_DICT[i], i)
        # when games are done, display the group
        print(f"Here is your completed table for {i}")
        for j in WC_DICT[i]['Teams']:
            print(f"{j}")
        print(f"The Group Rankings are:\n{WC_DICT[i]['Rankings']}")
    
    qual_teams = get_qualifiers(WC_DICT) 
    newWC = Tournament(qual_teams)
    newWC.make_bracket()
    newWC.disp()
    print('\n------UPDATED BRACKET------\n')
    newWC.play_bracket()
    newWC.disp()

### get the first 2 teams of each group for testing
# def main():
#     WC_DICT = make_WC_dictionary()
#     # print(f"The matchups will appear as 'Team1 VS Team2', write your predicted score in the format '0,3' to indicate a final score of Team1: 0, Team2: 3\n")
#     # for all groups
#     ko_teams = []
#     for it_group in WC_DICT:
#         newteams = [j[0] for j in WC_DICT[it_group]['Teams'][0:2]]
#         ko_teams.append(newteams)
#     print(ko_teams)


def make_WC_dictionary():
    new_DICT = {}
    new_DICT['Group A'] = {   'Teams':
                                    [ # [Country,        P,GF,GA,GD      
                                        ['Qatar',        0, 0, 0, 0],
                                        ['Ecuador',      0, 0, 0, 0],
                                        ['Senegal',      0, 0, 0, 0],
                                        ['Netherlands',  0, 0, 0, 0]
                                    ],
                                'Rankings': []
                            }
    new_DICT['Group B'] = {   'Teams':
                                    [
                                        ['England',         0,0,0,0],
                                        ['Iran',             0,0,0,0],
                                        ['United States',    0,0,0,0],
                                        ['Wales',            0,0,0,0]
                                    ],
                                'Rankings': []
                            }
    new_DICT['Group C'] = {   'Teams':
                                    [
                                        ['Argentina',    0, 0, 0, 0],
                                        ['Saudi Arabia', 0, 0, 0, 0],
                                        ['Mexico',       0, 0, 0, 0],
                                        ['Poland',       0, 0, 0, 0]
                                    ],
                                'Rankings': []
                            }
    new_DICT['Group D'] = {   'Teams':
                                    [
                                        ['France',    0, 0, 0, 0],
                                        ['Australia', 0, 0, 0, 0],
                                        ['Denmark',   0, 0, 0, 0],
                                        ['Tunisia',   0, 0, 0, 0]
                                    ],
                                'Rankings': []
                            }
    new_DICT['Group E'] = {   'Teams':
                                    [
                                        ['Spain'    , 0, 0, 0, 0],
                                        ['Costa Rica', 0, 0, 0, 0],
                                        ['Germany'  , 0, 0, 0, 0],
                                        ['Japan'    , 0, 0, 0, 0]
                                    ],
                                'Rankings': []
                            }
    new_DICT['Group F'] = {   'Teams':
                                    [
                                        ['Belgium', 0, 0, 0, 0],
                                        ['Canada', 0, 0, 0, 0],
                                        ['Morocco', 0, 0, 0, 0],
                                        ['Croatia', 0, 0, 0, 0]
                                    ],
                                'Rankings': []
                            }
    new_DICT['Group G'] = {   'Teams':
                                    [
                                        ['Brazil', 0, 0, 0, 0],
                                        ['Serbia', 0, 0, 0, 0],
                                        ['Switzerland', 0, 0, 0, 0],
                                        ['Cameroon', 0, 0, 0, 0]
                                    ],
                                'Rankings': []
                            }
    new_DICT['Group H'] = {   'Teams':
                                    [
                                        ['Portugal', 0, 0, 0, 0],
                                        ['Ghana', 0, 0, 0, 0],
                                        ['Uruguay', 0, 0, 0, 0],
                                        ['SouthKorea', 0, 0, 0, 0]
                                    ],
                                'Rankings': []
                            }
    return new_DICT

def get_group_scores(group, group_name):
    """
    input:
    {   'Teams':
            [ # [Country,        P,GF,GA,GD      
                ['Qatar',        0, 0, 0, 0],
                ['Ecuador',      0, 0, 0, 0],
                ['Senegal',      0, 0, 0, 0],
                ['Netherlands',  0, 0, 0, 0]
            ],
        'Rankings': []
    }, 'Group A'
    ouput:
    {   'Teams':
            [ # [Country,        P,GF,GA,GD      
                ['Qatar',        0, 0, 0, 0],
                ['Ecuador',      0, 0, 0, 0],
                ['Senegal',      0, 0, 0, 0],
                ['Netherlands',  0, 0, 0, 0]
            ],
        'Rankings': ['Senegal', 'Netherlands', 'Ecuador', 'Qatar']
    }

    ['Qatar', 'Ecuador', 'Senegal', 'Netherlands']
    game order:
    0 vs 1
    2 vs 3
    0 vs 2
    3 vs 1
    3 vs 0
    1 vs 2
    """
    order_of_play = [(0,1),(2,3),(0,2),(3,1),(3,0),(1,2)]
    list_of_teams = []
    for i in group['Teams']:
        list_of_teams.append(i[0])
    print(f"This is {group_name} with {', '.join(list_of_teams)}")
    for opponents in order_of_play:
        score = [0,0]
        team1 = opponents[0]
        team2 = opponents[1]
        score = play(team1, team2, list_of_teams)
        print(f"{list_of_teams[team1]} {score} {list_of_teams[team2]}")
        # set stats for team1
        group['Teams'][team1][GF_INDEX] += score[0]
        group['Teams'][team1][GA_INDEX] +=  score[1]
        group['Teams'][team1][GD_INDEX] = group['Teams'][team1][GF_INDEX] - group['Teams'][team1][GA_INDEX]
        # set stats for team2
        group['Teams'][team2][GF_INDEX] += score[1]
        group['Teams'][team2][GA_INDEX] += score[0]
        group['Teams'][team2][GD_INDEX] = group['Teams'][team2][GF_INDEX] - group['Teams'][team2][GA_INDEX]
        # add points
        if score[0] > score[1]:
            group['Teams'][team1][P_INDEX] += 3
        elif score[0] < score[1]:
            group['Teams'][team2][P_INDEX] += 3
        else: # tie
            group['Teams'][team1][P_INDEX] += 1
            group['Teams'][team2][P_INDEX] += 1
        
        # print(group['Teams'][team1])
        # print(group['Teams'][team2])
    # all games played for this group
    # rank teams
    group['Rankings'] = group_rank(group)

    return group

def play(team1, team2, group_list):
    if group_list != None:
        str_core = input(f"{group_list[team1]} VS {group_list[team2]}\n")
    else:
        str_core = input(f"{team1} VS {team2}\n")
    score = splitter(str_core)
    return score # [3,2]

def splitter(inStr):
    if ', ' in inStr:
        inStr = inStr.split(', ')
    elif ',' in inStr:
        inStr = inStr.split(',')
    elif ' ' in inStr:
        inStr = inStr.split(' ')
    else:
        exit()
    ouputScore = [eval(i) for i in inStr]
    print(ouputScore)
    return ouputScore

def group_rank(group):
    """
    input:
    {   'Teams':
            [ # [Country,        P,GF,GA,GD      
                ['Qatar',        0, 0, 0, 0],
                ['Ecuador',      0, 0, 0, 0],
                ['Senegal',      0, 0, 0, 0],
                ['Netherlands',  0, 0, 0, 0]
            ],
        'Rankings': []
    }
    ouput: ['Senegal', 'Netherlands', 'Ecuador', 'Qatar']
    """
    group_in_list = group['Teams']

    rankings = sorted(group_in_list, key=lambda x: x[1:4], reverse=True)
    group['Rankings'] = [i[0] for i in rankings]

    return group['Rankings']

def break_the_tie(team1, team2):
    winner = input(f"The game is tied between {team1} and {team2}. Who wins in penalties?\n")
    while (winner != team1) and (winner != team2):
        winner = input(f"Please input the winner as either {team1} or {team2}\n")
    return winner # [3,2]


class Tournament:
    def __init__(self, teams):
        self.bracket = {
                                                    'Final': {
                                                        'Teams': [],
                                                        'Score': [],
                                                        'Winner': ''
                                                    },
                                                    'ThirdPlaceGame': {
                                                        'Teams': [],
                                                        'Score': [],
                                                        'Winner': ''
                                                    },
            'LeftSemiFinal': {
                'Teams': [],
                'Score': [],
                'Winner': '',
                'NextGame': ['Final', 'ThirdPlaceGame']
            },
            'LeftTopQuarterFinal': {
                'Teams': [],
                'Score': [],
                'Winner': '',
                'NextGame': 'LeftSemiFinal'
            },
            'LeftBottomQuarterFinal': {
                'Teams': [],
                'Score': [],
                'Winner': '',
                'NextGame': 'LeftSemiFinal'
            },
            'L1R16': {
                'Teams': [],
                'Score': [],
                'Winner': '',
                'NextGame': 'LeftTopQuarterFinal'
            },
            'L2R16': {
                'Teams': [],
                'Score': [],
                'Winner': '',
                'NextGame': 'LeftTopQuarterFinal'
            },
            'L3R16': {
                'Teams': [],
                'Score': [],
                'Winner': '',
                'NextGame': 'LeftBottomQuarterFinal'
            },
            'L4R16': {
                'Teams': [],
                'Score': [],
                'Winner': '',
                'NextGame': 'LeftBottomQuarterFinal'
            },
                                                                        'RightSemiFinal': {
                                                                            'Teams': [],
                                                                            'Score': [],
                                                                            'Winner': '',
                                                                            'NextGame': ['Final', 'ThirdPlaceGame']
                                                                        },
                                                                        'RightTopQuarterFinal': {
                                                                            'Teams': [],
                                                                            'Score': [],
                                                                            'Winner': '',
                                                                            'NextGame': 'RightSemiFinal'
                                                                        },
                                                                        'RightBottomQuarterFinal': {
                                                                            'Teams': [],
                                                                            'Score': [],
                                                                            'Winner': '',
                                                                            'NextGame': 'RightSemiFinal'
                                                                        },
                                                                        'R1R16': {
                                                                            'Teams': [],
                                                                            'Score': [],
                                                                            'Winner': '',
                                                                            'NextGame': 'RightTopQuarterFinal'
                                                                        },
                                                                        'R2R16': {
                                                                            'Teams': [],
                                                                            'Score': [],
                                                                            'Winner': '',
                                                                            'NextGame': 'RightTopQuarterFinal'
                                                                        },
                                                                        'R3R16': {
                                                                            'Teams': [],
                                                                            'Score': [],
                                                                            'Winner': '',
                                                                            'NextGame': 'RightBottomQuarterFinal'
                                                                        },
                                                                        'R4R16': {
                                                                            'Teams': [],
                                                                            'Score': [],
                                                                            'Winner': '',
                                                                            'NextGame': 'RightBottomQuarterFinal'
                                                                        }

            }
        self.teams = teams
        self.group_assign = [[A,B],[B,A],[C,D],[D,C],[E,F],[F,E],[G,H],[H,G]]
        self.first_rounds = ['L1R16', 'R1R16', 'L2R16', 'R2R16', 'L3R16', 'R3R16', 'L4R16', 'R4R16']

    def make_bracket(self):
        # starting at quarterfinals, make bracket
        for i in range(len(self.first_rounds)):
            cur_round = self.first_rounds[i]
            cur_matchups = self.group_assign[i]

            team1 = self.teams[cur_matchups[0]][FIRST]
            print(f"{chr(cur_matchups[0]+65)}{FIRST+1}: {team1}")

            team2 = self.teams[cur_matchups[1]][SECOND]
            print(f"{chr(cur_matchups[1]+65)}{SECOND+1}: {team2}")

            self.bracket[self.first_rounds[i]]['Teams'] = [team1, team2]
    
    def play_bracket(self):
        for game in self.first_rounds:
            team1 = self.bracket[game]['Teams'][0]
            team2 = self.bracket[game]['Teams'][1]
            score = play(team1, team2, None)
            self.bracket[game]['Score'] = score
            if score[0] > score[1]:
                # team1 wins
                self.bracket[game]['Winner'] = team1
            elif score[0] < score[1]:
                # team1 wins
                self.bracket[game]['Winner'] = team2
            else: # score[0] == score[1]:
                # team1 wins
                print('BREAK THE TIE!')
                self.bracket[game]['Winner'] = break_the_tie(team1, team2)
            winner = self.bracket[game]['Winner']
            next_game = self.bracket[game]['NextGame']
            self.bracket[next_game]['Teams'].append(winner)
            ### QUARTERS FILLED BUT NOT PLAYED
            
    
    
    
    def get_winner(self):
        return self.bracket['Final']['Winner']
    def get_runner_up(self):
        for i in self.bracket['Final']['Teams']:
            if self.bracket['Final']['Winner'] != i:
                runner_up = i
                return runner_up
        return -1
    def get_third_place(self):
        return self.bracket['ThirdPlaceGame']['Winner']
    def disp(self):
        for i in self.bracket:
            print(f"{i}: {self.bracket[i]}")

def get_qualifiers(all_groups):
    qualifiers = []
    for i in all_groups:
        cur_qualifiers = all_groups[i]['Rankings'][0:2]
        qualifiers.append(cur_qualifiers)
    return qualifiers



if __name__ == "__main__":
    main()
