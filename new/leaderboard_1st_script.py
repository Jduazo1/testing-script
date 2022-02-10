import sys



class_name = ""
filein_raw = open(class_name + "_1_raw.txt", "r") #raw data
fileout_final = open(class_name +"_2_final.txt","w") #final text list
filein_player_data = open("data_players_slug.txt", "r") #player slug list
filein_team_data = open("data_leaderboard_team_image_link.txt", "r") #team iamge liist
data_players = filein_player_data.readlines()
data_teams = filein_team_data.readlines()
data_raw = filein_raw.readlines()

#player slug in dictionary
names_list = []
slug_list = []
for line in data_players:
    row = line.split("\t")
    names_list.append(row[0] + " " + row[1])
    slug = row[2]
    slug_list.append(slug[0:len(slug)-1])
player_slug_dict = dict(zip(names_list,slug_list))


#team iamge in dictionary
school_name_list = []
link_image_list = []
for line in data_teams:
    row = line.split("\t")
    school_name_list.append(row[0])
    link = row[1]
    link_image_list.append(link[0:len(link)-1])  
school_image_dict = dict(zip(school_name_list,link_image_list))


for i in range(0,len(data_raw)-4,5):
    rank = data_raw[i]
    name = data_raw[i+1]
    name_new = name.rstrip()
    school = data_raw[i+2]
    school_new = school.rstrip()
    position = data_raw[i+3]
    overall = data_raw[i+4]
    if name_new in player_slug_dict and school_new in school_image_dict:
        player_slug = player_slug_dict[name_new]
        player_link = "https://nextones.com/player/"+player_slug+"/statistics"
        team_image = school_image_dict[school_new]
        fileout_final.write(rank.rstrip() + "\t" + name_new + "\t" + school_new + "\t" + position.rstrip() + "\t" + overall.rstrip()  +  "\t" + player_link + "\t"+ team_image + "\n")
    
    elif name_new in player_slug_dict and school_new not in school_image_dict:
        player_slug = player_slug_dict[name_new]
        player_link = "https://nextones.com/player/"+player_slug+"/statistics"
        fileout_final.write(rank.rstrip() + "\t" + name_new + "\t" + school_new + "\t" + position.rstrip() + "\t" + overall[0:len(overall)-1] + "\t" + player_link + "\t"+"MISSING TEAM IMAGE LINK" + "\n")
    
    elif name_new not in player_slug_dict and school_new in school_image_dict:
        team_image = school_image_dict[school_new]
        fileout_final.write(rank.rstrip() + "\t" + name_new + "\t" + school_new + "\t" + position.rstrip() + "\t" + overall[0:len(overall)-1] + "\t" + "MISSING PLAYER SLUG" + "\t"+ team_image + "\n")
    
    else:
        fileout_final.write(rank.rstrip() + "\t" + name_new + "\t" + school_new + "\t" + position.rstrip() + "\t" + overall.rstrip() + "\t" + "MISSING PLAYER SLUG" + "\t"+ "MISSING TEAM IMAGE LINK" + "\n")




filein_raw.close()
filein_player_data.close()
filein_team_data.close()
fileout_final.close()
