#Final Project
# Include the required header comment lines at the top of your code (as before). If doing this as a PAIR project, include both member names that participated in the project. If a member does not participate, only write your name. 

#import modules

import csv


#Team Data – parallel lists
TEAM_CODES = ['ATF',  'AZC',  'BFB',  'BLR',  'CAP',  'CHB',  'CLB',  'CNB',  'DLC',  'DTL',
              'DVB',  'GBP',  'HST',  'INC',  'JKJ',  'KCC',  'LAC',  'LAR',  'LVR',  'MMD',
              'MNV',  'NEP',  'NOS',  'NYG',  'NYJ',  'PHE',  'PTS',  'SFN',  'STS',  'TBB',  'TNT',  'WSC']

TEAM_NAMES = ['Atlanta Falcons', 'Arizona Cardinals', 'Buffalo Bills', 'Baltimore Ravens', 'Carolina Panthers',
              'Chicago Bears', 'Cleveland Browns', 'Cincinnati Bengals', 'Dallas Cowboys', 'Detroit Lions',
              'Denver Broncos', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars',
              'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Las Vegas Raiders', 'Miami Dolphins',
              'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets',
              'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers',
              'Tennessee Titans', 'Washington Commanders']

#Positions Data – parallel lists
POS_CODES = ['C', 'CB', 'DE', 'DT', 'FB', 'G', 'K', 'LB', 'LS', 'OT', 'P', 'QB', 'RB', 'S', 'TE', 'WR']

POS_NAMES = ['Center', 'Cornerback', 'Defensive end', 'Defensive tackle', 'Fullback', 'Guard', 'Kicker', 'Linebacker',
             'Long snapper', 'Offensive tackle', 'Punter', 'Quarterback', 'Running back', 'Safety', 'Tight end', 'Wide receiver']


def main():

    CSVFILE = "NFL-players.csv"

    #display banner 
    banner = '*' * 50
    application_title = 'Victorino Reporting System'
    print(f"{banner}\n{application_title.center(50)}\n{banner}")

    #open file for reading
    with open(CSVFILE,'r', newline='') as infile:

        #create reader object
        reader = csv.reader(infile)

        #Read Row
        fields = next(reader)


    #Loop thru reader
    for row in reader:
        print(row)

        #Extract Values
        emp_id = row[0]
        last_name = row[1]
        first_name = row[2]
        team_code = row[3]
        position_code = row[4]
        player_num = row[5]
        player_age = int(row[6])
        player_weight = int(row[7])
        player_height = int(row[8])
        player_exp = int(row[9])
        player_college = row[10]

    #Display Row
        print('player name: ', first_name[2][3])
        
              
              


    #Display Banner
    #continue_selection = True
    #menu_selection = ''

    #Menu Loop
    #while menu_selection !='X':

    #Team Roster Report 
    print('1 - Team Roster Report')
    print('2 - Filtered Players Report')
    print('X - Exit')

    #user input
    user_input = input('Enter your selection: ')

    if user_input == '1':
        team_code = input('Enter a team code please: ') #get team code #also validateeeeeeeeeeeeeeeeeeeeeeeeeeeee


    elif user_input == '2':
        display_filtered_players()
    elif user_input == 'X':
        print(' Exiting the application.')
        
    else:
        print('Please Enter one of the given values')

        continue_selection = False
        

            
            
                    
        
        
        

        
    



def display_roster_report():

    #Get user input
    team_code=input('Enter team code selection: ').lower()

    #Validate Code
    is_valid = False
    while not is_valid:
        team_code=input('Enter team code selction:').upper
        
    if team_code =='':
        print('>>>Please Enter a team code:')
    elif team_code not in TEAM_CODES:
        print('>>>>Please Enter a valid team code')
    else:
        is_valid = True


    
    
        
        

    print('Team Roster Report by Player Number')
    
main()    
    
        
    

    



