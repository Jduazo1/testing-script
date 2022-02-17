import sys
# makes final html from rndx_3_final_updated.txt
# rndx_3_final_updated.txt -----> rndx_end_mock_draft.html
#
# Run as: python mock_draft_script.py mock_data_round_1.txt
#0      1       2           3       4       5
#team   name    school      desc    slug    img_link
filein = open("rnd1_3_final_updated.txt", "r")
fileout = open("rnd1_end_mock_draft.html", "w")
data = filein.readlines()

file_tho = "<table>\n"

x = 1


for line in data[0:]:
    row = line.split("\t")
    #[k.strip('\n') for k in row]
    file_tho += "<!-- "+ str(x) +"xxxxxxxxx-->\n"
    file_tho += "  <tr>\n"
    file_tho += "    <td>"+ str(x) +"</td>\n"
    file_tho += '    <td><img alt="'+row[0]+'" title="'+row[0]+'" src="' + row[5][0:len(row[5])-1] + '"></td>\n'
    file_tho += '    <td><a href="'+row[4]+'">'+row[1]+'</a></td>\n'
    file_tho += "    <td>"+row[2]+"</td>\n"
    file_tho += "    <td>"+row[3]+"</td>\n"
    file_tho += "  </tr>\n"
    x+=1

file_tho += "</table>"

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