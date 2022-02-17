# MOCK DRAFT
## SETUP
Setup excel sheet in this form of desired mock draft order
```
TEAM_IMAGE_LINK	  TEAM_NAME	  PLAYER_NAME	  PLAYER_TEAM	  PLAYER_DESC	  PLAYER_PROFILE_LINK
```
Files needed in folder:
- **mock_3_draft_script.py**											
  - *first script to go from raw data to final mock draft*

Files you must add in the folder:
- **xxxxx_mock_raw.txt**                               
  - *xxxxx = date of today*
  - *the .txt file will be blank*
EX
```
feb17_mock_raw.txt
```

1) in the xxxxx_mock_raw.txt copy and paste the sheet data into the text file.
2) on line 8 put the date that you named the original file in *name = ""*
EX
```
name = ""    -----> name = "feb17"
```
3) save the file
4) Run in the terminal of the folder:
```shell
python mock_draft_script.py
```



