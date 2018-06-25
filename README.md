# croosade-ranks
scrape rankings to see where you stand on croosade maplestory private server in regards to other players of your class.

# Example (my Marksman)

```
  py rankings-scrape.py squat
  for job:Marksman
    1: name=dull,level=171
    2: name=Madara,level=162
    3: name=NishadeMK,level=160
    4: name=Lament,level=159
    5: name=Moskov,level=156
    6: name=Jerrbear,level=155
    7: name=funded,level=155
    8: name=Hufflepuff,level=153
    9: name=SnipeAddict,level=151
    10: name=Blinkers,level=150
    11: name=ActiveGo,level=149
    12: name=Bazooka,level=148
    13: name=Sage,level=145
    14: name=Shoka,level=143
    15: name=Chipmunk,level=142
    16: name=Ralph,level=140
    17: name=Risk,level=139
    18: name=Arsenic,level=137
    19: name=Rovin,level=136-
    20: name=Kamatte,level=135
    21: name=Fieri,level=132
    22: name=StevenIsGa,level=132
    23: name=Mevv,level=131
    24: name=Altier,level=129
    25: name=Inferdesu,level=129
    26: name=Bamico,level=126
    27: name=KarlMarx,level=126
    28: name=Team,level=124
    29: name=Sneze,level=123
    30: name=squat,level=122
    31: name=Dragonfruit,level=122
```

# Notes
 - The script might take some time to run if your not on the higher end of the rankings.
 - If other players of your job are found on the same ranking page, they will be appropriately displayed below you.
 - If your character is below 4th job, lets say, a priest, then the application will pull anyone still listed as a priest above your characer. Turns out there are some players in 15x that are listed as priests. Pulling up my priest I noticed:
 ```
 for job: Priest
  class rank=1:   total rank=843  name=Shrek      level=135
  class rank=2:   total rank=906  name=Cream      level=134
  class rank=3:   total rank=935  name=PorkChamp  level=133
  ...
 ```
 I don't know if this is intentional or if these guys are just HS mules.
 
 
 # TODO
  - Associate job titles with their respective jobs I.E magician/cleric/priest/bishop so entering a priest character will pull up bishops from 120+.
  - web version using flask (?)
