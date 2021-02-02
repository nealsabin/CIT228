#Hands on 3 #3
players = {
    'akaline':{
        'first':'Al',
        'last':'Kaline',
        'position':'Right Fielder',    
    },
    'jverlander':{
        'first':'Justin',
        'last':'Verlander',
        'position':'Pitcher',
    },
    'lwhitaker':{
        'first':'Lou',
        'last':'Whitaker',
        'position':'Second Base',
    },
}

for player, playerInfo in players.items():
    print(f"\nFirst Name: {playerInfo['first']}")
    last=playerInfo['last']
    position=playerInfo['position']

    print(f"\tLast Name: {last}")
    print(f"\tPosition: {position}")