#dictionaries
team_players={"name": "Virat", "age": 37, "formats": "ODI", "playing_style": "right hand batsman"}
print(team_players.get("name"))
print(team_players.keys())
print(team_players.values())
print(team_players.items())
print(team_players.pop("playing_style"))
print(team_players.popitem())
print(team_players.update({"jersey":18}))
print(team_players)
def subtract_age(k,v):
    for k,v in team_players:
        if v==int:
            print(v-1)