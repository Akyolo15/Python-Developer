import random
import numpy
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/users/<user_id>', methods = ['POST'])
def user(user_id):
    if request.method == 'POST':
        """modify/update the information for <user_id>"""


teams=["Fenerbahçe","Galatasaray","Adana","Konyaspor"]
teams_yedek = list(teams)
size_team=len(teams)
if len(teams)%2!=0:
    teams.append("X")
Strength=[]
for x in teams:
    Strength.append(random.randint(1,100))
ratio=[x / sum(Strength) for x in Strength]
indis = random.choice(teams)
teams.remove(indis)
eslesmeler1 = []
eslesmeler2 = []
sonuclar1 = []
sonuclar2 = []
if size_team % 2 !=0:
    for i in range(size_team):
        if i%2==0:
            eslesmeler1.append([indis,teams[0]])
            eslesmeler2.append([teams[0],indis])
            if teams[0] != "X" and indis != "X":
                sonuclar1.append([random.randint(0, 10), random.randint(0, 10)])
                sonuclar2.append([random.randint(0, 10), random.randint(0, 10)])
            else:
                sonuclar1.append(["*", "*"])
                sonuclar2.append(["*", "*"])
        else:
            eslesmeler1.append([teams[0],indis])
            eslesmeler2.append([indis,teams[0]])
            if teams[0] != "X" and indis != "X":
                sonuclar1.append([random.randint(0, 10), random.randint(0, 10)])
                sonuclar2.append([random.randint(0, 10), random.randint(0, 10)])
            else:
                sonuclar1.append(["*", "*"])
                sonuclar2.append(["*", "*"])
        for j in range(int((size_team-2)/2)+1):
            if j % 2 == 0:
                eslesmeler1.append([teams[j+1],teams[size_team-j-1]])
                eslesmeler2.append([teams[size_team-j-1],teams[j+1]])
                if teams[j+1] != "X" and teams[size_team-j-1] != "X":
                    sonuclar1.append([random.randint(0, 10), random.randint(0, 10)])
                    sonuclar2.append([random.randint(0, 10), random.randint(0, 10)])
                else:
                    sonuclar1.append(["*", "*"])
                    sonuclar2.append(["*", "*"])
            else:
                eslesmeler1.append([teams[size_team-j-1],teams[j+1]])
                eslesmeler2.append([teams[j+1],teams[size_team-j-1]])
                if teams[j+1] != "X" and teams[size_team-j-1] != "X":
                    sonuclar1.append([random.randint(0, 10), random.randint(0, 10)])
                    sonuclar2.append([random.randint(0, 10), random.randint(0, 10)])
                else:
                    sonuclar1.append(["*", "*"])
                    sonuclar2.append(["*", "*"])
        teams = [teams[(x-1) % (len(teams))] for x in range(len(teams))]
else:
    for i in range(size_team-1):
        if i%2==0:
            eslesmeler1.append([indis,teams[0]])
            eslesmeler2.append([teams[0],indis])
            sonuclar1.append([random.randint(0, 10), random.randint(0, 10)])
            sonuclar2.append([random.randint(0, 10), random.randint(0, 10)])
        else:
            eslesmeler1.append([teams[0],indis])
            eslesmeler2.append([indis,teams[0]])
            sonuclar1.append([random.randint(0, 10), random.randint(0, 10)])
            sonuclar2.append([random.randint(0, 10), random.randint(0, 10)])
        for j in range(int((size_team-2)/2)):
            if i % 2 != 0 and j % 2 != 0:
                eslesmeler1.append([teams[j+1],teams[size_team-j-2]])
                eslesmeler2.append([teams[size_team-j-2],teams[j+1]])
                sonuclar1.append([random.randint(0, 10), random.randint(0, 10)])
                sonuclar2.append([random.randint(0, 10), random.randint(0, 10)])
            else:
                eslesmeler1.append([teams[size_team-j-2],teams[j+1]])
                eslesmeler2.append([teams[j+1],teams[size_team-j-2]])
                sonuclar1.append([random.randint(0, 10), random.randint(0, 10)])
                sonuclar2.append([random.randint(0, 10), random.randint(0, 10)])
        teams = [teams[(x-1) % (len(teams))] for x in range(len(teams))]

if size_team % 2 != 0:
    for i in range(len(eslesmeler1)):
        if i % int((size_team+1)/2) == 0:
            print("----------")
            print(str(int(i/((size_team+1)/2)+1)) + ". Hafta Programı")
            print("X işareti olan eşleşmede maç oynanmamıştır")
            print("----------")
        print(eslesmeler1[i][0] + " --- " + eslesmeler1[i][1])
else:
    for i in range(len(eslesmeler1)):
        if i % int(((size_team)/2)) == 0:
            print("----------")
            print(str(int(i/(size_team/2))+1) + ". Hafta Programı")
            print("----------")
        print(eslesmeler1[i][0] + " --- " + eslesmeler1[i][1])


if size_team % 2 != 0:
    for i in range(len(eslesmeler2)):
        if i % int((size_team+1)/2) == 0:
            print("----------")
            print(str(int(i/((size_team+1)/2)+1+len(teams))) + ". Hafta Programı")
            print("X işareti olan eşleşmede maç oynanmamıştır")
            print("----------")
        print(eslesmeler2[i][0] + " --- " + eslesmeler2[i][1])
else:
    for i in range(len(eslesmeler2)):
        if i % int(((size_team)/2)) == 0:
            print("----------")
            print(str(int(i/(size_team/2))+1+len(teams)) + ". Hafta Programı")
            print("----------")
        print(eslesmeler2[i][0] + " --- " + eslesmeler2[i][1])


if size_team % 2 != 0:
    for i in range(len(sonuclar1)):
        if i % int((size_team+1)/2) == 0:
            print("----------")
            print(str(int(i/((size_team+1)/2)+1)) + ". Hafta Sonuçları")
            print("----------")
        print(eslesmeler1[i][0]+" "+str(sonuclar1[i][0])+ " --- "+str(sonuclar1[i][1])+" "+eslesmeler1[i][1])
else:
    for i in range(len(sonuclar1)):
        if i % int(((size_team)/2)) == 0:
            print("----------")
            print(str(int(i / (size_team/2))+1) + ". Hafta Sonuçları")
            print("----------")
        print(eslesmeler1[i][0] + " " + str(sonuclar1[i][0]) + " --- " + str(sonuclar1[i][1]) + " " + eslesmeler1[i][1])

if size_team % 2 != 0:
    for i in range(len(sonuclar2)):
        if i % int((size_team+1)/2) == 0:
            print("----------")
            print(str(int(i/((size_team+1)/2)+1+len(teams))) + ". Hafta Sonuçları")
            print("----------")
        print(eslesmeler2[i][0]+" "+str(sonuclar2[i][0])+ " --- "+str(sonuclar2[i][1])+" "+eslesmeler2[i][1])
else:
    for i in range(len(sonuclar2)):
        if i % int(((size_team) / 2)) == 0:
            print("----------")
            print(str(int(i/(size_team/2))+1+len(teams)) + ". Hafta Sonuçları")
            print("----------")
        print(eslesmeler2[i][0] + " " + str(sonuclar2[i][0]) + " --- " + str(sonuclar2[i][1]) + " " + eslesmeler2[i][1])

puan_durumu = numpy.zeros(len(teams_yedek))
goal_diff = numpy.zeros(len(teams_yedek))
goal = numpy.zeros(len(teams_yedek))
index_number = numpy.zeros(len(teams_yedek))
print("-----------------------")
print("Lig Başlamadan Önce Şampiyonluk Olasılıkları")
print(ratio)
print("-----------------------")
if (size_team % 2) != 0: #\\ Ligin ilk yarısı
    for t in range(int(len(eslesmeler1)/int((size_team+1)/2))):
        print("------")
        print(str(t+1) + ". Hafta Puan Cetveli")
        for i in range(int((size_team+1)/2)):
                if eslesmeler1[t*int((size_team+1)/2)+i][0] != "X" and eslesmeler1[t*int((size_team+1)/2)+i][1] != "X":
                    if int(sonuclar1[t*int((size_team+1)/2)+i][0]) > int(sonuclar1[t*int((size_team+1)/2)+i][1]):
                        x = teams_yedek.index(eslesmeler1[t*int((size_team+1)/2)+i][0])
                        y = teams_yedek.index(eslesmeler1[t*int((size_team+1)/2)+i][1])
                        puan_durumu[x] +=3
                        goal_diff[x] +=int(sonuclar1[t*int((size_team+1)/2)+i][0])-int(sonuclar1[t*int((size_team+1)/2)+i][1])
                        goal[x] += int(sonuclar1[t*int((size_team+1)/2)+i][0])
                        index_number[x] = x
                        index_number[y] = y
                        puan_durumu[y] +=0
                        goal_diff[y] +=int(sonuclar1[t*int((size_team+1)/2)+i][1])-int(sonuclar1[t*int((size_team+1)/2)+i][0])
                        goal[y] += int(sonuclar1[t*int((size_team+1)/2)+i][1])
                    elif int(sonuclar1[t*int((size_team+1)/2)+i][0]) == int(sonuclar1[t*int((size_team+1)/2)+i][1]):
                        x = teams_yedek.index(eslesmeler1[t*int((size_team+1)/2)+i][0])
                        y = teams_yedek.index(eslesmeler1[t*int((size_team+1)/2)+i][1])
                        index_number[x] = x
                        index_number[y] = y
                        puan_durumu[x] +=1
                        goal_diff[x] +=0
                        goal[x] += int(sonuclar1[t*int((size_team+1)/2)+i][0])
                        puan_durumu[y] +=1
                        goal_diff[y] +=0
                        goal[y] += int(sonuclar1[t*int((size_team+1)/2)+i][1])
                    else:
                        x = teams_yedek.index(eslesmeler1[t*int((size_team+1)/2)+i][0])
                        y = teams_yedek.index(eslesmeler1[t*int((size_team+1)/2)+i][1])
                        index_number[x] = x
                        index_number[y] = y
                        puan_durumu[x] +=0
                        goal_diff[x] +=int(sonuclar1[t*int((size_team+1)/2)+i][0])-int(sonuclar1[t*int((size_team+1)/2)+i][1])
                        goal[x] += int(sonuclar1[t*int((size_team+1)/2)+i][0])
                        puan_durumu[y] +=3
                        goal_diff[y] +=int(sonuclar1[t*int((size_team+1)/2)+i][1])-int(sonuclar1[t*int((size_team+1)/2)+i][0])
                        goal[y] += int(sonuclar1[t*int((size_team+1)/2)+i][1])
                    if eslesmeler1[i][0] == "X":
                        x = teams_yedek.index(eslesmeler1[t*int((size_team+1)/2)+i][1])
                        index_number[x] = x
                        puan_durumu[x] +=0
                        goal_diff[x] +=0
                        goal[x] += 0
                    else:
                        x = teams_yedek.index(eslesmeler1[t*int((size_team+1)/2)+i][0])
                        index_number[x] = x
                        puan_durumu[x] +=0
                        goal_diff[x] +=0
                        goal[x] += 0

        name_team = []
        taken_point = []
        average = []
        goal_number = []
        sonuc= []
        puanla = []
        sorted_name_team = {}
        sorted_goal_number = numpy.zeros(len(teams_yedek))
        sorted_average = numpy.zeros(len(teams_yedek))
        tested = []
        tested2 = []
        ratio2 = []
        for t in range(len(teams_yedek)):
            puanla.append(teams_yedek[int(index_number[t])])
            puanla.append(puan_durumu[t])
            puanla.append(goal_diff[t])
            puanla.append(goal[t])
            sonuc=[puanla]
            name_team.append(teams_yedek[int(index_number[t])])
            taken_point.append(int(puan_durumu[t]))
            average.append(int(goal_diff[t]))
            goal_number.append(int(goal[t]))
            tested.append(0.65*int(puan_durumu[t])+int(goal_diff[t])*0.3+0.05*int(goal[t]))
        for i in range(len(taken_point) - 1):
            enk = taken_point[i]
            enk_indis = i
            for j in range(i + 1, len(taken_point)):
                if taken_point[j] < enk:
                    enk = taken_point[j]
                    enk_indis = j
            depo = taken_point[i]
            taken_point[i] = taken_point[enk_indis]
            taken_point[enk_indis] = depo
        for i in range(len(tested)-1):
            enk = tested[i]
            enk_indis = i
            for j in range(i + 1, len(tested)):
                if tested[j] < enk:
                    enk = tested[j]
                    enk_indis = j
            depo = tested[i]
            tested[i] = tested[enk_indis]
            tested[enk_indis] = depo
        for i in range(len(average)):
            ind = tested.index(0.65*int(puan_durumu[i])+int(average[i])*0.3+0.05*int(goal_number[i]))
            sorted_average[ind]=int(average[i])
            sorted_goal_number[ind]=int(goal_number[i])
            tested2.append(int(sorted_goal_number[ind]))
            tested2.append(int(sorted_goal_number[ind]))
            son = tested.index(0.65*int(sonuc[0][4*i+1])+int(sonuc[0][4*i+2])*0.3+0.05*int(sonuc[0][4*i+3]))
            sorted_name_team[son] = str(name_team[i])
            ratio2.append(ratio[i] + (float(ratio[i]) * (1 - float(ratio[i])) * (1 / ((len(average) / 2) * (1 + (len(average) / 2)))) * (i - ((len(average) - 1) / 2))))


        ratio=ratio2
        print("------")
        print("Teams:",sorted_name_team)
        print("Points:",taken_point)
        print("Average:",sorted_average)
        print("Number of Goal:",sorted_goal_number)
        print("------")
        print("Şampiyonluk Olasılıkları")
        print(ratio2)
        print("------")
else:
    for t in range(int(len(eslesmeler1)/int((size_team)/2))):
        print(str(t+1) + ". Score Sheet")
        for i in range(int((size_team)/2)):
                if int(sonuclar1[t*int((size_team)/2)+i][0]) > int(sonuclar1[t*int((size_team)/2)+i][1]):
                    x = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][0])
                    y = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][1])
                    puan_durumu[x] +=3
                    goal_diff[x] +=int(sonuclar1[t*int((size_team)/2)+i][0])-int(sonuclar1[t*int((size_team)/2)+i][1])
                    goal[x] += int(sonuclar1[t*int((size_team)/2)+i][0])
                    index_number[x] = x
                    index_number[y] = y
                    puan_durumu[y] +=0
                    goal_diff[y] +=int(sonuclar1[t*int((size_team)/2)+i][1])-int(sonuclar1[t*int((size_team)/2)+i][0])
                    goal[y] += int(sonuclar1[t*int((size_team)/2)+i][1])
                elif int(sonuclar1[t*int((size_team)/2)+i][0]) == int(sonuclar1[t*int((size_team)/2)+i][1]):
                    x = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][0])
                    y = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][1])
                    index_number[x] = x
                    index_number[y] = y
                    puan_durumu[x] +=1
                    goal_diff[x] +=0
                    goal[x] += int(sonuclar1[t*int((size_team)/2)+i][0])
                    puan_durumu[y] +=1
                    goal_diff[y] +=0
                    goal[y] += int(sonuclar1[t*int((size_team)/2)+i][1])
                else:
                    x = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][0])
                    y = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][1])
                    index_number[x] = x
                    index_number[y] = y
                    puan_durumu[x] +=0
                    goal_diff[x] +=int(sonuclar1[t*int((size_team)/2)+i][0])-int(sonuclar1[t*int((size_team)/2)+i][1])
                    goal[x] += int(sonuclar1[t*int((size_team)/2)+i][0])
                    puan_durumu[y] +=3
                    goal_diff[y] +=int(sonuclar1[t*int((size_team)/2)+i][1])-int(sonuclar1[t*int((size_team)/2)+i][0])
                    goal[y] += int(sonuclar1[t*int((size_team)/2)+i][1])

        name_team = []
        taken_point = []
        average = []
        goal_number = []
        sonuc= []
        puanla = []
        sorted_name_team = {}
        sorted_goal_number = numpy.zeros(len(teams_yedek))
        sorted_average = numpy.zeros(len(teams_yedek))
        tested = []
        tested2 = []
        ratio2 = []
        for t in range(len(teams_yedek)):
            puanla.append(teams_yedek[int(index_number[t])])
            puanla.append(puan_durumu[t])
            puanla.append(goal_diff[t])
            puanla.append(goal[t])
            sonuc=[puanla]
            name_team.append(teams_yedek[int(index_number[t])])
            taken_point.append(int(puan_durumu[t]))
            average.append(int(goal_diff[t]))
            goal_number.append(int(goal[t]))
            tested.append(0.65*int(puan_durumu[t])+int(goal_diff[t])*0.3+0.05*int(goal[t]))
        for i in range(len(taken_point) - 1):
            enk = taken_point[i]
            enk_indis = i
            for j in range(i + 1, len(taken_point)):
                if taken_point[j] < enk:
                    enk = taken_point[j]
                    enk_indis = j
            depo = taken_point[i]
            taken_point[i] = taken_point[enk_indis]
            taken_point[enk_indis] = depo
        for i in range(len(tested)-1):
            enk = tested[i]
            enk_indis = i
            for j in range(i + 1, len(tested)):
                if tested[j] < enk:
                    enk = tested[j]
                    enk_indis = j
            depo = tested[i]
            tested[i] = tested[enk_indis]
            tested[enk_indis] = depo
        for i in range(len(average)):
            ind = tested.index(0.65*int(puan_durumu[i])+int(average[i])*0.3+0.05*int(goal_number[i]))
            sorted_average[ind]=int(average[i])
            sorted_goal_number[ind]=int(goal_number[i])
            tested2.append(int(sorted_goal_number[ind]))
            tested2.append(int(sorted_goal_number[ind]))
            son = tested.index(0.65*int(sonuc[0][4*i+1])+int(sonuc[0][4*i+2])*0.3+0.05*int(sonuc[0][4*i+3]))
            sorted_name_team[son] = str(name_team[i])
            if i < len(average)/2:
                ratio2.append(ratio[i] + (float(ratio[i])*(1-float(ratio[i])) * (1 / ((len(average) / 2) * (1 + (len(average) / 2)))) * (i- len(average) / 2)))
            else:
                ratio2.append(ratio[i] + (float(ratio[i]) * (1 - float(ratio[i])) * (1 / ((len(average) / 4) * (1 + (len(average) / 4)))) * (1+i - (len(average) / 2))))


        ratio=ratio2
        print("------")
        print("Teams:",sorted_name_team)
        print("Points:",taken_point)
        print("Average:",sorted_average)
        print("Number of Goal:",sorted_goal_number)
        print("------")
        print("Şampiyonluk Olasılıkları")
        print(ratio2)
        print("------")

if (size_team % 2) != 0: #\\ Ligin ikinci yarısı
    for t in range(int(len(eslesmeler2)/int((size_team+1)/2))):
        print("------")
        print(str(int(t+(size_team+1))) + ". Hafta Puan Cetveli")
        for i in range(int((size_team+1)/2)):
                if eslesmeler2[t*int((size_team+1)/2)+i][0] != "X" and eslesmeler2[t*int((size_team+1)/2)+i][1] != "X":
                    if int(sonuclar2[t*int((size_team+1)/2)+i][0]) > int(sonuclar2[t*int((size_team+1)/2)+i][1]):
                        x = teams_yedek.index(eslesmeler2[t*int((size_team+1)/2)+i][0])
                        y = teams_yedek.index(eslesmeler2[t*int((size_team+1)/2)+i][1])
                        puan_durumu[x] +=3
                        goal_diff[x] +=int(sonuclar2[t*int((size_team+1)/2)+i][0])-int(sonuclar2[t*int((size_team+1)/2)+i][1])
                        goal[x] += int(sonuclar2[t*int((size_team+1)/2)+i][0])
                        index_number[x] = x
                        index_number[y] = y
                        puan_durumu[y] +=0
                        goal_diff[y] +=int(sonuclar2[t*int((size_team+1)/2)+i][1])-int(sonuclar2[t*int((size_team+1)/2)+i][0])
                        goal[y] += int(sonuclar2[t*int((size_team+1)/2)+i][1])
                    elif int(sonuclar2[t*int((size_team+1)/2)+i][0]) == int(sonuclar2[t*int((size_team+1)/2)+i][1]):
                        x = teams_yedek.index(eslesmeler2[t*int((size_team+1)/2)+i][0])
                        y = teams_yedek.index(eslesmeler2[t*int((size_team+1)/2)+i][1])
                        index_number[x] = x
                        index_number[y] = y
                        puan_durumu[x] +=1
                        goal_diff[x] +=0
                        goal[x] += int(sonuclar2[t*int((size_team+1)/2)+i][0])
                        puan_durumu[y] +=1
                        goal_diff[y] +=0
                        goal[y] += int(sonuclar2[t*int((size_team+1)/2)+i][1])
                    else:
                        x = teams_yedek.index(eslesmeler2[t*int((size_team+1)/2)+i][0])
                        y = teams_yedek.index(eslesmeler2[t*int((size_team+1)/2)+i][1])
                        index_number[x] = x
                        index_number[y] = y
                        puan_durumu[x] +=0
                        goal_diff[x] +=int(sonuclar2[t*int((size_team+1)/2)+i][0])-int(sonuclar2[t*int((size_team+1)/2)+i][1])
                        goal[x] += int(sonuclar2[t*int((size_team+1)/2)+i][0])
                        puan_durumu[y] +=3
                        goal_diff[y] +=int(sonuclar2[t*int((size_team+1)/2)+i][1])-int(sonuclar2[t*int((size_team+1)/2)+i][0])
                        goal[y] += int(sonuclar2[t*int((size_team+1)/2)+i][1])
                    if eslesmeler2[i][0] == "X":
                        x = teams_yedek.index(eslesmeler2[t*int((size_team+1)/2)+i][1])
                        index_number[x] = x
                        puan_durumu[x] +=0
                        goal_diff[x] +=0
                        goal[x] += 0
                    else:
                        x = teams_yedek.index(eslesmeler2[t*int((size_team+1)/2)+i][0])
                        index_number[x] = x
                        puan_durumu[x] +=0
                        goal_diff[x] +=0
                        goal[x] += 0

        name_team = []
        taken_point = []
        average = []
        goal_number = []
        sonuc= []
        puanla = []
        sorted_name_team = {}
        sorted_goal_number = numpy.zeros(len(teams_yedek))
        sorted_average = numpy.zeros(len(teams_yedek))
        tested = []
        tested2 = []
        ratio2 = []
        for t in range(len(teams_yedek)):
            puanla.append(teams_yedek[int(index_number[t])])
            puanla.append(puan_durumu[t])
            puanla.append(goal_diff[t])
            puanla.append(goal[t])
            sonuc=[puanla]
            name_team.append(teams_yedek[int(index_number[t])])
            taken_point.append(int(puan_durumu[t]))
            average.append(int(goal_diff[t]))
            goal_number.append(int(goal[t]))
            tested.append(0.65*int(puan_durumu[t])+int(goal_diff[t])*0.3+0.05*int(goal[t]))
        for i in range(len(taken_point) - 1):
            enk = taken_point[i]
            enk_indis = i
            for j in range(i + 1, len(taken_point)):
                if taken_point[j] < enk:
                    enk = taken_point[j]
                    enk_indis = j
            depo = taken_point[i]
            taken_point[i] = taken_point[enk_indis]
            taken_point[enk_indis] = depo
        for i in range(len(tested)-1):
            enk = tested[i]
            enk_indis = i
            for j in range(i + 1, len(tested)):
                if tested[j] < enk:
                    enk = tested[j]
                    enk_indis = j
            depo = tested[i]
            tested[i] = tested[enk_indis]
            tested[enk_indis] = depo
        for i in range(len(average)):
            ind = tested.index(0.65*int(puan_durumu[i])+int(average[i])*0.3+0.05*int(goal_number[i]))
            sorted_average[ind]=int(average[i])
            sorted_goal_number[ind]=int(goal_number[i])
            tested2.append(int(sorted_goal_number[ind]))
            tested2.append(int(sorted_goal_number[ind]))
            son = tested.index(0.65*int(sonuc[0][4*i+1])+int(sonuc[0][4*i+2])*0.3+0.05*int(sonuc[0][4*i+3]))
            sorted_name_team[son] = str(name_team[i])
            if i < len(average)-1:
                ratio2.append(ratio[i] - (float(ratio[i])*(1-float(ratio[i])) * (1 / ((len(average)/2) * (1 + (len(average)/2)))) * (i - (len(average) / 2)-1)))

            else:
                ratio2.append(ratio[i] + (float(ratio[i]) * (1 - float(ratio[i])) * (1 / ((len(average) / 2) * (1 + (len(average) / 2)))) * (1+i - len(average) / 2)))


        ratio=ratio2
        print("------")
        print("Teams:",sorted_name_team)
        print("Points:",taken_point)
        print("Average:",sorted_average)
        print("Number of Goal:",sorted_goal_number)
        print("------")
        print("Şampiyonluk Olasılıkları")
        print(ratio2)
        print("------")
else:
    for t in range(int(len(eslesmeler1)/int((size_team)/2))):
        print(str(int(t+size_team)) + ". Score Sheet")
        for i in range(int((size_team)/2)):
                if int(sonuclar1[t*int((size_team)/2)+i][0]) > int(sonuclar1[t*int((size_team)/2)+i][1]):
                    x = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][0])
                    y = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][1])
                    puan_durumu[x] +=3
                    goal_diff[x] +=int(sonuclar1[t*int((size_team)/2)+i][0])-int(sonuclar1[t*int((size_team)/2)+i][1])
                    goal[x] += int(sonuclar1[t*int((size_team)/2)+i][0])
                    index_number[x] = x
                    index_number[y] = y
                    puan_durumu[y] +=0
                    goal_diff[y] +=int(sonuclar1[t*int((size_team)/2)+i][1])-int(sonuclar1[t*int((size_team)/2)+i][0])
                    goal[y] += int(sonuclar1[t*int((size_team)/2)+i][1])
                elif int(sonuclar1[t*int((size_team)/2)+i][0]) == int(sonuclar1[t*int((size_team)/2)+i][1]):
                    x = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][0])
                    y = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][1])
                    index_number[x] = x
                    index_number[y] = y
                    puan_durumu[x] +=1
                    goal_diff[x] +=0
                    goal[x] += int(sonuclar1[t*int((size_team)/2)+i][0])
                    puan_durumu[y] +=1
                    goal_diff[y] +=0
                    goal[y] += int(sonuclar1[t*int((size_team)/2)+i][1])
                else:
                    x = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][0])
                    y = teams_yedek.index(eslesmeler1[t*int((size_team)/2)+i][1])
                    index_number[x] = x
                    index_number[y] = y
                    puan_durumu[x] +=0
                    goal_diff[x] +=int(sonuclar1[t*int((size_team)/2)+i][0])-int(sonuclar1[t*int((size_team)/2)+i][1])
                    goal[x] += int(sonuclar1[t*int((size_team)/2)+i][0])
                    puan_durumu[y] +=3
                    goal_diff[y] +=int(sonuclar1[t*int((size_team)/2)+i][1])-int(sonuclar1[t*int((size_team)/2)+i][0])
                    goal[y] += int(sonuclar1[t*int((size_team)/2)+i][1])

        name_team = []
        taken_point = []
        average = []
        goal_number = []
        sonuc= []
        puanla = []
        sorted_name_team = {}
        sorted_goal_number = numpy.zeros(len(teams_yedek))
        sorted_average = numpy.zeros(len(teams_yedek))
        tested = []
        tested2 = []
        ratio2 = []
        for t in range(len(teams_yedek)):
            puanla.append(teams_yedek[int(index_number[t])])
            puanla.append(puan_durumu[t])
            puanla.append(goal_diff[t])
            puanla.append(goal[t])
            sonuc=[puanla]
            name_team.append(teams_yedek[int(index_number[t])])
            taken_point.append(int(puan_durumu[t]))
            average.append(int(goal_diff[t]))
            goal_number.append(int(goal[t]))
            tested.append(0.65*int(puan_durumu[t])+int(goal_diff[t])*0.3+0.05*int(goal[t]))
        for i in range(len(taken_point) - 1):
            enk = taken_point[i]
            enk_indis = i
            for j in range(i + 1, len(taken_point)):
                if taken_point[j] < enk:
                    enk = taken_point[j]
                    enk_indis = j
            depo = taken_point[i]
            taken_point[i] = taken_point[enk_indis]
            taken_point[enk_indis] = depo
        for i in range(len(tested)-1):
            enk = tested[i]
            enk_indis = i
            for j in range(i + 1, len(tested)):
                if tested[j] < enk:
                    enk = tested[j]
                    enk_indis = j
            depo = tested[i]
            tested[i] = tested[enk_indis]
            tested[enk_indis] = depo

        for i in range(len(average)):
            ind = tested.index(0.65*int(puan_durumu[i])+int(average[i])*0.3+0.05*int(goal_number[i]))
            sorted_average[ind]=int(average[i])
            sorted_goal_number[ind]=int(goal_number[i])
            tested2.append(int(sorted_goal_number[ind]))
            son = tested.index(0.65*int(sonuc[0][4*i+1])+int(sonuc[0][4*i+2])*0.3+0.05*int(sonuc[0][4*i+3]))
            sorted_name_team[son] = str(name_team[i])
            if i < len(average)-1:
                ratio2.append(ratio[i] - (float(ratio[i])*(1-float(ratio[i])) * (1 / ((len(average)) * (1 + (len(average))))) * (i - (len(average) / 2)-1)))

            else:
                ratio2.append(ratio[i] + (float(ratio[i]) * (1 - float(ratio[i])) * (1 / ((len(average) /2) * (1 + (len(average) /2)))) * (1+i - len(average) / 2)))

        ratio=ratio2
        print("------")
        print("Teams:",sorted_name_team)
        print("Points:",taken_point)
        print("Average:",sorted_average)
        print("Number of Goal:",sorted_goal_number)
        print("------")

        print("Şampiyonluk Olasılıkları")
        print(ratio2)
        print("------")