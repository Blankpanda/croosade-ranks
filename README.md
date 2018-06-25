# croosade-ranks
scrape rankings to see where you stand on croosade maplestory private server in regards to other players of your class.

# Example (my Marksman)

```
py rankings-scrape.py squat
todays date: 2018-06-25 10:54:49.980221
total execution time: time taken in minutes: 2.4194298585255942
for job: Marksman
class rank=1:   total rank=76   name=dull       level=171
class rank=2:   total rank=151  name=Madara     level=163
class rank=3:   total rank=189  name=Lament     level=160
class rank=4:   total rank=197  name=NishadeMK  level=160
class rank=5:   total rank=230  name=funded     level=157
class rank=6:   total rank=257  name=Moskov     level=156
class rank=7:   total rank=279  name=Jerrbear   level=155
class rank=8:   total rank=315  name=Hufflepuff level=153
class rank=9:   total rank=326  name=Bazooka    level=153
class rank=10:  total rank=328  name=Blinkers   level=153
class rank=11:  total rank=348  name=SnipeAddict        level=152
class rank=12:  total rank=403  name=ActiveGo   level=150
class rank=13:  total rank=523  name=Sage       level=145
class rank=14:  total rank=542  name=Shoka      level=144
class rank=15:  total rank=603  name=Chipmunk   level=142
class rank=16:  total rank=640  name=Rovin      level=141
class rank=17:  total rank=655  name=Kamatte    level=141
class rank=18:  total rank=687  name=Ralph      level=140
class rank=19:  total rank=705  name=Risk       level=139
class rank=20:  total rank=717  name=Altier     level=139
class rank=21:  total rank=773  name=Arsenic    level=137
class rank=22:  total rank=908  name=Fieri      level=134
class rank=23:  total rank=947  name=Lovey      level=132
class rank=24:  total rank=966  name=StevenIsGa level=132
class rank=25:  total rank=986  name=Mevv       level=131
class rank=26:  total rank=1002 name=Fiend      level=131
class rank=27:  total rank=1090 name=Inferdesu  level=129
class rank=28:  total rank=1124 name=Sneze      level=128
class rank=29:  total rank=1134 name=Keiboo     level=128
class rank=30:  total rank=1184 name=Bamico     level=126
class rank=31:  total rank=1186 name=Dragonfruit        level=126
class rank=32:  total rank=1192 name=KarlMarx   level=126
class rank=33:  total rank=1197 name=Xuja       level=126
class rank=34:  total rank=1211 name=iceno24    level=126
class rank=35:  total rank=1254 name=Team       level=124
class rank=36:  total rank=1266 name=TreeCracker        level=124
class rank=37:  total rank=1280 name=squat      level=124
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
