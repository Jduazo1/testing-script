# INSTRUCTIONS TO CREATE LEADERBOARD HTML FILE
Files needed in folder:
- **leaderboard_1st_script.py**											
  - *first script to go from raw data to final data*
- **leaderboard_2nd_final_script.py**
  - *second script to go from final data to the final html leaderboard*
- **data_leaderboard_team_image_link.txt**        
  - *data of team and their team image link*
- **data_players_slug.txt**                     
  - *data of player and their profile link to NextOnes*

Files you must add in the folder:
- **xxxxx_1_raw.txt**                               
  - *xxxxx = whatever class the leaderboard will be*
  - *the .txt file will be blank*


## SETUP
Copy and paste the data from the NextOnes leaderboard site, all 150 players **make sure to highlight from the top to bottom**
- EX:
![highlight_example](/images/highlight_example.png)

Paste all text into file named **xxxxx_1_raw.txt**
- xxxxx = whatever class the leaderboard will be
- EX:
  - "juniors_1_raw.txt"

This is how file should look:
```
RANK
PLAYER_NAME
TEAM
POSITION
OVERALL
...
```

- EX:
```
1
Fardaws Aimaq
Utah Valley Wolverines
Center
99
2
Kofi Cockburn
Illinois Fighting Illini
Center
98
...
```

Make sure all needed files are in the folder.

## leaderboard_1st_script.py
On line 5 set the variable class_name to first word of **xxxxx_1_raw.txt**
- EX.
  - juniors_1_raw.txt
```
class_name = ""     ------->    class_name = "juniors"
```
Save the file

Run in the terminal of the folder:
```shell
python leaderboard_1st_script.py
```
### Check for errors
Once the script has been ran, there should be a file in your folder named **xxxxx_2_final.txt**

The file should have the following format, each of these elements in one line:
```
RANK    PLAYER_NAME     TEAM    POSITION    OVERALL     NEXTONES_PLAYER_PROFILE_LINK    TEAM_IMAGE_LINK
```
EX.
```
1	Fardaws Aimaq	Utah Valley Wolverines	Center	99	https://nextones.com/player/fardaws-aimaq/statistics	https://firebasestorage.googleapis.com/v0/b/samico-nextones.appspot.com/o/college-logos%2Futah-valley-wolverines.png?alt=media
2	Kofi Cockburn	Illinois Fighting Illini	Center	98	https://nextones.com/player/kofi-cockburn/statistics	https://firebasestorage.googleapis.com/v0/b/samico-nextones.appspot.com/o/college-logos%2Fillinois-fighting-illini.png?alt=media
```
Check the file for potential errors.
### POTENTIAL ERROR #1:
Make sure desired amount of players are present. The leaderboard should go all the way to 150.
If not all 150 players are present, that means one player is missing their team.
In the NextOnes leaderboard site some players are missing their team
- EX.
![missing_team_example](/images/missing_team_example.png)

- Locate the number of the last missing player on the **xxxxx_1_raw.txt** and click on the player profile with the missing team.
- Copy and paste the team name from the profile after the player name.
- EX.
```
61                                  61
Jovan Blacksher Jr.     ----->      Jovan Blacksher Jr.
Guard                               Grand Canyon Antelopes
87                                  Guard
                                    87
```

Once completed, save the **xxxxx_1_raw.txt**
- Run in the terminal of the folder again:
```shell
python leaderboard_1st_script.py
```                             
Check the file again and if all the players are there and it goes to the desired amount move on and check for the next error.

### POTENTIAL ERROR #2:
Missing player slug
- If the NEXTONES_PLAYER_PROFILE_LINK for a player says "MISSING PLAYER SLUG" that means that player is not in the data_players_slug.txt.
- EX.
**xxxxx_2_final.txt:**
```
61	Jovan Blacksher Jr.	Grand Canyon Antelopes	Guard	87	MISSING PLAYER SLUG	https://firebasestorage.googleapis.com/v0/b/samico-nextones.appspot.com/o/college-logos%2Fgrand-canyon-antelopes.png?alt=media
```

Go onto the NextOnes website and find the player profile for the missing player.
- In the **data_players_slug.txt** file:
  - start a new line at the bottom of the file and type out the players first and last name exactly how it is on the **xxxxx_2_final.txt**
  - **make sure to separate the first and last name with a TAB**
    - after the last name hit tab again and paste the slug, the slug of a player is everything that is between **"https://nextones.com/"** AND **"/statistics"**

- EX:
```
Jovan	Blacksher Jr.	jovan-blacksher-jr-
```

Once completed save the **data_players_slug.txt** and **xxxxx_2_final.txt**
Run in the terminal of the folder again:
```shell
python leaderboard_1st_script.py
```

### POTENTIAL ERROR #3:
Missing  team image link
- If the TEAM_IMAGE_LINK for a player says "MISSING TEAM IMAGE LINK" that means that team image is not in the **data_leaderboard_team_image_link.txt**
- EX.
**xxxxx_2_final.txt:**
```
4	E.J. Liddell	Ohio State Buckeyes	Forward	96	https://nextones.com/player/e-j-liddell-c82/statistics	MISSING TEAM IMAGE LINK
```
- Go onto the NextOnes website and find the player profile and copy the team
- Search up the image on google and save the image
- save the image name as the team name exactly how it is in the row and make all the letters lowercase and replace all spaces with hyphens "-"
- save the image into the firebase storage
- In the **data_leaderboard_team_image_link.txt** file:
  - start a new line at the bottom of the file and type out the team name exactly how it is on the xxxxx_2_final.txt 
  -  after the team name hit **TAB** and paste the firebase image link into the line

- EX:
```
Ohio State Buckeyes	https://firebasestorage.googleapis.com/v0/b/samico-nextones.appspot.com/o/college-logos%2Fohio-state-buckeyes.png?alt=media
```
Once completed save the **data_leaderboard_team_image_link.txt** and **xxxxx_2_final.txt**
Run in the terminal of the folder again:
```shell
python leaderboard_1st_script.py
```

If no more errors move onto the next script
## leaderboard_2nd_final_script.py
On line 4 set the variable *class_name* to first word of xxxxx_1_raw.txt
- EX. juniors_1_raw.txt
```
class_name = ""     ------->    class_name = "juniors"
```
Save the file

Run in the terminal of the folder:
```shell
python leaderboard_2nd_final_script.py
```
Once the script has been ran, there should be a file in your folder named **xxxxx_end_leaderboard_html.html**

this is the final leaderboard ready to be put on the site




