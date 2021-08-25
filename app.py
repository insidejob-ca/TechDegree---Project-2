import constants
import copy
from copy import deepcopy

team_name = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

def display_menu(): 
    print("-----------------------------------\n   BASKETBALL TEAM STATS TOOL   \n-----------------------------------")
    print("\n########### MENU ###########\n")
#    print("Here are your options:\n1) Display Team Stats\n2) Quit")

def team_stats(team_name, players): # function to display clean data for the stats
    print("\n-------------------- \nTeam {} Stats:\n--------------------\n\nTotal players : {}".format(team_name, len(players)))
    team_players = []
    players_guardians = []
    players_exp = []
    players_height = []
    
    for i in players:
        team_player_name = i['name']  ## Player's name 
        team_players.append(team_player_name)
        players_names_list=', '.join(team_players) 
        i['guardians'] = i['guardians'].split('and') ## Player's guardians name)
        player_guardians = i['guardians']
        players_guardians.extend(player_guardians)
        guardians_list=', '.join(players_guardians)

            
        player_exp_value = i['experience']   ## Player's experience value
        if str(player_exp_value).lower() == 'yes':
            i['experience'] = True
        else:
            i['experience'] = False
        players_exp.append(i['experience'])
        
        player_height = i['height']
        player_height_inc = i['height'].split(' ') ## Player's height 
        player_height_value = int(player_height_inc[0])
        i['height'] = player_height_value
        players_height.append(player_height_value)
        avg_height = round(sum(players_height) / len(players_height), 1) ## Player's average height calculation
#        print(constants.PLAYERS)
#        print(players)    
    display_stats(players_exp, avg_height, players_names_list, guardians_list)
    
    

def display_stats(players_exp, avg_height, players_names_list, guardians_list): #function to print the stats for user input
    print("Total experienced:  {}\nTotal inexperienced:  {}\n".format(players_exp.count(True), players_exp.count(False)))
    print("Average height:  ", avg_height, "inches\n")
    print("Players on Team:\n", players_names_list)
    print("Guardians:\n", guardians_list)
    
    
def continue_playing(): #controlling if user wish to continue playing
    continuing = input("\nEnter c to continue or q to quit. ")
    print("\n")

    while continuing.lower() != 'c' and continuing.lower() != 'q':
        print("Invalid input.")
        continuing = input("Enter c to continue or q to quit. ")
        print("\n")

    return continuing.lower()


def start_game(): #function will start the tool 
    play_game = True
    while play_game:
        print("===== Here are your options: =====\n1) Display Team Stats\n2) Quit")
        
        try:
            user_input = int(input("Enter an option > "))
            if user_input > 2:
                print("Please Enter the valid option from the menu list.")
        except ValueError:
                print("Oh no, we ran into an issue, Please try again with integers only from choice list options.")
        else:
            
            if user_input == 1:
                
                game_running = True
                while game_running:
                    print('\n===== Teams_List: =====\n1) Panthers\n2) Bandits\n3) Warriors\n')
                    try:
                        user_team_input = int(input("\nEnter an option to see the players on the team  >  "))
                            
                        if user_team_input not in range(1,4):
                            print("Please Enter the valid option from the team's list options.")
                            continue
                    except ValueError as err:
                            print("Oh no, we ran into an issue. Invalid option, Integers are accepted only!")
                    else:
                        if user_team_input == 1:
                            player_list_team = constants.PLAYERS[:3] + constants.PLAYERS[9:12]
                            team_stats(constants.TEAMS[0], player_list_team)    
                            if continue_playing() == 'c':
                                print("Thanks for continuing exploring the tool!")
#                               display_menu()
                                continue
                            else:
                                print("Thanks for checking the BASKETBALL TEAM STATS TOO, Bye!!!")
                                game_running = False
                                play_game = False
                        elif user_team_input == 2:
                            player_list_team2 = constants.PLAYERS[3:9]
                            team_stats(constants.TEAMS[1], player_list_team2)
                            if continue_playing() == 'c':
                                print("Thanks for continuing exploring the tool!")
                                continue
#                                display_menu()
                            else:
                                print("Thanks for checking the BASKETBALL TEAM STATS TOO, Bye!!!")
                                game_running = False
                                play_game = False       
                                
                        elif user_team_input == 3:
                            player_list_team3 = constants.PLAYERS[12:]
                            team_stats(constants.TEAMS[2], player_list_team3)
                            if continue_playing() == 'c':                             
                                print("Thanks for continuing exploring the tool!")
#                                display_menu()
                                continue
                                
                            else:
                                print("Thanks for checking the BASKETBALL TEAM STATS TOOL, Bye!!!")
                                game_running = False
                                play_game = False                                
            elif user_input == 2:
                print("Bye, thanks for checking the tool!!!")
                play_game = False            
    
    
    
if __name__ == "__main__":
#    team_stats()
#    print("-----------------------------------\n   BASKETBALL TEAM STATS TOOL   \n-----------------------------------")
#    print("---- MENU ----")
    
    display_menu()
    start_game()
