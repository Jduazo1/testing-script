# take mock with slugs and gives file with team image link
#
#
# data_nba_team_image.txt  &  rndx_2_with_slug.txt -----> rndx_3_final.txt
# Run as: python mock_2_nba_image_link.py mock_data_round_1.txt
import sys
filein = open("rnd2_2_with_slug_updated.txt", "r")
filein_data = open("data_nba_team_image.txt","r")
fileout = open("rnd2_3_final.txt", "w")
data = filein_data.readlines()
data_mock = filein.readlines()

x = 1

team_name_list =[]
link_list =[]

for line in data:
    row1 = line.split("\t")
    #print(row1)
    team_name_list.append(row1[0])
    link = row1[1]
    link_list.append(link[0:len(link)-1])
#print(link_list)
team_dict = dict(zip(team_name_list,link_list))

for linex in data_mock:
    rowx = linex.split("\t")
    teamx = rowx[0]
    namex = rowx[1]
    schoolx = rowx[2]
    descx = rowx[3]
    slugx = rowx[4]
    if teamx in team_dict:
        linkx = team_dict[teamx]
        fileout.write(teamx + "\t" + namex + "\t" + schoolx+ "\t" + descx + "\t" + slugx[0:len(slugx)-1] + "\t" + linkx[0:len(linkx)-1] + "\n")
    else:
        #print(name1+ " missing slug")
        fileout.write(teamx + "\t" + namex + "\t" + schoolx + "\t" + descx + "\t" + slugx[0:len(slugx)-1] + "\t" + "missing link" + "\n")
    


#[0:len(linkx)-1]
# for line1 in data_players:
#     row1 = line1.split("\t")
#     team1 = row1[0]
#     name1 = row1[1]
#     school1 = row1[2]
#     desc1 = row1[3]
#     if name1 in slug_dict:
#         slug1 = slug_dict[name1]
#         #print(name1 +" " + slug1)
#         player_link = "https://nextones.com/player/"+slug1+"/statistics"
#         fileout.write(team1 + "\t" + name1 + "\t" + school1+ "\t" + desc1[0:len(desc1)-1] +  "\t" + player_link[0:len(player_link)-1] + "\n")
#     else:
#         print(name1+ " missing slug")
#         fileout.write(team1 + "\t" + name1 + "\t" + school1+ "\t" + desc1[0:len(desc1)-1] +  "\t" + "missing slug" + "\n")
    

# file_tho += "</table>"

fileout.close()
filein.close()
