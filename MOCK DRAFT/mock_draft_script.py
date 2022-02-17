import sys
# makes final html from rndx_3_final_updated.txt
# rndx_3_final_updated.txt -----> rndx_end_mock_draft.html
#
# Run as: python mock_draft_script.py mock_data_round_1.txt
# 0                  1           2               3               4               5
# TEAM_IMAGE_LINK	TEAM_NAME	PLAYER_NAME	    PLAYER_TEAM	    PLAYER_DESC	    PLAYER_PROFILE_LINK
name = "feb17"
filein = open(name + "_mock_raw.txt", "r")
fileout = open(name + "_mock_draft_end.html", "w")
data = filein.readlines()
file_tho = "<!DOCTYPE html>\n"
file_tho += "<html>\n"
file_tho += "<head>\n"
file_tho += "<style>\n"
file_tho += "table{\n"
file_tho += "    width:100%;\n"
file_tho += "    border-collapse: collapse;\n"
file_tho += "    margin: 25px 0;\n"
file_tho += "    font-size: 0.9em;\n"
file_tho += "    font-family: Bebas,sans-serif;\n"
file_tho += "}\n"
file_tho += "th{\n"
file_tho += "    border-top: 2px solid black;\n"
file_tho += "    border-bottom: 2px solid black;\n"
file_tho += "    background-color: #45f1fb;\n"
file_tho += "    text-align: center;\n"
file_tho += "    font-weight: 900;\n"
file_tho += "    font-size: 1.0em;\n"
file_tho += "    font-family: Bebas,sans-serif;   \n"
file_tho += "}\n"
file_tho += "td{\n"
file_tho += "    padding: .5% 2.5%;\n"
file_tho += "}\n"
file_tho += "tr{\n"
file_tho += "    border-left: 2px solid #000000;\n"
file_tho += "    border-right: 2px solid #000000;\n"
file_tho += "}\n"
file_tho += "img{\n"
file_tho += "   width:100%;\n"
file_tho += "}\n"
file_tho += "tr:nth-of-type(odd) {\n"
file_tho += "  background-color: #b8fafd;\n"
file_tho += "}\n"
file_tho += "tr:last-child{\n"
file_tho += "  border-bottom: 2px solid #000000;\n"
file_tho += "}\n"
file_tho += "tr:hover{\n"
file_tho += "  background-color: #D4D0E6;\n"
file_tho += "}\n"
file_tho += "td:nth-child(1) {  \n"
file_tho += "  font-weight: 1000;\n"
file_tho += "  font-size: 1.5em;\n"
file_tho += "}\n"
file_tho += "td:nth-child(2) {  \n"
file_tho += "  width:20%;\n"
file_tho += "}\n"
file_tho += "td:nth-child(5) {  \n"
file_tho += "  font-family: Barlow,sans-serif;\n"
file_tho += "  font-weight: 500;\n"
file_tho += "  font-style: italic;\n"
file_tho += "  color: #52504e;\n"
file_tho += "}\n"
file_tho += "h2{\n"
file_tho += "  font-weight: 800;\n"
file_tho += "  font-size: 2em;\n"
file_tho += "  width:100%;\n"
file_tho += "  text-align: center;\n"
file_tho += "  font-family: Bebas,sans-serif;\n"
file_tho += "}\n"
file_tho += "h3{\n"
file_tho += "  font-weight: 800;\n"
file_tho += "  font-size: 1em;\n"
file_tho += "  width:100%;\n"
file_tho += "  text-align: left;\n"
file_tho += "  font-family: Bebas,sans-serif;\n"
file_tho += "}\n"
file_tho += "</style>\n"
file_tho += "</head>\n"
file_tho += "<body>\n"
file_tho += "<h2>2022 MOCK DRAFT</h2>\n"
file_tho += "<h3>ROUND 1</h3>\n"
file_tho += "<table>\n"
file_tho += "  <tr>\n"
file_tho += "    <th> </th>\n"
file_tho += "    <th>TEAM</th>\n"
file_tho += "    <th>PLAYER</th>\n"
file_tho += "    <th>ORIGINAL TEAM</th>\n"
file_tho += "    <th>PLAYER DESCRIPTION</th>\n"
file_tho += "  </tr>\n"


x = 1


for line in data[0:]:
    row = line.split("\t")
    #[k.strip('\n') for k in row]
    file_tho += "<!-- "+ str(x) +"xxxxxxxxx-->\n"
    file_tho += "  <tr>\n"
    file_tho += "    <td>"+ str(x) +"</td>\n"
    file_tho += '    <td><img alt="'+row[1]+'" title="'+row[1]+'" src="' + row[0].rstrip() + '"></td>\n'
    file_tho += '    <td><a href="'+row[5]+'">'+row[2]+'</a></td>\n'
    file_tho += "    <td>"+row[3]+"</td>\n"
    file_tho += "    <td>"+row[4]+"</td>\n"
    file_tho += "  </tr>\n"
    x +=1
    if x == 31:
        file_tho += "</table>\n"
        file_tho += "<h3>ROUND 2</h3>\n"
        file_tho += "<table>\n"
        file_tho += "   <tr>\n"
        file_tho += "       <th> </th>\n"
        file_tho += "       <th>TEAM</th>\n"
        file_tho += "       <th>PLAYER</th>\n"
        file_tho += "       <th>ORIGINAL TEAM</th>\n"
        file_tho += "       <th>PLAYER DESCRIPTION</th>\n"
        file_tho += "   </tr>\n"

file_tho +="</table>\n"
file_tho += "</body>\n"
file_tho += "</html>\n"

fileout.writelines(file_tho)
fileout.close()
filein.close()


# <tr>
#   <td>NUMBER</td>
#   <td><img src="PHOTO LINK"></td>
#   <td><a href="PLAYER LINK">PLAYER NAME</a></td>
#   <td>ORIGINAL TEAM</td>
#   <td>DESCRIPTION</td>
# </tr>

#0          1               2               3               4                   5
#NUMBER     PHOTO LINK      PLAYER LINK     PLAYER NAME     ORIGINAL_TEAM       DESCRIPTION
# SELECT CustomerID,ContactName,Country FROM [Customers]
# WHERE Country='Mexico' AND City='México D.F.'
# ORDER BY CustomerID ASC;