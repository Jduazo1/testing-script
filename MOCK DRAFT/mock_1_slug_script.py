# adds slug to each player
# takes in mock order without slug   needs data player slugs
# data_players_script.txt  &  rnd1_x_without_slug.txt -----> rnd1_x_with_slug.txt
import sys

filein = open("data_players_slug.txt", "r")
filein_players = open("rnd2_1_without_slug.txt", "r")
fileout = open("rnd2_2_with_slug.txt", "w")
data = filein.readlines()
data_players = filein_players.readlines()
names_list = []
slug_list = []


for line in data:
    row = line.split("\t")
    names_list.append(row[0] + " " + row[1])
    slug = row[2]
    slug_list.append(slug[0:len(slug)-1])
    #print(line[0:len(line)-1])
    #print(n)

slug_dict = dict(zip(names_list,slug_list))

for line1 in data_players:
    row1 = line1.split("\t")
    team1 = row1[0]
    name1 = row1[1]
    school1 = row1[2]
    desc1 = row1[3]
    if name1 in slug_dict:
        slug1 = slug_dict[name1]
        #print(name1 +" " + slug1)
        player_link = "https://nextones.com/player/"+slug1+"/statistics"
        fileout.write(team1 + "\t" + name1 + "\t" + school1+ "\t" + desc1[0:len(desc1)-1] +  "\t" + player_link + "\n")
    else:
        fileout.write(team1 + "\t" + name1 + "\t" + school1+ "\t" + desc1[0:len(desc1)-1] +  "\t" + "MISSING SLUG" + "\n")
    

fileout.close()
filein.close()
filein_players.close()